# Retro

This repo has results on papers by five physicists I studied with, and bugs in one physics code. They went to the authors from November 5 to 7, 2026. AI agents did the work and I told them what to do. For each one, a separate referee agent on a different model did it again, and it did not get the code of the agent that found it. No journal has seen any of this, so all of it is a candidate.

## What we did

We picked a paper and asked one question about it. Can the printed bound be better, and can we certify it? Can this series be summed in closed form? Is there a proof, where the paper only has numbers? Do the printed examples follow from the definitions in the paper? Is the code right on small inputs?

Every run did the numbers in the paper first, if there was enough in it to do that again. For the Stampedes I seed, we got all 30 of the printed entries back, and then we tried something new. For the de Sitter bootstrap, the referee did the one-functional baseline in the paper, 6.43173726057, before it checked the new bound.

## A number alone is not new physics

One of the physicists I studied with said it plainly. A number alone is not worth much, if there is no new physics or new intuition behind it. I think he is right. Most of what we have is a better number, a closed form, a correction, or a bug in the code. The referees say the same thing. The new bound is a smaller number "within the authors' existing linear-programming approach". The seed "reformulates an existing exact determinant". The Coulomb reading has "no independently established new physical phenomenon".

## The physics came from a question

The closed form for the seed was just a formula. Then the author asked two questions: is it in Stampedes II, and what is this ODE? The answer to that is the part that reads like physics. It is the zero-angular-momentum radial Coulomb scattering equation in two dimensions, with L as the radius, B as the charge and the energy at π². So the phase has a Coulomb log in it, and if you increase B it delays every positive zero. It still explains a seed they already had. It is not a discovery. But a physicist can use it. The agent did not ask that question. A person did.

## It can be easy to beat a number on purpose

For one Padé approximation we certified an endpoint error below 0.000067%. The best one they printed is 31%. Then the referee tried the simplest thing. Equation (81) in the paper, with an ordinary [4/4] Padé, is about 14 times better than ours. Their point is that the paper used simple low-order curves on purpose. If you beat a number nobody tried to push, that tells you nothing about the physics.

## What was easy to check by hand

In a 2013 quantization paper, the symmetric and Duflo cubic examples it prints do not follow from the maps that are in it. 18 of 27 symmetric cubics agree, and 12 of 27 Duflo ones. Two methods that do not share code agree on all 108 cases. And you can check one of them by hand: the symmetric map gives X₁³ for the cube of X̂₁, and the paper prints X₁³ + X₁. So nobody has to trust the agent.

## What it says, and what they meant

The fused-link counterexample is one of those. It is true for the ordinary algebra: at ℓ = 3 and L = 6, the image has dimension 34 against 35 invariants. But with Lusztig's divided powers it goes away. So the agent can say what the paper says, and only the authors know which one they meant.

## In the code it is cheap to check

In KITE, the referee did 4 of 5 claimed bugs again on its own clone. It only had the claim to work from. The other one was intentional. The main one: it computes the finite-temperature optical conductivity at the default temperature, and it prints the one you asked for.

## What is easy and what is hard

Easy: to do a table again, to push a calculation along a pipeline that is already there, and to certify it. We did that with interval or exact arithmetic. The new bound is certified on all 61 closed intervals of the spectrum, with 640-bit Arb arithmetic. The seed is checked on 528 rational coefficients through L^32. The method that did that check shares no code with the one that found it.

Hard: to know if it is new. Almost every verdict has prior work in it. We found some of it late, and some of it we could not rule out. A thesis that prints the same 5.67049. A paper on adapted Padé expansions. A 2024 paper that recalls the Toda observation. Earlier work on divided powers. None of the verdicts says who was first, and none of them says this is new physics.

Hardest: to say what a result means. The referee can say it holds. It cannot say it matters.

FrontierPhysics did the same thing on 56 tasks that came from the work of physicists themselves. The best agent passed 27.4% of runs. In an expert audit of 168 runs, most of what went wrong was rigor (48%) and missing expert intuition (34%), and not physics knowledge.

## What we did not have

The inputs behind the numbers they print. The eight functionals behind 5.67049 are not public, so we have the one in the paper and not one of our own.

Something that says what they think is open. The seed was a good one to pick because Stampedes I asks for the closed resummation.

## What would make this easier

- Publish the code and the coefficients behind every bound and every table.
- Say which reading of a conjecture is the one you meant.
- Give every result to a physicist who will ask what it means.

## What is still open

Every verdict ends with the next thing to do. The ones I think matter:

- Get the eight functionals back, and do 5.67049 again on our own.
- Compare the seed with the finite-B Fredholm determinant, and put a bound on the cross-ratio corrections we left out of it.
- Do the fused-link image for all of L, with the root-of-unity convention fixed.
- Give a certified table of the error against the degree, for both Padé prescriptions, so that the comparison is fair.

And if any of this is useful to the people who wrote the papers. I don't know if it matters.

## What you should expect

Expect the calculation to be done and checked. Expect a closed form, a certificate, a corrected table or a bug. Do not expect new physics.

Lean does not help much here yet. Perturbative QFT and most of the bootstrap have no rigorous foundation to formalize. So the check is a second computation. It has to be independent of the first one, plus known limits and symmetry checks. The meaning is still on you.

The papers are public and the checks are cheap, so one person with agents can go through a lot of physics. Anthropic's numbers for each field put physics and astronomy at 40% of the time of a researcher that AI could take on. That is close to math at 43%. Theory groups have almost no lab steps in them, so I think they are closer to math. What is still slow is the part only people do: to decide if a result is interesting.

## Thanks

Everything here starts from someone else's paper or code. Thanks to all of them, and to the ones who replied and told me what they thought.

## References

Papers:

- Hogervorst, Penedones, Salehi Vaziri, Towards the non-perturbative cosmological bootstrap: https://arxiv.org/abs/2107.13871
- Olivucci, Vieira, Stampedes I: https://arxiv.org/abs/2111.12131
- Kostov, Petkova, Serban: https://arxiv.org/abs/1905.11467
- Alho, Calogero: https://arxiv.org/abs/1907.09970 ; Alho, Calogero, Liljenberg: https://arxiv.org/abs/2104.11131
- Alho, Hell, Uggla: https://arxiv.org/abs/1503.06994 ; Alho, Uggla: https://arxiv.org/abs/2407.14378
- Fonseca, Zinn-Justin: https://arxiv.org/abs/1212.4672
- Guedes, Oriti, Raasakka: https://arxiv.org/abs/1301.7750
- João, Anđelković, Covaci, Rappoport, Lopes, Ferreira, KITE, Royal Society Open Science 7:191809 (2020): https://doi.org/10.1098/rsos.191809

Prior work:

- Álvarez, Medina: https://arxiv.org/abs/2304.05650
- On the single-scaling Toda observation: https://arxiv.org/abs/2408.15331
- Blanchet, De Renzi, Murakami: https://arxiv.org/abs/1910.12427
- Kupriyanov, Vitale: https://arxiv.org/abs/1502.06544

The field:

- FrontierPhysics: https://arxiv.org/abs/2611.06910
- Anthropic Economics, AI for scientific discovery: how researchers use Claude, November 5, 2026: https://www.anthropic.com/research/how-researchers-use-claude
- Arb/FLINT, for the interval arithmetic behind the certificates.

This repo:

- The results, the claims, the derivations and the verdicts are all in README.md
