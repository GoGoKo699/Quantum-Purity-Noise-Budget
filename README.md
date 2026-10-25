# Quantum Purity Noise Budget

**Independent noise at the source imposes a logarithmic budget for learning purity, even with unlimited quantum memory and collective measurements.**

An unknown $`n`$-qubit source is promised to produce either one fixed pure state or the maximally mixed state. Each copy passes through independent local depolarization before the learner receives it. The learner may then retain every copy and perform arbitrary noiseless quantum processing.

For site-dependent retention parameters $`0\le\eta_{n,i}\le1`$, define

```math
\begin{aligned}
\mathcal N_n&=\bigotimes_{i=1}^{n}\mathcal D_{\eta_{n,i}},\\
\mathcal D_\eta(X)&=\eta X+(1-\eta)\mathrm{Tr}(X)I/2,\\
B_n&=\sum_{i=1}^{n}(1-\eta_{n,i}^{2}).
\end{aligned}
```

At any fixed error tolerance $`0<\delta<1/2`$, the worst-case copy complexity satisfies

```math
\boxed{
\text{Polynomial-copy learnability}
\quad\Longleftrightarrow\quad
B_n=O(\log n).
}
```

Equivalently, the expected number of locally replaced sites per copy in the channel's replacement realization, $`\Lambda_n=\sum_i(1-\eta_{n,i})`$, must be $`O(\log n)`$, because $`\Lambda_n\le B_n\le2\Lambda_n`$. In the homogeneous case this is $`n(1-\eta_n)=O(\log n)`$.

## Results

| Result | Content | Proof |
|---|---|---|
| **Collective channel converse** | A finite-copy bound for every acquisition channel through its Petz round trip, allowing arbitrary joint measurements of all received copies | [Channel bound, C1](science/channel_bound.md) |
| **Constructive test** | A uniform output-purity floor for every pure input, resolved by two-copy SWAP measurements with an explicit error bound | [Constructive test, U1](science/constructive_test.md) |
| **Logarithmic noise threshold** | A necessary and sufficient criterion for polynomial copy complexity under heterogeneous local depolarization, with a polynomial-gate sufficient procedure | [Threshold, T1](science/threshold.md) |

The lower bound gives exponential sample cost for any fixed nonzero local noise rate on a positive fraction of sites. A logarithmic total budget remains learnable, even if a logarithmic number of sites are completely depolarized. The positive procedure uses two $`n`$-qubit registers and $`O(n)`$ gates per pair test.

For subextensive budgets $`B_n=o(n)`$, upper and lower bounds establish exponential dependence on $`B_n`$ up to constants in the exponent. Exact optimal exponents are not claimed. Some extensive profiles make a pure source and the mixed source exactly identical after noise, so their sample complexity is infinite.

## Read the science

Start with the [source model and precise claims](science/model.md). The [channel bound](science/channel_bound.md) proves the unrestricted converse; the [constructive test](science/constructive_test.md) establishes the achievable purity signal; the [threshold theorem](science/threshold.md) combines them. [Worked channels](science/examples.md) show nonunital outputs, partial traces and exact failures of identifiability. The [resource interpretation](science/interpretation.md) explains what unlimited downstream computation can and cannot change.

| To inspect | Read |
|---|---|
| Source access, error criterion and asymptotic quantifiers | [Operational model](science/model.md) |
| Haar moments, Petz normalization and the all-copy bound | [Channel converse](science/channel_bound.md) |
| Output-purity floor, concentration and Bell measurement implementation | [Constructive test](science/constructive_test.md) |
| Unequal noise rates, logarithmic threshold and extensive-noise limits | [Noise budget](science/threshold.md) |
| Identity, replacement, partial trace, amplitude damping and dephasing | [Examples](science/examples.md) |
| Memory, gates, source preparation and changed access models | [Interpretation](science/interpretation.md) |
| Inherited ingredients and closest existing results | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Finite reproduction and its limits | [Verification](verification/README.md) |

[The LLM reading guide](llms.txt) maps questions to their authoritative scientific files.

## Study the project

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source-to-project bridge](learning/WATROUS_BRIDGE.md) selects the relevant sections, translates the notation and explains how state discrimination and Haar moments lead into the channel converse and the constructive test. The bridge supplies the project-specific steps without requiring the whole book as a prerequisite.

The [30-milestone map](learning/MILESTONES.md) follows the scientific dependencies in two phases. **Twelve background milestones** build from states and channels to the clean collective testing problem. **Eighteen narrative milestones** connect the noise-normalization argument, the attainable purity signal and the logarithmic threshold, ending with the result's scope and physical interpretation. Each milestone states a central question, an understanding target, dependencies, a conceptual connection and precise source pointers.

## Relation to established results

The pure-versus-maximally-mixed learning problem, Haar moment identities, Petz recovery and SWAP purity estimation are established ingredients. Closest precedents include [noisy adaptive two-copy learning](references/RELATED_WORK.md#cgk2026), [arbitrary-memory bounds for entanglement-breaking noise](references/RELATED_WORK.md#bhalerao2026), and [collective indistinguishability of reduced Haar states](references/RELATED_WORK.md#bansal2025).

The result developed here combines an unrestricted collective converse for weak local acquisition noise with a matching heterogeneous polynomial-complexity threshold. The general-channel proof supplies a sufficient hardness criterion; it is not an if-and-only-if classification of arbitrary channels. The [source-by-source comparison](references/RELATED_WORK.md) identifies both the overlap and the distinct operational claim.

## Reproduce the finite checks

From the repository root, using Python 3.12:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite directly constructs finite Haar moments and noisy density matrices. It checks 48 local-depolarization moment cases, 84 pure-state purity-floor cases, 25 amplitude-damping cases and 5 model-boundary examples. It uses double-precision arithmetic with explicit tolerances. Universal and asymptotic statements are established by the written proofs.

## Scope

The same unknown pure state is repeated, and noise instances are independent across copies. The channel acts before learner access; perfect processing afterward is already allowed. Source encoding before noise, environment records, protected source families or correlated noise change the problem. Haar averaging is a worst-case proof device, with no efficient preparation or classical-data-loading claim. Noise parameters, or an adequate total-budget bound, are known to the test.

An exponential quantum sample lower bound does not determine the best quantum-to-classical sample-complexity ratio. The result concerns a specific quantum-data source promise and its acquisition cost.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
