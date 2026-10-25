# Source access and the learning question

An unknown pure state and the maximally mixed state have very different purities. With clean copies, a learner can detect this difference by comparing pairs of examples. This project asks how much independent corruption those examples can undergo before even an unrestricted quantum learner loses polynomial sample complexity.

The distinction between source access and subsequent computation is essential. The noise acts before the learner receives a state. After reception, the learner has perfect quantum memory and arbitrary collective processing. The lower bound therefore constrains the information in the available examples, including their correlations across repeated preparations of the same unknown state.

## 1. Operational model

Let $`A`$ be a finite-dimensional Hilbert space of dimension $`d\ge 2`$, and let $`\mathcal N:\mathcal L(A)\to\mathcal L(B)`$ be a known completely positive trace-preserving map. The source satisfies one of two promises:

```math
H_0:\quad \rho=\tau:=I_A/d,
\qquad
H_1:\quad \rho=\psi:=|\psi\rangle\langle\psi|,
```

where the pure state in $`H_1`$ is arbitrary and unknown. It is fixed throughout the experiment. Each source call returns one copy of $`\mathcal N(\rho)`$, and different copies undergo independent instances of the channel. Conditional on the source state, the received state after $`m`$ calls is

```math
\mathcal N(\rho)^{\otimes m}.
```

The learner may use unlimited noiseless quantum memory, ancillary systems, adaptive operations, unrestricted classical computation and one joint measurement on all received systems. Every protocol with a fixed maximum of $`m`$ calls is included: a protocol that sometimes stops earlier can receive and ignore the remaining copies. Its final decision is a two-outcome POVM on the $`m`$-copy state.

The source interface supplies no classical description of $`\psi`$, purification, environment record, noise flag, coherent preparation oracle or inverse preparation oracle. The learner cannot encode a state before the acquisition channel acts. A channel may change the system dimension, and the reference output

```math
\sigma:=\mathcal N(\tau)
```

need not be maximally mixed or invertible. The [channel theorem](channel_bound.md) treats its support explicitly.

## 2. Minimax error and charged resources

Fix an error tolerance $`0\lt \delta\lt 1/2`$. A test is valid when both its null error and its error on every pure source are at most $`\delta`$. If $`E`$ is the effect corresponding to the decision “pure,” this means

```math
\mathrm{Tr}(E\sigma^{\otimes m})\le\delta,
\qquad
\inf_{\psi\ \mathrm{pure}}
\mathrm{Tr}\!\left[E\mathcal N(\psi)^{\otimes m}\right]
\ge 1-\delta.
```

Write $`M(\mathcal N,\delta)`$ for the minimum allowed maximum copy count. Set it to infinity if no finite count works. The bound concerns a maximum number of calls; expected stopping costs are a different convention and are not substituted silently.

Each supplied source copy is counted. The converse imposes no gate, memory or time limit after acquisition, so a processing improvement cannot evade it. The positive result separately accounts for its gates, memory and classical processing. Source preparation and noise calibration are not assigned an end-to-end runtime advantage: the source is an input interface, and the channel parameters or an adequate bound on them are known. No QRAM or free loading of a classical dataset is used.

For a sequence of $`n`$-qubit channels $`\mathcal N_n`$, write $`M_n(\delta)=M(\mathcal N_n,\delta)`$. “Polynomial-copy learnability” means that constants $`C,a,n_0`$ exist such that

```math
M_n(\delta)\le Cn^a\qquad\text{for every }n\ge n_0.
```

The error tolerance is fixed independently of $`n`$. The statement permits finitely many exceptional system sizes. It is a worst-case promise-testing statement, with the unknown pure state allowed to vary with $`n`$.

## 3. Local depolarization and total noise

The family admitting an exact polynomial-complexity criterion is

```math
\mathcal N_n=\bigotimes_{i=1}^{n}\mathcal D_{\eta_{n,i}},
\qquad
\mathcal D_\eta(X)=\eta X+(1-\eta)\mathrm{Tr}(X)I/2,
\qquad 0\le\eta_{n,i}\le1.
```

