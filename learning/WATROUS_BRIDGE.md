# From Watrous to purity testing with noisy examples

An unknown pure state can be recognized without learning its direction: compare two independently prepared copies. The comparison is a measurement of the SWAP operator, whose mean is the state's purity. This project asks what remains possible when each copy is corrupted **before** the learner receives it, even though the learner can subsequently store and process every received copy perfectly.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. It supplies the language of states, channels and measurements, the operational meaning of trace distance, and the symmetric-subspace identity for random pure states. This bridge connects those ingredients to the channel-dependent lower bound and the logarithmic noise-budget criterion proved in the repository.

The argument has two directions. A lower bound must control every permitted measurement, so it studies the distinguishability of the entire received state. An upper bound must exhibit an actual procedure, so it identifies a purity gap and measures it. Their meeting point is the same total local-noise budget.

<a id="source-route"></a>
## 1. The selected source and the route through it

Use the [author's book page](https://jhwatrous.github.io/books-and-courses.html) or the [publisher's record](https://doi.org/10.1017/9781316848142). The links below point to the author-hosted chapters; copies of the book are not included in this repository. Section, theorem and equation numbers were checked in those PDFs.

| Project ingredient | Verified Watrous location | Use here |
|---|---|---|
| Eigenvalues, adjoints and matrix norms | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), Section 1.1.3; Schatten duality and Hölder in Eqs. (1.173)–(1.174) | Interpret purity, operator norm and trace norm |
| States and subsystems | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Sections 2.1.2–2.1.3 | Separate a pure joint state from a mixed reduced state |
| Channels and measurements | Chapter 2, Section 2.2.1, Definition 2.13; Section 2.3.1 | Specify acquisition and the final decision |
| Optimal binary discrimination | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Section 3.1.1, Theorem 3.4 | Turn trace distance into an error bound |
| The symmetric subspace | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), Section 7.1.1, Proposition 7.1, Eq. (7.8); Proposition 7.2 and Eq. (7.16) | Express its projector as a permutation average and count its dimension |
| Uniform pure-state moments | Chapter 7, Section 7.2.1, Lemma 7.24, Eq. (7.159) | Replace a Haar integral by a finite permutation sum |

The support-normalized Petz round trip, weighted collision calculation, cycle bounds, and noise-budget comparison are supplied below as the **project-specific bridge**. They are not asserted to be theorems from Watrous. The [research references](../references/RELATED_WORK.md) retain attribution for Petz recovery, SWAP estimation and related testing results without introducing another educational anchor.

<a id="notation"></a>
## 2. A notation dictionary

The main translation is between a unit vector and its density operator. A vector describes amplitudes; the rank-one projector is the operator to which a channel is applied.

| In Watrous | In this project | Meaning |
|---|---|---|
| Complex Euclidean spaces $`\mathcal X,\mathcal Y`$ | Input $`A`$ and output $`B`$ | The spaces on which the systems are described |
| A unit vector $`u`$ and the operator $`uu^*`$ | $`\vert \psi\rangle`$ and $`\psi=\vert \psi\rangle\langle\psi\vert `$ | Two representations of a pure state |
| $`X^*`$ | $`X^\dagger`$ | Conjugate transpose; the corresponding star/dagger on a map denotes its Hilbert–Schmidt adjoint |
| $`\mathrm D(\mathcal X)`$ | Density operators $`\rho`$ on $`A`$ | Positive operators with trace one |
| A channel $`\Phi\in\mathrm C(\mathcal X,\mathcal Y)`$ | $`\mathcal N:\mathcal L(A)\to\mathcal L(B)`$ | The acquisition channel |
| $`\mathbb 1_{\mathcal X}`$ | $`I_A`$ | Identity operator; distinct from the identity channel |
| Uniform spherical measure $`\mu`$ on $`\mathrm S(\mathcal X)`$ | Haar-distributed projector $`\psi`$ | Sample $`u`$ from the sphere, then form $`uu^\dagger`$; its global phase disappears |
| Haar measure denoted $`\eta`$ in Chapter 7 | Local retention parameters $`\eta_j`$ | Unrelated uses of the same letter; $`\eta_j`$ here is a number in $`[0,1]`$ |
| Permutations $`W_\pi`$ of tensor factors | $`U_\pi`$ | Operators exchanging whole copies |
| Number of tensor factors often denoted $`n`$ | Copy count $`m`$ | Here $`n`$ instead counts physical qubits and $`d=2^n`$ |
| Generic state letters | $`\tau=I_A/d`$, $`\sigma=\mathcal N(\tau)`$ | The input null and its received output; $`\sigma`$ need not be maximally mixed |
| Permutation group on $`m`$ objects | $`S_m^{\mathrm{perm}}`$ | Kept distinct from the null state $`S_m=\sigma^{\otimes m}`$ |

