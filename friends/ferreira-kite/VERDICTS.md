# Independent KITE referee verdicts

Refereed locally on 2026-11-06 against fresh clone commit `a1e1f7ce6e48505ce2655315c2565446315a67e0`. Only the hunter's claim document and report were read; none of their scripts, patches, fixtures or output files was run, imported or copied. The suspected list was excluded.

| ID | Verdict | My repro path | Effect on users' results |
|---|---|---|---|
| KITE-CFG-001 | **CONFIRMED** | [repro/config/run.py](repro/config/run.py), [result](repro/config/shifted_diagonal.json) | Nonzero energy shift invents interorbital couplings, even for diagonal onsite matrices, changing the exported Hamiltonian and spectrum. Exporter-only execution; pybinding limitation below. |
| KITE-CFG-002 | **INTENDED** | [repro/config/run.py](repro/config/run.py), [default](repro/config/imaginary_default.json), [explicit complex](repro/config/imaginary_explicit_complex.json) | Imaginary onsite entries are lost in documented real-only mode; setting `is_complex=True` preserves them. Incomplete automatic detection is a safeguard inconsistency, not a demonstrated violation of the documented mode contract. |
| KITE-TOOLS-001 | **CONFIRMED** | [repro/optical/run.py](repro/optical/run.py), [scalar reference](repro/optical/scalar_reference.py), [results](repro/optical/results.json) | File temperature is printed but ignored in both optical calculation branches, so finite-temperature spectra use the default cold occupations. |
| KITE-TOOLS-002 | **CONFIRMED** | [repro/ldos/run.py](repro/ldos/run.py), [results](repro/ldos/results.json) | The documented Green LDOS kernel returns spectral density too large by a factor of pi. |
| KITE-TOOLS-003 | **CONFIRMED** | [repro/ldos/run.py](repro/ldos/run.py), [results](repro/ldos/results.json) | A non-divisible moment count silently loses its remainder on multiple threads, making Jackson LDOS depend on decomposition. Divisible counts are unaffected in the control. |

## Ranked findings

1. **TOOLS-001: ignored optical temperature.** Affects the ordinary file-driven workflow and both calculation branches, while displaying the requested temperature. Explicit CLI `-T` avoids it. The numerical effect is substantial in the independent molecule below.
2. **CFG-001: onsite energy rescaling changes the physical model.** Affects valid multi-orbital matrices whenever the energy shift is nonzero; even zero off-diagonal entries become couplings. Manual asymmetric bounds are explicitly documented. Zero shift and single-orbital inputs passed the controls.
3. **TOOLS-002: absolute Green LDOS normalization.** Every tested energy on the supported `green` path has the same factor-of-pi error. This changes local spectral weight and state counts. The default Jackson path does not execute the faulty expression.
4. **TOOLS-003: lost threaded moments.** A supported `-M` override can change results solely through the decomposition. Lower priority because it requires a non-divisible count; usual divisible counts avoid this failure.

CFG-002 is excluded from this correctness-bug ranking. Nothing has been sent to the author or anyone else. These are proposed communication priorities based on demonstrated numerical effects and documented paths; Ricardo reads first and the friend decides whether they care.

## Executed inputs and independent answers

### CFG-001 — diagonal onsite matrix acquires coupling