The rates can depend on both the site and the system size. A rate of one retains the site perfectly; a rate of zero replaces it completely. In this channel's replacement realization, $`\lambda_{n,i}=1-\eta_{n,i}`$ is the replacement probability. Define

```math
B_n:=\sum_{i=1}^{n}(1-\eta_{n,i}^{2}),
\qquad
\Lambda_n:=\sum_{i=1}^{n}(1-\eta_{n,i}).
```

Then $`\Lambda_n`$ is the expected number of replaced sites per source copy in that realization, and

```math
\Lambda_n\le B_n\le2\Lambda_n.
```

The parameter $`B_n`$ enters the channel proof naturally. The equivalent budget $`\Lambda_n`$ gives a direct operational interpretation. Neither counts gate errors in the learner's later computation.

## 4. Principal results and their proof homes

| Result | Statement | Authoritative account |
|---|---|---|
| **C1: collective channel converse** | A finite-copy collision-divergence bound in terms of the Petz round trip, valid for every finite-dimensional acquisition channel and unrestricted collective measurements | [Channel bound](channel_bound.md) |
| **U1: constructive test** | A uniform output-purity floor for every pure input and an explicit two-copy procedure with bounded error | [Constructive test](constructive_test.md) |
| **T1: logarithmic budget** | For heterogeneous local depolarization, polynomial-copy learnability holds exactly when $`B_n=O(\log n)`$, equivalently $`\Lambda_n=O(\log n)`$ | [Noise threshold](threshold.md) |

The central classification is

```math
M_n(\delta)\text{ is polynomially bounded in }n
\quad\Longleftrightarrow\quad
B_n=O(\log n).
```

The sufficient procedure also has polynomial gate complexity. A fixed nonzero local noise rate on a positive fraction of sites gives an exponential lower bound on copies. If $`B_n/\log n\to\infty`$, the required copy count is superpolynomial. If $`B_n`$ merely fails to be $`O(\log n)`$, possibly through oscillations, the conclusion is that no uniform polynomial bound exists.

For $`B_n=o(n)`$, the lower and upper bounds give exponential dependence on $`B_n`$ up to constants in the exponent. The exact exponent is not determined. For some extensive noise profiles the promises overlap exactly, giving infinite sample complexity; those profiles are not assigned a finite exponential upper bound.

## 5. Why averaging over pure states is legitimate

For the converse, choose the unknown pure state once from Haar measure and keep it fixed. The two Bayesian states are

```math
M_m:=\mathbb E_{\psi\sim\mathrm{Haar}}
       \mathcal N(\psi)^{\otimes m},
\qquad S_m:=\sigma^{\otimes m}.
```

A test that succeeds for every pure state also succeeds on this average. Their optimal discrimination therefore gives a minimax lower bound. The order of averaging and tensoring matters: independently drawing a new Haar state on every call would make the alternative equal to $`S_m`$ immediately, which is a different source model.

At one copy, $`M_1=\sigma`$ for every channel. Multi-copy information comes from the common unknown input. The proof controls how acquisition noise suppresses that information even when the learner measures all copies together. Haar averaging does not assert efficient physical preparation of a Haar state, and does not say that every pure input is equally difficult.

## 6. Reading route and attribution

Read the [channel converse](channel_bound.md), then the [constructive test](constructive_test.md) and their combination in the [threshold theorem](threshold.md). The [worked channels](examples.md) explain nonunital outputs, partial traces and exact failures of identifiability. The [interpretation](interpretation.md) brings together sample cost, available operations and the physical meaning of the budget.

The [related-work account](../references/RELATED_WORK.md) separates the contribution from the inherited Haar moment identity, Petz recovery, SWAP purity estimation, noisy two-copy learning bounds, collective bounds for entanglement-breaking noise, and partial-trace indistinguishability. The [verification guide](../verification/README.md) documents finite checks and their limits. Universal and asymptotic claims rest on the proofs, rather than on numerical enumeration.