For an operator $`X`$, $`\|X\|_1`$ is the sum of its singular values, $`\|X\|_2^2=\mathrm{Tr}(X^\dagger X)`$, and $`\|X\|_\infty`$ is its largest singular value. For positive $`X`$, the last quantity is its largest eigenvalue. All logarithms used in the project bounds are natural.

<a id="states-and-acquisition"></a>
## 3. From a state to the received experiment

A density operator has nonnegative eigenvalues $`p_i`$ summing to one. Its purity is $`\mathrm{Tr}\rho^2=\sum_i p_i^2`$. A pure state has one eigenvalue equal to one, whereas the maximally mixed state on dimension $`d`$ has all eigenvalues $`1/d`$. Their purities are therefore $`1`$ and $`1/d`$.

The source promises either $`\rho=\tau=I_A/d`$ or one fixed unknown pure state $`\rho=\psi`$. A completely positive trace-preserving map $`\mathcal N`$ acts on each copy before reception. Complete positivity permits the input to be entangled with other systems; trace preservation keeps probabilities normalized. For $`m`$ independent channel uses, the learner receives

```math
H_0:\quad \sigma^{\otimes m},
\qquad
H_1:\quad \mathcal N(\psi)^{\otimes m},
\qquad
\sigma=\mathcal N(I_A/d).
```

Purity in the promise refers to the source. Even under $`H_1`$, the received state can be mixed.

### A one-qubit example

Let $`\mathcal D_\eta(\rho)=\eta\rho+(1-\eta)I_2/2`$. For any pure qubit state, its noisy output has eigenvalues $`(1+\eta)/2`$ and $`(1-\eta)/2`$, regardless of the unknown direction. Consequently,

```math
\mathrm{Tr}[\mathcal D_\eta(\psi)^2]
=\frac{1+\eta^2}{2},
\qquad
\mathrm{Tr}[\mathcal D_\eta(I_2/2)^2]=\frac12.
```

The operator $`F`$ that exchanges the two copies has outcomes $`+1`$ and $`-1`$. In an eigenbasis of a state $`\omega`$,

```math
\mathrm{Tr}[F(\omega\otimes\omega)]
=\sum_{a,b}p_ap_b\langle a,b|b,a\rangle
=\sum_a p_a^2
=\mathrm{Tr}\omega^2.
```

Thus pairwise comparison sees a gap $`\eta^2/2`$ without identifying the pure state. At $`\eta=1`$ the gap is constant; at $`\eta=0`$ the two received hypotheses coincide. For many qubits, the difficulty is to obtain statements that remain valid for every entangled pure input.

### The same unknown state is repeated

To prove a lower bound, choose $`\psi`$ once at random and keep it fixed. Averaging the resulting experiment gives

```math
M_m=\mathbb E_\psi[\mathcal N(\psi)^{\otimes m}],
\qquad
S_m=\sigma^{\otimes m}.
```

The conditional copies are independent given $`\psi`$, but the averaged state $`M_m`$ retains information about their common unknown input. Moving the expectation inside each tensor factor would describe a different source:

```math
\mathbb E_\psi[\mathcal N(\psi)^{\otimes m}]
\quad\text{versus}\quad
\bigl(\mathbb E_\psi\mathcal N(\psi)\bigr)^{\otimes m}.
```

At one copy the two agree. The point of the lower bound is to control the information that emerges at higher copy counts.

<a id="discrimination"></a>
## 4. Why an arbitrary learner is a discrimination problem

A binary measurement is specified by an effect $`E`$ with $`0\le E\le I`$; the probability of declaring “pure” on a received state $`\omega`$ is $`\mathrm{Tr}(E\omega)`$. A valid test at error tolerance $`\delta<1/2`$ satisfies

```math
\mathrm{Tr}(ES_m)\le\delta,
\qquad
\mathrm{Tr}[E\mathcal N(\psi)^{\otimes m}]
\ge1-\delta
\quad\text{for every pure }\psi.
```

Watrous's Theorem 3.4 supplies the optimal equal-prior success probability for two known states:

```math
p_{\mathrm{succ}}^{\mathrm{opt}}
=\frac12+\frac14\|M_m-S_m\|_1
=\frac{1+T(M_m,S_m)}2,
\qquad
T(M,S)=\frac12\|M-S\|_1.
```

The project-specific step is the passage from the worst-case requirement to this binary problem. Averaging a test's pure-input error over any prior cannot make it exceed the worst-case error. A uniformly successful test must therefore satisfy

```math
T(M_m,S_m)\ge1-2\delta.
```

An upper bound on the trace distance consequently becomes a lower bound on the required number of copies.

This covers an unrestricted learner. If a downstream channel $`\mathcal A`$ is followed by a final effect $`F`$, its overall effect on the received systems is $`\mathcal A^\dagger(F)`$. The same description includes ancillas, stored quantum systems, adaptive measurements and classical control. A protocol with a deterministic maximum of $`m`$ calls can receive and ignore any unused copies. No restriction to pairwise measurements is made in this converse.

<a id="haar-moments"></a>
## 5. The symmetric-subspace identity in project notation

Here the book supplies the central exact identity. Lemma 7.24 expresses the uniform spherical moment as the normalized symmetric projector. Combining it with Proposition 7.1 and the dimension count gives

```math
\mathbb E_\psi[\psi^{\otimes m}]
=\frac{\Pi_{\mathrm{sym}}^{(m)}}
       {\binom{d+m-1}{m}}
=\frac{1}{(d)_m}
  \sum_{\pi\in S_m^{\mathrm{perm}}}U_\pi,
\qquad
(d)_m=d(d+1)\cdots(d+m-1).
```

The first equality uses $`\psi=uu^\dagger`$, so the sphere and pure-projector formulations are identical for this integrand. The factor $`m!`$ from the permutation average cancels the $`m!`$ in the binomial coefficient.

For one and two copies, this becomes

```math
\mathbb E_\psi\psi=\frac{I}{d},
\qquad
\mathbb E_\psi[\psi^{\otimes2}]
=\frac{I+F}{d(d+1)}.
```

The first identity explains why one copy cannot distinguish the Haar alternative from the null, for any channel. The SWAP term in the second identity exposes information that is present across copies. Applying the acquisition channel to this moment gives $`M_m=\mathcal N^{\otimes m}(\mathbb E_\psi\psi^{\otimes m})`$.

The remaining problem is quantitative: how much of this repeated-input information survives the channel? Expanding the full $`m`$-copy operator is unnecessary. The next steps convert its distinguishability into scalar moments controlled by one channel parameter.

<a id="petz-support"></a>
## 6. The missing normalization: support and the Petz round trip