The cited [kite.py:1261](upstream/kite/kite.py#L1261) subtracts a scalar from the entire onsite matrix. For my input `H = diag(1,3)` eV and bounds `[-1,5]`, the scale is 3 and shift is 2. The correct scaled matrix is `diag(-1/3,1/3)`; its off-diagonal entries stay zero.

Decoding the actual exported HDF5 hopping datasets and undoing rescaling instead gives physical `[[1,-2],[-2,3]]` eV. Its eigenvalues are `2 ± sqrt(5)` = `[-0.2360679775,4.2360679775]` eV; the input's exact eigenvalues are `[1,3]`. This demonstrates corruption even without an original interorbital coupling. The same diagonal input with bounds `[-5,5]` and a shifted scalar onsite input both export correctly.

User reachability: [settings.md, Spectrum Range](upstream/kite/docs/documentation/settings.md#spectrum-range) encourages manual energy bounds; [tb_model.md, Adding lattice sites](upstream/kite/docs/documentation/tb_model.md#adding-lattice-sites) routes lattice input through pybinding. Its independently downloaded 0.9.5 [matrix overload](deps/pybinding-0.9.5/cppcore/src/Lattice.cpp#L38) accepts onsite matrices and stores their Hermitian form; [Python binding](deps/pybinding-0.9.5/cppmodule/src/Lattice.cpp#L9) exposes `energy` as the onsite matrix. Both my diagonal matrix and the CFG-002 Hermitian matrix satisfy that representation.

### CFG-002 — observed loss, but documented real mode

The claimed detection loop [kite.py:1187](upstream/kite/kite.py#L1187) inspects hopping families only. My Hermitian onsite matrix is `[[0.4,0.6i],[-0.6i,-0.4]]` eV with symmetric bounds `[-2,2]`, avoiding the shift bug. Default real mode exports `diag(0.4,-0.4)` and eigenvalues `[-0.4,0.4]`, whereas the supplied matrix has eigenvalues `±sqrt(0.52)` = `±0.7211102551`. With `is_complex=True`, the same unmodified exporter preserves the entire matrix and its eigenvalues.

However, [settings.md:85–88](upstream/kite/docs/documentation/settings.md#complex) reserves complex storage for `is_complex=True` and says `is_complex=False` should be used for real symmetric Hamiltonians. The [Configuration docstring](upstream/kite/kite.py#L775) also describes the flag as reflecting the Hamiltonian's type. Thus the triggering combination supplies a complex Hamiltonian to documented real mode. The automatic promotion for complex intersite hoppings is an inconsistent convenience; I found no documented promise of comprehensive automatic detection. I would describe this as possible input checking/hardening, not send it as a correctness bug in supported complex-mode use. No hardening change was made.

### TOOLS-001 — temperature supplied by file never updates beta

The [temperature read at line 180](upstream/kite/tools/Src/OptCond_1order/conductivity_optical.cpp#L180) leaves beta at its default, while [the CLI override](upstream/kite/tools/Src/OptCond_1order/conductivity_optical.cpp#L258) updates it. Both `calculate` and `calculateBlocks` consume beta.

My input is an array of disconnected two-site molecules with hopping 0.35 eV and sites separated by 0.8 nm, unit cell area 1 nm², energy scale 1 and shift 0. I supply exact normalized trace moments, 128 moments, 2049 Simpson points, Fermi energy 0 and broadening 0.12 eV. In the independent scalar reference, the two eigenvalues are ±0.35; Jackson spectral projectors and exact scalar resolvents enter the eigenbasis Kubo trace. That reference never uses KITE or the supplied Gamma matrix. Its finite Jackson expansion and integration grid match the requested numerical definition; the Green resolvent is evaluated exactly.

At omega = 0.7 eV, requested `kBT=0.3` eV:

| Calculation | Conductivity, e²/h |
|---|---:|
| Independent hot reference | `3.00226715596 + 0.253847984606i` |
| Unpatched, temperature from file | `5.73209 + 0.532202i` |
| Independent cold reference, kBT=0.001 | `5.73209055841 + 0.532202465137i` |
| Unpatched, explicit CLI `-T 0.3` | `3.00227 + 0.253848i` |

The hot-file and cold-file outputs are identical at all three frequencies, and both regular and block branches show the same result. Explicit CLI temperature agrees with the independent hot reference at saved-text precision. Both hot runs print `Temperature: 0.3`.

User reachability: [default usage](upstream/kite/docs/api/kite-tools.md#default-usage) says the file alone suffices; [calculation.md:66–67](upstream/kite/docs/documentation/calculation.md#parameters) defines the temperature of the Fermi distribution; [FAQ](upstream/kite/docs/faq.md#what-are-the-units-of-the-temperature) specifies energy units. This is not an intended default override, and is not a Kelvin-conversion claim.

The first NumPy reference contraction emitted BLAS floating-point warnings despite finite numbers. I replaced that contraction with [ordinary scalar math](repro/optical/scalar_reference.py), recomputed it, and reran the optical fixture without warnings. The initial log is retained as [console-initial.txt](repro/optical/console-initial.txt).

### TOOLS-002 — Green LDOS normalization

The cited [ldos.cpp:277](upstream/kite/tools/Src/Spectral/ldos.cpp#L277) accumulates minus the imaginary Green coefficient without division by pi. My exact input is a single local level at 0.25 eV, 256 moments, one thread and broadening eta = 0.15 eV. The independently correct density is the normalized Lorentzian `eta / (pi * ((E-0.25)^2 + eta^2))`.

| Energy, eV | Unpatched LDOS, 1/eV | Correct LDOS, 1/eV |
|---:|---:|---:|
| -0.25 | 0.550459 | 0.175216451110 |
| 0.25 | 6.66667 | 2.122065907892 |
| 0.50 | 1.76471 | 0.561723328560 |

The discrepancy is pi to saved-text precision, and not a finite-expansion effect. One thread isolates this claim from the excluded suspected Green indexing issue. User reachability: both [tools help](upstream/kite/tools/Src/Tools/parse_input.cpp#L112) and [API documentation](upstream/kite/docs/api/kite-tools.md#advanced-usage) explicitly offer `--LDOS -K green eta`; LDOS denotes a spectral density, and the default Jackson expression already includes its pi normalization.

### TOOLS-003 — a supported override loses a nonzero last moment

At [ldos.cpp:245](upstream/kite/tools/Src/Spectral/ldos.cpp#L245), each thread takes `floor(M/P)` terms with no remainder assignment. My stored input contains 32 exact moments for a zero-energy local level, `mu_n = cos(n*pi/2)`. Both lattice sizes and decomposition obey the documented TILE=8 constraint. I request seven moments with the documented `--LDOS -M 7` override.

At E=0, the complete finite Jackson sum is `1.007200458900` 1/eV. The unpatched result is `1.0072` on one thread and `0.983893` on two threads. The missing n=6 term is nonzero. A six-moment control produces `0.872882` on both thread counts. This tests the post-processor override, without asking the core to generate an odd number of moments.

User reachability: [tools API](upstream/kite/docs/api/kite-tools.md#advanced-usage) and help expose the override without a thread-divisibility restriction; the code checks that it does not exceed stored moments, but imposes no divisibility rule. [Decomposition documentation](upstream/kite/docs/documentation/settings.md#divisions) recommends multiple partitions. Reusing moments with different post-processing parameters is an explicit advertised workflow.

## Upstream status

Read-only `~/dev/.bin/gh api` requests fetched all 36 issue/PR entries, 28 PR records, 19 issue comments, one review comment, releases, branch heads and commit history. Snapshots and extracted text are in [evidence/](evidence/). There were no open issues or PRs at fetch time. Reviewed numerical/build PR diffs include #4, #5, #6, #9, and recent #35–37. None of the four surviving failure mechanisms appeared in the reviewed discussions or diffs. Issue #17 concerns server-dependent DOS/DC NaNs and supplies no matching optical/LDOS/exporter diagnosis; it is not evidence that these specific bugs are known.

Latest release is [1.1](https://github.com/quantum-kite/kite/releases/tag/1.1), published 2025-04-29, commit `078c23511bf63b6478af39f6a44d6e03828ec09a`. Master still points to the tested pin. `kite-develop` is `304d127c7f3e6d6fed530fd14dd2e90ebc9f5250`; `test-h` is `2b55aa088c09997ea7d5d956c0e1132a73f43218`. The affected three source files are byte-identical in all four versions, as recorded in [source-versions.json](evidence/source-versions.json); all core and tools source also has no diff from release 1.1 to the pin. `gh-pages` contains the generated documentation site. No current fix was found. This is a public-history check, not a claim about private reports or forks.

## Build limits and replay

KITEx failed two honest attempts: missing dependencies first, then Apple libc++ lacking `std::cyl_bessel_j` at `SimulationGaussianWavePacket.cpp:154`. The core was not modified or retried after that. KITE-tools built from the unchanged pin using locally built HDF5 1.14.6, Eigen 3.4.0, and the installed Homebrew libomp; an explicit libomp link was needed. Build/configuration logs, dependency hashes and Python versions are under [evidence/](evidence/).

Pybinding 0.9.5 installation failed, finally on its bundled Eigen's `Transpositions.h:387`. Therefore CFG-001/002 execute the actual unmodified `kite.config_system` with a minimal lattice data interface verified against pybinding's source and an empty import-only `pybinding` placeholder. No pybinding function runs, no bounds are mocked, and explicit energy bounds avoid pybinding's automatic scaling entirely. These are exporter verdicts, not end-to-end pybinding/KITEx verdicts. The three TOOLS claims use the real compiled executable and independent exact supplied moments. No core recursion or stochastic-moment calculation was tested; none of the five allegations was left entirely unexercised.

From this working directory, with the retained local venv and binary:

```sh
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/config/run.py --interface-only
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/ldos/run.py build/local/KITE-tools
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/optical/run.py build/local/KITE-tools
```

No hunter fix was applied or evaluated. No issues, PRs, comments, forks, messages or contacts were made. **NEW: no.** This is independent referee adjudication of existing software claims; no novel scientific result or predictive score is claimed. Predictive baselines and SBS do not apply.
