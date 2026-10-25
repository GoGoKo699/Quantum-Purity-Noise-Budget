# A logarithmic noise budget characterizes polynomial learnability

For heterogeneous local depolarizing noise, the total noise budget determines whether an arbitrary unknown pure source can be distinguished from the maximally mixed source with polynomially many noisy copies. The converse allows joint measurements on all copies and unlimited noiseless quantum memory. The matching feasibility criterion is attained by independent measurements on pairs of copies.

This page states and proves the criterion. The operational definitions are in [the model](model.md), the general collective-measurement converse is [Theorem C1](channel_bound.md), and the explicit testing procedure is [Theorem U1](constructive_test.md).

## Model and noise parameters

For each integer $`n\geq1`$, let $`d_n=2^n`$ and consider the channel

```math
\mathcal N_n=\bigotimes_{j=1}^{n}\mathcal D_{\eta_{n,j}},
\qquad
\mathcal D_\eta(X)
=\eta X+(1-\eta)\mathrm{tr}(X)\frac{I_2}{2},
\qquad 0\leq\eta_{n,j}\leq1.
```

The source is promised to emit either $`I_{d_n}/d_n`$ or one fixed, unknown pure state $`\psi`$. Every copy passes through an independent use of $`\mathcal N_n`$ before it reaches the learner. Under the alternative, the output of $`m`$ uses is $`\mathcal N_n(\psi)^{\otimes m}`$: the pure state is fixed across copies, while the channel noise is independent across copies.

Fix an error tolerance $`0\lt \delta\lt 1/2`$. Write $`M_n(\delta)`$ for the minimum fixed maximum number of noisy source copies required by a test whose false-positive probability under the maximally mixed source and false-negative probability for every pure source are each at most $`\delta`$. All collective measurements, noiseless quantum memory, and noiseless processing are permitted. Set $`M_n(\delta)=\infty`$ when no such test exists.

Define the two total budgets

```math
B_n=\sum_{j=1}^{n}(1-\eta_{n,j}^{2}),
\qquad
\Lambda_n=\sum_{j=1}^{n}(1-\eta_{n,j}).
```

They obey

```math
\Lambda_n\leq B_n\leq2\Lambda_n,
```

because $`1-\eta^2=(1-\eta)(1+\eta)`$. In the replacement representation of the channel, each site is independently retained with probability $`\eta_{n,j}`$ and replaced by the maximally mixed qubit with probability $`1-\eta_{n,j}`$. Thus $`\Lambda_n`$ is the expected number of replaced sites in one source copy. These budgets charge the number and strength of noisy sites; they do not require a uniform lower bound on the individual $`\eta_{n,j}`$.

All logarithms below are natural. The channel sequence, or a sufficient known upper bound on its budget, is available to the testing procedure.

## Theorem T1: polynomial learnability if and only if the budget is logarithmic

For any sequence of channel parameters $`\{\eta_{n,j}:1\leq j\leq n\}_{n\geq1}`$ and any fixed $`0\lt \delta\lt 1/2`$, the following statements are equivalent:

1. There are finite constants $`C,k,n_0`$ such that $`M_n(\delta)\leq Cn^k`$ for every $`n\geq n_0`$.
2. $`B_n=O(\log n)`$.
3. $`\Lambda_n=O(\log n)`$.

When these conditions hold, a procedure using only independent two-copy measurements has polynomial source-copy complexity and polynomial gate complexity. A known integer upper bound $`L_n\geq B_n`$ with $`L_n=O(\log n)`$ is sufficient to implement it with $`O(\log n)`$-bit classical counters and threshold comparisons; exact knowledge of every channel parameter is unnecessary.

For finite $`n`$, define

```math
\kappa_n=\prod_{j=1}^{n}\frac{1+\eta_{n,j}^{2}}{2},
\qquad
c_\delta=2\log\!\left(1+4(1-2\delta)^2\right)\gt 0.
```

Every successful test using at most $`m`$ copies satisfies, when $`\kappa_n\gt 2^{-n}`$,

```math
m(m-1)\geq\frac{c_\delta}{\kappa_n-2^{-n}}.
```

In particular, with the inequalities understood in the extended real sense when $`M_n(\delta)=\infty`$,

```math
M_n(\delta)
\geq\max\!\left\{2,\sqrt{c_\delta}\,e^{B_n/4}\right\}.
```

For every $`n`$ satisfying $`n\geq2B_n+1`$, the constructive bound is

```math
M_n(\delta)
\leq64\log(1/\delta)\,16^{B_n}+2.
```

