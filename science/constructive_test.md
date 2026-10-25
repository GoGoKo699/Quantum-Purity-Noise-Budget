# An explicit two-copy test

Independent measurements on pairs of noisy copies suffice whenever the total local-depolarization budget is logarithmic. This page gives the uniform purity gap, the exact error and copy-count bounds, and a circuit and classical decision rule that implement the test. Its asymptotic consequence is [Theorem T1](threshold.md#theorem-t1-polynomial-learnability-if-and-only-if-the-budget-is-logarithmic).

## Output purity has a uniform lower bound

Use the [source model](model.md): one fixed unknown pure input $\psi$ passes independently through

```math
\mathcal N_n=\bigotimes_{j=1}^{n}\mathcal D_{\eta_{n,j}},
\qquad 0\leq\eta_{n,j}\leq1.
```

Let $\rho=\mathcal N_n(\psi)$ and define

```math
A_n=\prod_{j=1}^{n}\frac{1+3\eta_{n,j}^{2}}{4},
\qquad
B_n=\sum_{j=1}^{n}(1-\eta_{n,j}^{2}).
```

For every pure input, including an arbitrarily entangled input,

```math
\boxed{\displaystyle
\operatorname{tr}(\rho^2)\geq A_n\geq4^{-B_n}.}
```

### Proof by the Pauli-error representation

A qubit depolarizing channel has the random-Pauli form

```math
\mathcal D_\eta(F)=\sum_{P\in\{I,X,Y,Z\}}q_P PFP^\dagger,
\qquad
q_I=\frac{1+3\eta}{4},
\qquad
q_X=q_Y=q_Z=\frac{1-\eta}{4}.
```

For an arbitrary qubit operator $F$, this identity follows directly from $\sum_{P\in\{X,Y,Z\}}PFP=2\operatorname{tr}(F)I-F$. Tensoring the channel representations gives probabilities $q_P$ on $n$-qubit Pauli strings. Since $\psi$ is pure,

```math
\begin{aligned}
\operatorname{tr}\!\left[\mathcal N_n(\psi)^2\right]
&=\sum_{P,Q}q_Pq_Q
\left|\langle\psi|P^\dagger Q|\psi\rangle\right|^2\\
&\geq\sum_Pq_P^2\\
&=\prod_{j=1}^{n}
\left[\left(\frac{1+3\eta_{n,j}}{4}\right)^2
+3\left(\frac{1-\eta_{n,j}}{4}\right)^2\right]\\
&=A_n.
\end{aligned}
```

The inequality keeps the diagonal terms $P=Q$, which are one, and drops nonnegative off-diagonal terms. It does not assume that different Pauli errors produce orthogonal states.

For $b\in[0,1]$, the convex function $f(b)=-\log(1-3b/4)$ lies below the chord joining its endpoint values. Therefore

```math
-\log(1-3b/4)\leq b\log4,
\qquad
1-3b/4\geq4^{-b}.
```

Apply this to $b_j=1-\eta_{n,j}^2$ and multiply over sites to obtain $A_n\geq4^{-B_n}$.

## Theorem U1: a uniform two-copy test

Fix $n\geq1$ and $0<\delta<1/2$. Suppose a known number $a_n$ satisfies

```math
2^{-n}<a_n\leq A_n,
\qquad
\Delta_n=a_n-2^{-n}>0.
```

On each of $t$ independent pairs of noisy source copies, measure the global SWAP observable and record $X_i\in\{-1,+1\}$. Declare the source pure if

```math
\frac1t\sum_{i=1}^{t}X_i
>\frac{a_n+2^{-n}}2,
```

and declare it maximally mixed otherwise. Both the false-positive probability under the maximally mixed source and the false-negative probability for every pure source are at most $\delta$ whenever

```math
t\geq\frac{8\log(1/\delta)}{\Delta_n^2}.
```

In particular, the number of noisy source copies is bounded by

```math
\boxed{\displaystyle
M_n(\delta)
\leq2\left\lceil
\frac{8\log(1/\delta)}{(a_n-2^{-n})^2}
\right\rceil.}
```

One may take $a_n=A_n$ when the channel parameters are known, or $a_n=4^{-\beta_n}$ when a known upper bound $\beta_n\geq B_n$ gives a positive gap. A nonpositive value of this sufficient gap does not itself prove impossibility; it means this particular guarantee is unavailable.

### Error proof and normalization

The SWAP identity gives

```math
\mathbb E[X_i]=\operatorname{tr}[\mathrm{SWAP}(\rho\otimes\rho)]
=\operatorname{tr}(\rho^2).
```

Under the null hypothesis the mean is $\mu_0=2^{-n}$, since $\mathcal N_n$ fixes the maximally mixed state. Under every pure-source alternative the mean is at least $a_n$. The threshold in U1 is separated from either possible mean by at least $\Delta_n/2$.

For independent variables in $[-1,1]$, either one-sided Hoeffding tail at distance $u$ is bounded by $\exp(-tu^2/2)$. Taking $u=\Delta_n/2$ bounds each of the two decision errors by

```math
\exp\!\left(-\frac{t\Delta_n^2}{8}\right).
```

The errors are bounded separately, as required by the model. There is no additional union-bound factor. The factor of two in the copy count counts the two source copies consumed by each SWAP measurement. Independence is used between pairs; outcomes at different sites within a pair may be correlated.

## A circuit with linear gate count per pair

The global swap of two $n$-qubit registers factors into commuting local swaps:

```math
\mathrm{SWAP}_{\mathrm{global}}
=\bigotimes_{j=1}^{n}\mathrm{SWAP}_{j,j'}.
```

Each local swap has eigenvalue $-1$ on the Bell singlet $|\Psi^-\rangle$ and $+1$ on the other three Bell states. A Bell measurement of the pair $(j,j')$ can be implemented by a CNOT from $j$ to $j'$, followed by a Hadamard on $j$, then computational-basis measurement of both qubits. The singlet yields outcome $11$ in this convention.

If the two observed bits at site $j$ are $u_j,v_j$, the local swap eigenvalue is $(-1)^{u_jv_j}$. The global bounded outcome is their classical product,

```math
X_i=\prod_{j=1}^{n}(-1)^{u_jv_j}
=(-1)^{\sum_{j=1}^{n}u_jv_j}.
```

This is a measurement of the global SWAP eigenvalue even though it also resolves additional commuting information. It uses one CNOT, one Hadamard, and two single-qubit measurements per site. The quantum resources are $2n$ source-register qubits and $O(n)$ elementary gates per pair, with no ancillary quantum register required. All coherent storage can be released after each pair.

The classical computation maintains the parity of the singlet outcomes for the current pair and an accumulated signed count over pairs. It does not reconstruct the state or retain every measurement record. For $t$ pairs, the count needs $O(\log t)$ bits. Total quantum gate complexity is $O(nt)$ under the ideal learner-operation model.

## A known budget is enough: exact dyadic implementation

The polynomial regime does not require high-precision access to every $\eta_{n,j}$. Suppose the learner is given a valid integer bound $L_n\geq B_n$ and that

```math
n\geq2L_n+2.
```

Set $a=4^{-L_n}=2^{-2L_n}$. Every pure-source output has purity at least $a$, while the null purity is at most $a/4$. The simple threshold $a/2$ then gives the following exact decision rule:

```math
\text{declare pure if}\qquad
2^{2L_n+1}\sum_{i=1}^{t}X_i>t.
```

The null mean is at least $a/4$ below this threshold and every alternative mean is at least $a/2$ above it. Hence

```math
\Pr_{\mathrm{null}}(\text{declare pure})
\leq e^{-ta^2/32},
\qquad
\sup_{\psi\ \mathrm{pure}}
\Pr_{\psi}(\text{declare mixed})
\leq e^{-ta^2/8}.
```

It is therefore enough to use

```math
t=\left\lceil32\,16^{L_n}\log(1/\delta)\right\rceil
```

pairs, or $2t$ noisy source copies. For an entirely integer specification at fixed $\delta$, one may instead choose the constant $K_\delta=\lceil32\log(1/\delta)\rceil$ and use $t=K_\delta16^{L_n}$.

If $L_n=O(\log n)$ and $\delta$ is fixed, the pair count is polynomial. The signed counter, the specified pair count, and the shifted integer used in the final comparison all have $O(\log n)$ bits. The threshold itself is dyadic; the procedure never needs to represent the exponentially small null mean $2^{-n}$ numerically. Rounding a known valid real budget bound upward to obtain $L_n$ changes the bound by less than one and preserves these conclusions.

## Relation to the collective lower bound

The test provides the constructive direction of T1. If $B_n\leq C\log n$ eventually, then $4^{-B_n}$ is inverse polynomial while $2^{-n}$ is exponentially small, yielding a polynomially resolvable gap. The [collective converse](channel_bound.md) proves that the same logarithmic budget condition is necessary even when the learner can store and measure all copies jointly. Pairwise measurements therefore suffice to attain this feasibility boundary; the results do not assert optimal constants or equal copy counts for pairwise and collective procedures.

These bounds concern independent source noise followed by noiseless learner operations. Additional noise in the Bell circuit or correlated noise between source copies requires a separate analysis. In particular, an implementation fault model is not charged implicitly to $B_n$.

The SWAP purity identity and its use for direct estimation of nonlinear state functionals are established tools; see [Ekert et al. (2002)](../references/RELATED_WORK.md#ekert2002). The Pauli representation and both inequalities above are proved explicitly here. The [related-work account](../references/RELATED_WORK.md) distinguishes these inherited tools from the total-budget criterion and from previous noisy two-copy learning bounds.
