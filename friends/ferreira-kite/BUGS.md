# Confirmed KITE correctness bugs

Pinned upstream: **a1e1f7ce6e48505ce2655315c2565446315a67e0**, default `master`, shallow clone in `upstream/kite/`.
Latest release: **1.1**, published 2025-04-29, tag commit `078c23511bf63b6478af39f6a44d6e03828ec09a` (`sources/releases.json`, `sources/tags.json`).
Aires Ferreira is named under **Project founders** in the pinned [README](upstream/kite/README.md), and is an author of [João et al., KITE, R. Soc. Open Sci. 7, 191809 (2020)](https://arxiv.org/abs/1910.05194), whose PDF is retained in `sources/kite-paper.pdf`.

These five bugs were not found in the reviewed public issue/PR history. This is a local software repair result, **not a novel scientific result: NEW: no**. No paper number was improved, stated scientific open problem settled, or new-data prediction tested. No predictive model or predictive score is reported; trivial/simple/model baselines and SBS are inapplicable.

Each section links a runnable repro with pinned output, independently computed correct output, repaired output, a minimal root-relative git patch, and a normal-input regression comparison. Independent numerical checks are separately written Python/NumPy implementations, not a second person or an external referee. Nothing was sent or published.

## KITE-CFG-001 — energy shift changes off-diagonal onsite terms

- **Location:** `kite.py:1261`.
- **Wrong:** subtracting the scalar energy shift broadcasts it to every element of a multi-orbital onsite matrix. Rescaling requires subtraction of shift × identity.
- **Before → correct/after:** onsite H=`[[1,.25],[.25,2]]` eV, bounds [-1,5]; exported physical eigenvalues `[-0.3200274723,3.3200274723]` → `[0.9409830056,2.0590169944]` eV.
- **Effect:** nonzero shifts silently change hybridization, splittings and the resulting spectral/transport problem; automatic asymmetric bounds can also produce nonzero shifts, although that route was not exercised.
- **Evidence:** [repro and reasoning](repro/KITE-CFG-001/README.md), [before](repro/KITE-CFG-001/before.txt), [after](repro/KITE-CFG-001/after.txt), [patch](repro/KITE-CFG-001/patch.diff).
- **Independent check/control:** decode the actual HDF5 hopping representation, invert rescaling and diagonalize in plain NumPy. Zero-shift and one-orbital controls retain identical dataset values.
- **Confidence:** high for the exporter with explicit bounds. Pybinding itself was not installed; its import is stubbed, no API calls are made, and the fixture uses upstream `lattice.py` with the same matrix representation as pybinding's retained source.
- **Reason:** [KITE Eq. (2.14)](https://arxiv.org/abs/1910.05194); [Weiße et al. (2006), Eq. (24)](https://arxiv.org/abs/cond-mat/0504627).

## KITE-CFG-002 — imaginary onsite couplings disappear with default real configuration

- **Location:** `kite.py:1187–1192`, with loss during real hopping export at lines 1309 and 1435.
- **Wrong:** automatic complex detection checks intersite hoppings but ignores onsite matrices. Default `is_complex=False` silently drops imaginary onsite entries.
- **Before → correct/after:** Hermitian H=`[[0,-i],[i,0]]` eV yields eigenvalues `[0,0]` → `[-1,1]` eV; Tr(H²) `0` → `2` eV². `IS_COMPLEX` becomes 1.
- **Effect:** onsite spin/orbital terms can be removed, changing the Hamiltonian rather than its numerical precision. Explicit `is_complex=True` avoids this bug.
- **Evidence:** [repro and reasoning](repro/KITE-CFG-002/README.md), [before](repro/KITE-CFG-002/before.txt), [after](repro/KITE-CFG-002/after.txt), [patch](repro/KITE-CFG-002/patch.diff).
- **Independent check/control:** independent HDF5 decoding, NumPy eigvalsh and the identity sigma_y²=I. Explicit-complex and ordinary real controls have identical HDF5 dataset values before/after.
- **Confidence:** high for the explicit-bounds exporter; same import-only pybinding limitation as CFG-001.
- **Reason:** Hermitian-matrix spectral decomposition; [KITE Sec. 2(a)](https://arxiv.org/abs/1910.05194).

## KITE-TOOLS-001 — optical conductivity uses stale inverse temperature

- **Location:** `tools/Src/OptCond_1order/conductivity_optical.cpp:180`; beta consumed at lines 391 and 623.
- **Wrong:** reading the HDF5 temperature does not refresh beta=1/temperature. Without CLI `-T`, both optical calculation branches use the default k_B*T=0.001 eV, regardless of the stored value.
- **Before → correct/after:** two-site molecule at omega=0.6 eV and requested k_B*T=0.2 eV: sigma `4.78760 + 0.782720i` → `3.02977 + 0.480812i` in e²/h. Independent result `3.0297736361 + 0.4808121743i`.
- **Effect:** temperature dependence and thermal occupation of optical transitions are wrong while the program prints the requested temperature. No Kelvin-conversion bug is claimed: temperature is k_B*T in energy units, per the pinned FAQ.
- **Evidence:** [repro and parameters](repro/KITE-TOOLS-001/README.md), [pinned spectrum](repro/KITE-TOOLS-001/before/hot.dat), [repaired spectrum](repro/KITE-TOOLS-001/after/hot.dat), [independent numbers](repro/KITE-TOOLS-001/correct.json), [patch](repro/KITE-TOOLS-001/patch.diff).
- **Independent check/control:** exact NumPy eigensystem, finite Jackson spectral projectors and direct scalar resolvents in the Kubo trace; matched moment count, grid and broadening. Default-temperature control is byte-identical.
- **Confidence:** high. Real compiled post-processor, no mocks. The independent calculation agrees at all three frequencies within the precision of saved text.
- **Reason:** Fermi occupation definition and [KITE Eq. (2.23)](https://arxiv.org/abs/1910.05194).

## KITE-TOOLS-002 — Green-function LDOS omits 1/pi

- **Location:** `tools/Src/Spectral/ldos.cpp:277`.
- **Wrong:** Green LDOS uses −Im(G), rather than −Im(G)/pi; total DOS already contains the factor.
- **Before → correct/after:** zero-energy isolated level, eta=0.2 eV: rho(0) `5` → `1.59155` 1/eV; exact `1.591549430918953`. The other tested energies show the same factor of pi.
- **Effect:** absolute local spectral weight and integrated state counts are too large by pi for the `green` kernel. This is distinct from Lorentz damping coefficients.
- **Evidence:** [repro and definition](repro/KITE-TOOLS-002/README.md), [before](repro/KITE-TOOLS-002/before.txt), [after](repro/KITE-TOOLS-002/after.txt), [patch](repro/KITE-TOOLS-002/patch.diff).
- **Independent check/control:** NumPy spectral decomposition and the defining resolvent/Lorentzian. One thread, 128 moments; truncation is negligible at this broadening. Jackson-kernel files are byte-identical.
- **Confidence:** high; actual compiled post-processor, agreement at all three energies.
- **Reason:** spectral-density definition; [KITE Eqs. (2.19)–(2.20), Fig. 1(a)](https://arxiv.org/abs/1910.05194).

## KITE-TOOLS-003 — threaded LDOS silently loses remainder moments

- **Location:** `tools/Src/Spectral/ldos.cpp:245–265`.
- **Wrong:** P threads each receive floor(M/P) moments; remaining moments are discarded. No divisibility restriction is enforced for the supported `-M` override.
- **Before → correct/after:** five-moment Jackson LDOS of an isolated zero-energy level: one thread `0.742723`, two threads `0.689671` → both `0.742723` 1/eV; independent `0.7427230677621784`.
- **Effect:** changing decomposition/thread count changes spectral results; if threads outnumber moments, all contributions can be lost. The demonstrated case uses only two threads.
- **Evidence:** [repro and reasoning](repro/KITE-TOOLS-003/README.md), [before](repro/KITE-TOOLS-003/before.txt), [after](repro/KITE-TOOLS-003/after.txt), [patch](repro/KITE-TOOLS-003/patch.diff).
- **Independent check/control:** NumPy eigensystem and complete finite Jackson expansion. Input contains 128 moments, with a legal `-M 5` post-processing override, avoiding any untested odd-moment core calculation. Four-moment two-thread output is byte-identical.
- **Confidence:** high for Jackson LDOS, actual compiled post-processor. Separate Green indexing concern below remains outside this fix.
- **Reason:** finite Chebyshev/Jackson expansion, [Weiße et al., Eqs. (71)–(72)](https://arxiv.org/abs/cond-mat/0504627).

## Suspected — not confirmed and not included as fixes

1. **Green LDOS moment index across threads:** `tools/Src/Spectral/ldos.cpp:277` passes local `m` to `green`, while the Jackson path uses the global index. Not independently isolated here. TOOLS-003 fixes partition sizes/offsets but does not claim to resolve this separate issue.
2. **Odd requested core moment counts:** `Src/Simulation/SimulationLMU.cpp:98–110` and `Src/Tools/Gamma1D.cpp:67–77` process pairs and write the n+1 entry without an obvious odd-tail guard. No runnable KITEx binary, so no memory-error or incorrect-output claim.
3. **Custom potential with nonzero energy shift:** `Src/Hamiltonian/Hamiltonian.cpp:387` subtracts Eshift from an additive local potential, while base onsite terms were already shifted. Additive use appears in `Src/Vector/KPM_Vector2D.cpp:475–478`. This needs a running core and a documented potential-definition check; no confirmed double-shift claim.

## Known issues excluded and upstream history reviewed

Read all 36 public issue/PR entries, all 28 PR bodies, all 19 issue comments and the one review comment before reporting; there were no open issues or PRs. Raw API snapshots are under `sources/` (`issues.json`, `pulls.json`, `all-issue-comments.json`, `all-review-comments.json`). Numerical cleanup PRs #4, #5, #6, #9 and recent #35–37 have retained diffs/comments. None contains the five fixes above. In particular:

- [#1](https://github.com/quantum-kite/kite/pull/1), [#2](https://github.com/quantum-kite/kite/pull/2), [#7](https://github.com/quantum-kite/kite/issues/7), [#8](https://github.com/quantum-kite/kite/issues/8), [#11](https://github.com/quantum-kite/kite/pull/11), [#13](https://github.com/quantum-kite/kite/issues/13): build/install/packaging and missing/old dependencies. Local build failures are recorded as limitations, not new bugs.
- [#14](https://github.com/quantum-kite/kite/issues/14): missing release 1.1 tag, restored; excluded.
- [#15](https://github.com/quantum-kite/kite/issues/15): TILE=8 size restrictions and large unit cells; excluded. Tiny post-processing fixtures do not claim KITEx can run prohibited lattice sizes.
- [#17](https://github.com/quantum-kite/kite/issues/17): server-dependent DOS/DC NaNs without a minimal input; no claim to diagnose it or report it again.
- [#5](https://github.com/quantum-kite/kite/pull/5), [#6](https://github.com/quantum-kite/kite/pull/6): second-order Gamma2 frequency argument already questioned in upstream comments; excluded.
- [#35–37](https://github.com/quantum-kite/kite/pull/37): the new `lattice.py` alternative; not itself reported as a bug. The latest four commits, all dated 2026-10-14, concern only this addition and merges. `sources/commits-six-months.json` covers 2026-05-06 onward; `sources/branches.json` also records development heads.

## Scope and use

Use [combined.patch](combined.patch) to apply all five repairs together; the two standalone LDOS patches overlap, so avoid concatenating their diffs. The combined patch applies cleanly to the pin and its compiled post-processing plus both config repros agree with the isolated repairs (`checks/combined/check-output.txt`).

The normal chain, square-lattice and graphene DOS checks use independent exact spectra and a matched 64-moment Jackson expansion (`checks/dos_closed_forms.py`, `checks/dos/results.json`). The zero-current atomic optical check returns zero (`checks/zero_current/optcond.dat`). These validate the post-processing layer with exact supplied moments; they do **not** validate stochastic moments or the KITEx recursion.

KITEx failed two honest attempts: missing Eigen/OpenMP headers first; then Apple libc++ lacks std::cyl_bessel_j in the wavepacket translation unit. Core build work stopped. KITE-tools compiled, then linked successfully with explicit installed libomp. Dependencies were built/installed only inside this working directory, apart from reuse of already-installed Homebrew libomp. Python exporter tests do not call pybinding. Source remains unchanged at the pin; all changes are local diff artifacts and patched test copies. No issue, PR, fork, comment, or contact was made.