The finite-size upper bound is sufficient, not a necessary condition for a test to exist. A sharper directly usable bound, whenever its gap is positive, appears in [Theorem U1](constructive_test.md#theorem-u1-a-uniform-two-copy-test).

## Exact channel coefficient

The coefficient in Theorem C1 specializes for a bistochastic channel to

```math
\kappa(\mathcal N)
=\max_{\phi\ \mathrm{pure}}
\left\|\mathcal N^\dagger\mathcal N(\phi)\right\|_\infty.
```

Here $`\mathcal N^\dagger`$ is the Hilbert–Schmidt adjoint. Local depolarizing channels are self-adjoint and satisfy $`\mathcal D_\eta\mathcal D_\eta=\mathcal D_{\eta^2}`$. Consequently,

```math
\mathcal N_n^\dagger\mathcal N_n
=\bigotimes_{j=1}^{n}\mathcal D_{\eta_{n,j}^{2}}.
```

The following elementary argument computes the maximum even when $`\phi`$ is entangled across all sites. Suppress the index $`n`$, set $`s_j=\eta_j^2`$, and expand each factor as a mixture of retention and complete replacement. For a retained subset $`S\subseteq\{1,\ldots,n\}`$, the corresponding output on $`\phi`$ is

```math
\mathrm{tr}_{\bar S}(\phi)
\otimes\frac{I_{\bar S}}{2^{n-|S|}},
```

with the tensor factors placed at their original sites. Its operator norm is at most $`2^{-(n-|S|)}`$, since the reduced state has norm at most one. Convexity of the operator norm therefore gives

```math
\begin{aligned}
\left\|\bigotimes_{j=1}^{n}\mathcal D_{s_j}(\phi)\right\|_\infty
&\leq\sum_{S\subseteq[n]}
\left(\prod_{j\in S}s_j\right)
\left(\prod_{j\notin S}(1-s_j)\right)
2^{-(n-|S|)}\\
&=\prod_{j=1}^{n}\left(s_j+\frac{1-s_j}{2}\right)
=\prod_{j=1}^{n}\frac{1+s_j}{2}.
\end{aligned}
```

A product pure input attains this bound. On each site its output has largest eigenvalue $`(1+s_j)/2`$, and the largest eigenvalue of the product output is the product of these values. Hence

```math
\boxed{\displaystyle
\kappa(\mathcal N_n)=\kappa_n
=\prod_{j=1}^{n}\frac{1+\eta_{n,j}^{2}}{2}.}
```

This calculation does not assume a general multiplicativity theorem for maximum output norms.

## Proof of Theorem T1

### Necessity, including unrestricted collective measurements

Theorem C1 applies to the Haar average of the fixed-pure-source alternative,

```math
T_{n,m}=\mathbb E_{\psi\sim\mathrm{Haar}}
\mathcal N_n(\psi)^{\otimes m},
\qquad
\sigma_{n,m}=\left(\frac{I_{d_n}}{d_n}\right)^{\otimes m}.
```

A test that succeeds for every pure source also succeeds against this prior. The theorem gives

```math
1+\chi^2(T_{n,m}\|\sigma_{n,m})
\leq\exp\!\left[\binom m2(\kappa_n-2^{-n})\right].
```

The trace-distance requirement for two errors at most $`\delta`$, together with the trace-distance/chi-square inequality, yields the stated bound $`m(m-1)\geq c_\delta/(\kappa_n-2^{-n})`$. The full moment calculation and error normalization are proved in [Theorem C1](channel_bound.md). If $`\kappa_n=2^{-n}`$, all sites are completely depolarized and the two hypotheses coincide exactly, so $`M_n(\delta)=\infty`$.

Writing $`b_j=1-\eta_{n,j}^2\in[0,1]`$ and using $`1-x\leq e^{-x}`$ gives

```math
\kappa_n=\prod_j(1-b_j/2)\leq e^{-B_n/2}.
```

Thus every finite successful copy count obeys

```math
m^2\geq m(m-1)
\geq\frac{c_\delta}{\kappa_n-2^{-n}}
\geq\frac{c_\delta}{\kappa_n}
\geq c_\delta e^{B_n/2}.
```

At least two copies are necessary because the one-copy Haar average of the alternative equals the null state. Together these facts prove the lower bound in T1. In particular, $`M_n(\delta)\leq Cn^k`$ eventually implies

```math
B_n\leq4k\log n+4\log C-2\log c_\delta
```

eventually. This establishes necessity without any restriction on the learner's coherent memory or joint measurements.

### Sufficiency with independent pair measurements

[Theorem U1](constructive_test.md#theorem-u1-a-uniform-two-copy-test) proves that every pure input has noisy output purity at least

```math
A_n=\prod_{j=1}^{n}\frac{1+3\eta_{n,j}^{2}}{4}
\geq4^{-B_n}.
```

The maximally mixed source has output purity $`2^{-n}`$. Taking $`a_n=4^{-B_n}`$ in U1 therefore gives, whenever $`a_n\gt 2^{-n}`$,

```math
M_n(\delta)
\leq2\left\lceil
\frac{8\log(1/\delta)}{(4^{-B_n}-2^{-n})^2}
\right\rceil.
```

If $`n\geq2B_n+1`$, then $`2^{-n}\leq4^{-B_n}/2`$. Substitution yields the finite-size upper bound in T1.

Suppose now that $`B_n\leq C\log n`$ for all sufficiently large $`n`$. The condition $`n\geq2B_n+1`$ then holds eventually, and

```math
M_n(\delta)
\leq64\log(1/\delta)\,n^{C\log16}+2.
```

Each pair measurement uses $`O(n)`$ elementary gates, so its total gate count is polynomial as well. U1 also gives an implementation using a supplied integer upper bound on $`B_n`$ and exact dyadic threshold comparisons. Finally, $`\Lambda_n\leq B_n\leq2\Lambda_n`$ proves equivalence with the replacement budget criterion.

## Consequences and asymptotic qualifications

### Homogeneous noise

If every site has the same parameter $`\eta_n`$, then

```math
B_n=n(1-\eta_n^2),
\qquad
\Lambda_n=n(1-\eta_n).
```

Polynomial learnability is therefore equivalent to $`n(1-\eta_n)=O(\log n)`$. This equivalence holds over the whole parameter interval $`0\leq\eta_n\leq1`$. In particular, a fixed positive amount of depolarizing noise at every site gives an exponential lower bound on source-copy complexity even when all copies can be processed collectively.

### Bounded and subextensive budgets

If $`B_n\leq B_0\lt \infty`$, then, for every $`n\geq2B_0+1`$,

```math
2\leq M_n(\delta)
\leq64\log(1/\delta)\,16^{B_0}+2.
```

Thus a bounded total budget permits a constant number of source copies at fixed error, including when some individual sites are completely depolarized. The constant need not be small.

More generally, if $`B_n=o(n)`$, the finite-size upper bound eventually applies. The two explicit bounds in T1 then imply

```math
\log M_n(\delta)=\Theta_\delta(1+B_n).
```

The added one is necessary to state this uniformly when $`B_n`$ is bounded or zero. The result fixes the polynomial-versus-superpolynomial boundary; it does not identify the optimal constant in an exponential sample-complexity rate.

### Oscillating sequences

The $`O(\log n)`$ criterion is an eventual bound for every sufficiently large $`n`$. If $`B_n/\log n\to\infty`$, the converse gives $`M_n(\delta)=n^{\omega(1)}`$. If this ratio merely has unbounded limsup, the correct conclusion is that no single polynomial bounds $`M_n(\delta)`$ eventually: for each fixed polynomial degree, the lower bound exceeds that degree along an unbounded subsequence. The sequence may still have infinitely many sizes with a bounded budget and constant copy complexity. Failure of $`B_n=O(\log n)`$ alone does not imply superpolynomial growth at every sufficiently large size.

## Extensive noise can make the hypotheses identical

The subextensive upper bound must not be extended to all budgets. Let $`n`$ be even, completely depolarize the first $`n/2`$ sites, and leave the other $`n/2`$ sites noiseless. Use the pure input consisting of Bell pairs joining corresponding sites in the two halves:

```math
\psi=\bigotimes_{j=1}^{n/2}
|\Phi^+\rangle\langle\Phi^+|_{j,j+n/2}.
```

Replacing one member of each Bell pair by a maximally mixed qubit makes the entire output exactly $`I_{2^n}/2^n`$. The pure-source and maximally mixed-source hypotheses therefore overlap, and $`M_n(\delta)=\infty`$ for every $`\delta\lt 1/2`$. In this example,

```math
B_n=n/2,
\qquad A_n=2^{-n}.
```

The zero gap in U1 correctly prevents a finite upper bound. This example also shows why a universal assertion $`M_n=e^{\Theta(B_n)}`$ over all extensive budgets would be false.

## Scope and attribution

The lower bound concerns noise already applied to each source copy. It remains valid with perfect learner operations and unrestricted noiseless quantum memory. Access to the source before the noise, an encoding promise that restricts the admissible pure states, or a channel whose noise is correlated between copies changes the statistical experiment. For example, a common random unitary applied to every copy preserves pairwise SWAP expectations even when its one-copy average is maximally mixed. The independent-channel-use model is therefore substantive.

The construction uses established SWAP-based purity estimation; see [Ekert et al. (2002)](../references/RELATED_WORK.md#ekert2002). The Haar moment identity used in C1 is standard symmetric-subspace machinery; see [Harrow (2013)](../references/RELATED_WORK.md#harrow2013). The closest noisy-purity comparison is [Cotler, Gong, and Kannan](../references/RELATED_WORK.md#cgk2026), whose noisy two-copy-round model is discussed in the [related-work account](../references/RELATED_WORK.md). The proofs here separate the unrestricted collective converse, the exact local-channel coefficient, and the constructive total-budget criterion; these are distinct claims from the inherited measurement and moment identities.