This section supplies a local derivation beyond the selected textbook route. The [Petz construction](../references/RELATED_WORK.md#petz1988) is established recovery mathematics; its role here is to normalize a moment calculation. The argument does not require the learner to implement it or to recover the unknown state.

### Why a singular null output is harmless

Let $`\Pi`$ be the projector onto the support of $`\sigma=\mathcal N(I_A/d)`$. Every input state obeys $`\rho\le I_A`$, so positivity gives

```math
0\le\mathcal N(\rho)\le\mathcal N(I_A)=d\sigma.
```

All possible received states therefore live in the support of $`\sigma`$. Define $`\sigma^{-1/2}`$ by inverting its positive eigenvalues and setting it to zero on the orthogonal complement. This does not discard any possible observation. Moreover,

```math
\mathrm{Tr}[\Pi\mathcal N(\rho)]=1
\ \text{for all states }\rho
\quad\Longrightarrow\quad
\mathcal N^\dagger(\Pi)=I_A.
```

The adjoint is defined by the Hilbert–Schmidt pairing: for Hermitian operators, $`\mathrm{Tr}[Y\mathcal N(X)]=\mathrm{Tr}[\mathcal N^\dagger(Y)X]`$.

### Where the dimension factor comes from

The Petz map for reference input $`\tau=I_A/d`$ is

```math
\mathcal R(Y)
=\tau^{1/2}\mathcal N^\dagger
  \bigl(\sigma^{-1/2}Y\sigma^{-1/2}\bigr)\tau^{1/2}
=\frac1d\mathcal N^\dagger
  \bigl(\sigma^{-1/2}Y\sigma^{-1/2}\bigr).
```

The dimension here is the **input** dimension. The factor comes from two copies of $`\tau^{1/2}=I_A/\sqrt d`$; it is not a freely chosen normalization.

For $`Y=\Pi Y\Pi`$, cyclicity of trace and $`\mathcal N(I_A)=d\sigma`$ give

```math
\mathrm{Tr}\mathcal R(Y)
=\frac1d\mathrm{Tr}
 \bigl[\sigma^{-1/2}Y\sigma^{-1/2}\mathcal N(I_A)\bigr]
=\mathrm{Tr}Y.
```

Conjugation and the adjoint of a completely positive map are completely positive. Thus $`\mathcal R`$ is a channel on this output support. Its composition

```math
\mathcal K=\mathcal R\circ\mathcal N
```

is a channel on the input system and fixes the identity:

```math
\mathcal K(I_A)
=\mathcal N^\dagger(\Pi)=I_A.
```

In particular, $`\mathcal K(\phi)`$ is a normalized density operator for every pure $`\phi`$. This is the property needed for the moment bound. Define

```math
\kappa=\max_{\phi\ \mathrm{pure}}\|\mathcal K(\phi)\|_\infty,
\qquad
\frac1d\le\kappa\le1.
```

A small $`\kappa`$ bounds the concentration of every such round-trip output. A large $`\kappa`$ records that at least one direction survives; it does not establish that every pure source can be distinguished from the null.

For a square unital channel, $`\sigma=I_A/d`$ and the factors simplify to $`\mathcal K=\mathcal N^\dagger\mathcal N`$. For a general channel the weighting by $`\sigma`$ is essential.

### A singular-output check

Consider a device that replaces every input with $`|0\rangle\langle0|`$. Then $`\sigma=\Pi=|0\rangle\langle0|`$ and its support inverse is simply $`\Pi`$. On an output operator $`y\Pi`$,

```math
\mathcal R(y\Pi)=yI_A/d,
\qquad
\mathcal K(\rho)=I_A/d.
```

Hence $`\kappa=1/d`$. All received copies are identical under both hypotheses, exactly as the physical description requires. There is no divergent inverse and no recovery of the lost input.

The full support and channel-property audit is in [C1, proof step 1](../science/channel_bound.md#1-support-and-normalization).

<a id="weighted-collision"></a>
## 7. From trace distance to a channel-weighted moment

The trace norm answers the operational question, but the square of a weighted matrix is easier to average. For normalized states $`M,S`$ with $`\mathrm{supp}M\subseteq\mathrm{supp}S`$, define

```math
\chi^2_{1/2}(M\|S)
=\mathrm{Tr}
 \left[\left(S^{-1/4}MS^{-1/4}\right)^2\right]-1.
```

If $`M`$ and $`S`$ are diagonal in the same basis, this reduces to the classical expression $`\sum_i(M_i-S_i)^2/S_i`$ on the positive support of $`S`$. The weighting measures a deviation relative to the reference probabilities. In the noncommuting case, the order of the factors matters.

Set $`Z=S^{-1/4}(M-S)S^{-1/4}`$. Expanding the square gives $`\|Z\|_2^2=\chi^2_{1/2}(M\|S)`$. Since $`M-S=S^{1/4}ZS^{1/4}`$, the weighted Schatten-norm estimate is

```math
\|M-S\|_1
\le\|S^{1/4}\|_4^2\|Z\|_2
=\sqrt{\chi^2_{1/2}(M\|S)},
```

where $`\|S^{1/4}\|_4^4=\mathrm{Tr}S=1`$. This is the local weighted application of norm inequalities introduced in Watrous's Section 1.1.3. It yields

```math
T(M,S)\le\frac12\sqrt{\chi^2_{1/2}(M\|S)}.
```

The quarter powers are algebraic normalizations; they do not represent a physical filtering operation supplied to the learner.

### Why the Petz map appears in the square

Expanding a square of a Haar average introduces two independent integration variables, $`\psi`$ and $`\phi`$. These are variables in the proof, not independently resampled source states within an experiment. For one output factor,

```math
\mathrm{Tr}\!
 \left[\mathcal N(\psi)\sigma^{-1/2}
       \mathcal N(\phi)\sigma^{-1/2}\right]
=d\,\mathrm{Tr}[\psi\mathcal K(\phi)].
```

Tensor-product traces factor across the $`m`$ received copies, producing the exact identity

```math
1+\chi^2_{1/2}(M_m\|S_m)
=d^m\mathbb E_{\psi,\phi}
 \left[\mathrm{Tr}(\psi\mathcal K(\phi))\right]^m.
```

Fix $`\phi`$ temporarily and write $`\omega=\mathcal K(\phi)`$. The problem has become a scalar Haar moment of $`\mathrm{Tr}(\psi\omega)`$, where $`\omega`$ is a density operator with largest eigenvalue at most $`\kappa`$. This is the precise connection between the textbook moment formula and the acquisition channel.

The exact expansion and the trace-distance argument are given in [C1, proof steps 2 and 4](../science/channel_bound.md#proof-of-theorem-c1).

<a id="cycle-bound"></a>
## 8. How permutation cycles control all copy counts

Contract the Haar moment with $`\omega^{\otimes m}`$. A cycle of length $`\ell`$ in a permutation connects $`\ell`$ matrix indices into a trace $`\mathrm{Tr}\omega^\ell`$. Disjoint cycles give separate factors:

```math
d^m\mathbb E_\psi[\mathrm{Tr}(\psi\omega)]^m
=\frac{d^m}{(d)_m}
 \sum_{\pi\in S_m^{\mathrm{perm}}}
 \prod_{c\in\mathrm{cycles}(\pi)}
 \mathrm{Tr}\omega^{|c|}.
```

For three copies, the identity permutation contributes $`1`$, the three transpositions contribute $`3\mathrm{Tr}\omega^2`$, and the two three-cycles contribute $`2\mathrm{Tr}\omega^3`$. Thus the numerator is

```math
1+3\mathrm{Tr}\omega^2+2\mathrm{Tr}\omega^3
\le1+3\kappa+2\kappa^2
=(1+\kappa)(1+2\kappa).
```

The inequality follows eigenvalue by eigenvalue: if $`0\le p_i\le\kappa`$ and $`\sum_i p_i=1`$, then $`\sum_i p_i^\ell\le\kappa^{\ell-1}`$. A permutation with $`c(\pi)`$ cycles therefore contributes at most $`\kappa^{m-c(\pi)}`$.

The general sum has a simple recurrence. When a new object is added to a permutation of $`j`$ objects, it can form its own cycle, contributing a factor $`1`$, or be inserted after any of the $`j`$ existing objects, each contributing a factor $`\kappa`$. Consequently,

```math
\sum_{\pi\in S_m^{\mathrm{perm}}}\kappa^{m-c(\pi)}
=\prod_{j=0}^{m-1}(1+j\kappa).
```

Combining this with the Haar normalization and averaging over $`\phi`$ yields the central finite bound:

```math
1+\chi^2_{1/2}(M_m\|S_m)
\le\prod_{j=0}^{m-1}\frac{1+j\kappa}{1+j/d}
\le
\exp\!\left[\frac{m(m-1)}2\left(\kappa-\frac1d\right)\right].
```

The final step uses $`\log(1+x)\le x`$ on each ratio. Retaining the denominator is meaningful: when $`\kappa=1/d`$, the product is exactly one, recovering exact indistinguishability for a replacement channel.

Now combine this upper bound with the operational requirement from Section 4. A test with both errors at most $`\delta`$ needs $`\chi^2_{1/2}\ge4(1-2\delta)^2`$, hence

```math
m(m-1)\ge\frac{c_\delta}{\kappa-1/d},
\qquad
c_\delta=2\log\!\left[1+4(1-2\delta)^2\right],
```

when $`\kappa>1/d`$. At $`\delta=1/3`$, the constant is $`2\log(13/9)`$. This is [Theorem C1](../science/channel_bound.md#theorem-c1-finite-moment-and-copy-bounds), whose canonical proof states the quantifiers and support conditions together.

### The complementary purity parameter

[Theorem C2](../science/channel_bound.md#theorem-c2-a-bound-from-maximal-output-purity) keeps a different piece of spectral information:

```math
\gamma=\max_{\phi\ \mathrm{pure}}
       \mathrm{Tr}[\mathcal K(\phi)^2].
```

For nontrivial cycles, $`\mathrm{Tr}\omega^\ell\le\gamma^{\ell/2}`$ for $`\ell\ge2`$; fixed points still contribute one. Grouping permutations by the number of objects they move gives C2's derangement sum. This can sharpen the quantitative lower bound. C1 alone suffices for the polynomial-sample criterion, and its product preserves the exact replacement-channel limit.

<a id="local-noise-budget"></a>
## 9. From a channel bound to a logarithmic noise budget

For the family in [Theorem T1](../science/threshold.md#theorem-t1-polynomial-learnability-if-and-only-if-the-budget-is-logarithmic), an $`n`$-qubit copy passes through

```math
\mathcal N_n=\bigotimes_{j=1}^n\mathcal D_{\eta_j},
\qquad
\mathcal D_{\eta_j}(X)
=\eta_jX+(1-\eta_j)\mathrm{Tr}(X)I_2/2.
```

The parameters may depend on $`n`$ as well as on the site. Since these channels are unital and self-adjoint,

```math
\mathcal K_n=\mathcal N_n^\dagger\mathcal N_n
=\bigotimes_j\mathcal D_{\eta_j^2}.
```

### The coefficient is exact even for entangled inputs

Expand each factor as retaining or replacing its site. If a subset $`J`$ is retained, the output is the reduced state $`\phi_J`$ tensored with maximally mixed states on the replaced sites. Its operator norm is at most $`2^{-(n-|J|)}`$. Summing these bounds with their nonnegative replacement probabilities factorizes. A product pure input attains the result:

```math
\kappa_n
=\prod_{j=1}^n\frac{1+\eta_j^2}{2}.
```

This calculation uses positivity and the bound $`\|\phi_J\|_\infty\le1`$. It does not assume a general multiplicativity rule for channel norms; the full subset expansion is in [T1's coefficient calculation](../science/threshold.md#exact-channel-coefficient).

Define

```math
B_n=\sum_j(1-\eta_j^2),
\qquad
\Lambda_n=\sum_j(1-\eta_j),
\qquad
\Lambda_n\le B_n\le2\Lambda_n.
```

In the retention/replacement realization, $`\Lambda_n`$ is the expected number of replaced sites per source copy. It is an interpretation of the specified channel, not an additional noise record available to the learner.

Writing $`b_j=1-\eta_j^2`$ and using $`1-x\le e^{-x}`$ gives $`\kappa_n=\prod_j(1-b_j/2)\le e^{-B_n/2}`$. C1 then implies the necessary bound

```math
m\ge\sqrt{c_\delta}\,e^{B_n/4}.
```

Thus a polynomial bound on copies forces $`B_n=O(\log n)`$.

### A positive test needs a uniform output-purity gap

The upper bound needs a statement for **every** pure input. Express each depolarizing channel as a random Pauli error, with probabilities

```math
q_I=\frac{1+3\eta}{4},
\qquad
q_X=q_Y=q_Z=\frac{1-\eta}{4}.
```

Here $`I,X,Y,Z`$ are the identity and the three Pauli unitaries. For the product channel, write $`q_P`$ for the probability of a Pauli string $`P`$. Squaring the output state gives

```math
\mathrm{Tr}[\mathcal N_n(\psi)^2]
=\sum_{P,Q}q_Pq_Q
 |\langle\psi|P^\dagger Q|\psi\rangle|^2
\ge\sum_Pq_P^2
=A_n,
\qquad
A_n=\prod_j\frac{1+3\eta_j^2}{4}.
```

Only the $`P=Q`$ terms are retained in the inequality. The discarded terms are nonnegative; different errors need not produce orthogonal states.

The elementary inequality $`\log(1-3b/4)\ge-b\log4`$ for $`0\le b\le1`$ gives $`A_n\ge4^{-B_n}`$. The null output has purity $`2^{-n}`$. When

```math
\Delta_n=4^{-B_n}-2^{-n}>0,
```

independent SWAP measurements therefore separate the null mean from every alternative mean by at least $`\Delta_n`$. Thresholding the sample mean halfway between the two guarantees both errors at most $`\delta`$ using

```math
t\ge\frac{8\log(1/\delta)}{\Delta_n^2}
```

pairs, or $`2\lceil t\rceil`$ source copies. This follows from concentration of independent outcomes in $`[-1,1]`$. [Theorem U1](../science/constructive_test.md#theorem-u1-a-uniform-two-copy-test) provides the complete error calculation, a Bell-measurement implementation using $`O(n)`$ gates per pair, and an exact decision rule requiring only a known integer upper bound on $`B_n`$.

When $`B_n=O(\log n)`$, the term $`4^{-B_n}`$ is inverse polynomial, while $`2^{-n}`$ becomes smaller. The gap can therefore be resolved with polynomially many pairs. Combining this construction with the collective converse gives

```math
M_n(\delta)\text{ is eventually bounded by a polynomial in }n
\quad\Longleftrightarrow\quad
B_n=O(\log n)
\quad\Longleftrightarrow\quad
\Lambda_n=O(\log n).
```

The positive procedure uses pairs; the necessity statement already permits a joint measurement on all copies. This establishes a feasibility boundary, not equality of their optimal copy counts.

<a id="scope-and-examples"></a>
## 10. Examples that fix the meaning of the result

The following cases separate information loss, a weak lower bound, and a change in the available source.

| Case | What the calculation says | Interpretation |
|---|---|---|
| Identity acquisition | $`\kappa=1`$; clean SWAP comparisons have a constant purity gap | A constant number of copies suffices at fixed error |
| A replacement channel | $`\kappa=1/d`$ and every input produces the same $`\sigma`$ | The hypotheses are identical for every copy count |
| Exactly $`k`$ sites completely replaced, all others noiseless | $`B_n=k`$, even though those sites individually retain no information | $`k=O(\log n)`$ permits polynomial testing eventually; uniformly weak noise on every site is unnecessary |
| Full dephasing in a fixed basis | $`\kappa=1`$, but the pure uniform superposition maps to $`I/d`$ | A large $`\kappa`$ does not guarantee identifiability for all pure inputs |
| Source encoding before noise | The allowed pure states and generally the null state change | A protected source is a different promise problem |

For a concrete instance, fully replace one qubit and leave the others noiseless. Then $`B_n=1`$ and $`A_n=1/4`$. For $`n\ge3`$, the gap from the null purity is at least $`1/8`$, so a constant number of SWAP pairs suffices at fixed error. The size qualification matters: for two qubits, a Bell-state source with one qubit replaced produces exactly $`I_4/4`$, and testing is impossible. The eventual constant-copy statement concerns the family as the number of otherwise noiseless qubits grows.

Full dephasing is a particularly useful boundary. Basis states survive it, so the maximum defining $`\kappa`$ is large. Yet the particular pure state $`d^{-1/2}\sum_j|j\rangle`$ has a maximally mixed diagonal. One impossible pure input defeats a worst-case guarantee. C1 is a sufficient hardness criterion for general channels; the iff classification is proved for the product-depolarizing family.

A nonunital example also explains why the output null is kept as $`\sigma`$. One-qubit amplitude damping with probability $`g`$ sends $`I_2/2`$ to

```math
\sigma_g=\frac12
\begin{pmatrix}1+g&0\\0&1-g\end{pmatrix}.
```

Using $`I_2/2`$ as the received null would describe the wrong experiment. The [amplitude-damping example](../science/examples.md#amplitude-damping-a-nonunital-example) computes the correctly weighted map and its singular endpoint.

Independent acquisition is also substantive. A common unknown unitary applied to every copy preserves their joint purity comparison, whereas independent random unitaries can destroy it. The one-copy channel average alone does not specify the repeated-copy experiment when noise is correlated.

Finally, the asymptotic statements have precise limits. For $`B_n=o(n)`$, the proved bounds imply $`\log M_n(\delta)=\Theta_\delta(1+B_n)`$, without fixing the optimal exponential constant. Some extensive-noise profiles make the hypotheses overlap exactly. Failure of an eventual $`O(\log n)`$ bound can occur only on a subsequence; it does not by itself mean superpolynomial growth at every large size. These cases are addressed in [T1's qualifications](../science/threshold.md#consequences-and-asymptotic-qualifications).

<a id="reading-the-result"></a>
## 11. Returning to the canonical statements

The source-to-project connection is now explicit: Watrous turns random pure states into symmetric-subspace moments and trace distance into an operational error. The local bridge normalizes those moments against the received null, bounds the resulting permutation cycles through the channel, and compares that converse with a uniform purity-measurement procedure.

| Question | Canonical location |
|---|---|
| What does the learner receive, and what counts as success? | [Operational model](../science/model.md) |
| What is proved for an arbitrary acquisition channel? | [C1 and C2](../science/channel_bound.md) |
| How is the positive test implemented and counted? | [U1 and its circuit](../science/constructive_test.md) |
| Why is the total budget logarithmic? | [T1 and its proof](../science/threshold.md) |
| What happens for partial trace, amplitude damping or dephasing? | [Worked channels](../science/examples.md) |
| Which tools and nearby results are established prior work? | [Related work](../references/RELATED_WORK.md) |
| What do the numerical checks establish? | [Verification guide](../verification/README.md) |
| How do the understanding targets fit together? | [Thirty-milestone map](MILESTONES.md) |

The finite checks support implementation and normalization checks; the all-channel, all-copy and asymptotic conclusions rely on the proofs. The bridge is an explanation of their connections, while the science files remain the authoritative statements.
