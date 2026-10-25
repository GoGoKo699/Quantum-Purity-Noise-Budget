# A collective lower bound for an arbitrary acquisition channel

The channel bound controls how well **any measurement on all received copies** can distinguish a pure source from a maximally mixed source. Its parameter is the largest output eigenvalue of the channel composed with its Petz recovery map. This formulation includes nonunital channels and reference outputs with nonfull support.

The [operational model](model.md) specifies the source access and resources. The [depolarizing threshold](threshold.md) applies the bound to heterogeneous local noise. [Worked examples](examples.md) give exact channel calculations and show why the parameter is a sufficient hardness criterion, not a complete test of identifiability. Attribution and the comparison with prior results are in [related work](../references/RELATED_WORK.md).

## Setup and channel parameter

Let $`A`$ and $`B`$ be finite-dimensional systems, let $`d=\dim A\ge 2`$, and let $`\mathcal N:\mathcal L(A)\to\mathcal L(B)`$ be a quantum channel. The source is promised to be either $`\tau=I_A/d`$ or a fixed unknown pure state $`\psi=|\psi\rangle\langle\psi|`$. Each call supplies an independent copy of $`\mathcal N(\rho)`$ for the same source state $`\rho`$.

Define

```math
\sigma=\mathcal N(\tau),
\qquad
\Pi=\mathrm{supp}(\sigma).
```

Here $`\Pi`$ denotes the orthogonal projector onto the support. All inverse powers of $`\sigma`$ act on that support and vanish on its orthogonal complement. The Petz map for reference state $`\tau`$ is

```math
\mathcal R(X)
=\frac{1}{d}\mathcal N^\dagger
  \bigl(\sigma^{-1/2}X\sigma^{-1/2}\bigr),
\qquad
\mathcal K=\mathcal R\circ\mathcal N.
```

The normalization $`1/d`$ comes from the two factors of $`\tau^{1/2}`$ in the standard Petz recovery map; it is essential. The map $`\mathcal R`$ is used on $`\Pi\mathcal L(B)\Pi`$. On this algebra it is completely positive and trace preserving. The resulting map $`\mathcal K`$ on $`A`$ is a unital quantum channel and is self-adjoint for the Hilbert–Schmidt inner product. These properties are proved below; the recovery construction itself is standard [Petz machinery](../references/RELATED_WORK.md#petz1986), with its explicit map and support convention given in [Wilde, Section 12.3](../references/RELATED_WORK.md#wilde2017).

The parameter in the theorem is

```math
\kappa(\mathcal N)
=\max_{\phi\ \mathrm{pure}}
       \|\mathcal K(\phi)\|_\infty,
\qquad
\frac{1}{d}\le\kappa(\mathcal N)\le 1.
```

The norm is the largest eigenvalue for a positive operator. We abbreviate this parameter to $`\kappa`$. When $`A=B`$ and $`\mathcal N`$ is unital, $`\sigma=I_A/d`$ and the expression simplifies to $`\mathcal K=\mathcal N^\dagger\mathcal N`$.

For an integer $`m\ge 1`$, let

```math
M_m=\mathbb E_{\psi\sim\mathrm{Haar}}
          [\mathcal N(\psi)^{\otimes m}],
\qquad
S_m=\sigma^{\otimes m}.
```

The same pure state is used in every tensor factor before the Haar average is taken. For normalized states $`M,S`$ with $`\mathrm{supp}M\subseteq\mathrm{supp}S`$, define the sandwiched collision quantity

```math
\chi^2_{1/2}(M\|S)
=\mathrm{Tr}
   \left[\left(S^{-1/4}MS^{-1/4}\right)^2\right]-1.
```

Thus $`\log(1+\chi^2_{1/2})`$ is the sandwiched Rényi divergence of order two. We use $`T(M,S)=\tfrac12\|M-S\|_1`$ for trace distance, and all logarithms are natural.

## Theorem C1: finite moment and copy bounds

For every integer $`m\ge 1`$,

```math
1+\chi^2_{1/2}(M_m\|S_m)
\le
\prod_{j=0}^{m-1}\frac{1+j\kappa}{1+j/d}
\le
\exp\left[
  \frac{m(m-1)}{2}\left(\kappa-\frac1d\right)
\right].
```

Consequently,

```math
T(M_m,S_m)
\le
\frac12\sqrt{
  \prod_{j=0}^{m-1}\frac{1+j\kappa}{1+j/d}-1
}
\le
\frac12\sqrt{
  \exp\left[
    \frac{m(m-1)}{2}\left(\kappa-\frac1d\right)
  \right]-1
}.
```

Let $`0\lt \delta\lt 1/2`$. Suppose a protocol uses at most $`m`$ source copies, incorrectly declares the maximally mixed source to be pure with probability at most $`\delta`$, and incorrectly declares any pure source to be maximally mixed with probability at most $`\delta`$. The protocol may use unrestricted quantum memory, ancillas, adaptation and collective measurements after acquisition. If $`\kappa\gt 1/d`$, it must satisfy

```math
m(m-1)
\ge
\frac{c_\delta}{\kappa-1/d},
\qquad
c_\delta=2\log\bigl(1+4(1-2\delta)^2\bigr).
```

At $`\delta=1/3`$, $`c_\delta=2\log(13/9)`$. If $`\kappa=1/d`$, no such protocol exists for any finite number of copies. Equivalently, when $`\kappa\gt 1/d`$ the real-valued copy lower bound is

```math
m\ge
\frac{1+\sqrt{1+4c_\delta/(\kappa-1/d)}}{2}.
```

The Haar distribution is a prior for proving a worst-case lower bound. No efficient circuit for preparing Haar-distributed states is assumed or supplied.

## Proof of Theorem C1

### 1. Support and normalization

Every state $`\rho`$ satisfies $`0\le\rho\le I_A=d\tau`$. Positivity of $`\mathcal N`$ gives

```math
0\le\mathcal N(\rho)\le d\sigma.
```

Every channel output is therefore supported in $`\Pi`$. For every input state, $`\mathrm{Tr}[\Pi\mathcal N(\rho)]=1`$, which implies

```math
\mathcal N^\dagger(\Pi)=I_A.
```

Complete positivity of $`\mathcal R`$ follows from its expression as the composition of a conjugation and $`\mathcal N^\dagger`$. For any $`X=\Pi X\Pi`$,

```math
\begin{aligned}
\mathrm{Tr}\mathcal R(X)
&=\frac1d\mathrm{Tr}
   \bigl[\sigma^{-1/2}X\sigma^{-1/2}\mathcal N(I_A)\bigr] \\
&=\mathrm{Tr}(X\Pi)
=\mathrm{Tr}X,
\end{aligned}
```

because $`\mathcal N(I_A)=d\sigma`$. Hence $`\mathcal K`$ is completely positive and trace preserving. It is unital since

```math
\mathcal K(I_A)
=\mathcal N^\dagger(\Pi)=I_A.
```

The conjugation $`X\mapsto\sigma^{-1/2}X\sigma^{-1/2}`$ is self-adjoint, so $`\mathcal K`$ is self-adjoint. More explicitly, for every operator $`X`$,

```math
\mathrm{Tr}[X^\dagger\mathcal K(X)]
=\frac1d
 \bigl\|\sigma^{-1/4}\mathcal N(X)\sigma^{-1/4}\bigr\|_2^2
\ge 0.
```

Thus it is also positive semidefinite as a Hilbert–Schmidt superoperator. A trace-preserving extension of $`\mathcal R`$ outside $`\Pi`$ is unnecessary; any such extension has the same composition with $`\mathcal N`$.

### 2. Exact collision identity

For pure states $`\psi`$ and $`\phi`$, the definition of $`\mathcal K`$ gives

```math
\mathrm{Tr}
 \bigl[\mathcal N(\psi)\sigma^{-1/2}
       \mathcal N(\phi)\sigma^{-1/2}\bigr]
=d\mathrm{Tr}[\psi\mathcal K(\phi)].
```

Expanding the square in the collision quantity introduces two independent Haar integrals. Tensor products then factor, giving the exact identity

```math
1+\chi^2_{1/2}(M_m\|S_m)
=d^m\mathbb E_{\psi,\phi}
      \bigl[\mathrm{Tr}(\psi\mathcal K(\phi))\bigr]^m.
```

Fix $`\phi`$ and set $`\omega=\mathcal K(\phi)`$. It is a density operator with $`\|\omega\|_\infty\le\kappa`$.

### 3. Haar moments and permutation cycles

Write $`S_m^{\mathrm{perm}}`$ for the permutation group on $`m`$ objects, $`U_\pi`$ for the corresponding permutation of tensor factors, and $`(d)_m=d(d+1)\cdots(d+m-1)`$. The standard [Haar moment identity](../references/RELATED_WORK.md#harrow2013), also developed in [Mele's tutorial](../references/RELATED_WORK.md#mele2024), is

```math
\mathbb E_\psi[\psi^{\otimes m}]
=\frac1{(d)_m}\sum_{\pi\in S_m^{\mathrm{perm}}}U_\pi.
```

Taking its contraction with $`\omega^{\otimes m}`$ yields

```math
\mathbb E_\psi[\mathrm{Tr}(\psi\omega)]^m
=\frac1{(d)_m}
  \sum_{\pi\in S_m^{\mathrm{perm}}}
    \prod_{c\in\mathrm{cycles}(\pi)}
       \mathrm{Tr}\omega^{|c|}.
```

If $`\ell\ge1`$, positivity and unit trace give

```math
\mathrm{Tr}\omega^\ell
\le \kappa^{\ell-1}\mathrm{Tr}\omega
=\kappa^{\ell-1}.
```

A permutation with $`c(\pi)`$ cycles therefore contributes at most $`\kappa^{m-c(\pi)}`$. The cycle generating function is

```math
\sum_{\pi\in S_m^{\mathrm{perm}}}\kappa^{m-c(\pi)}
=\prod_{j=0}^{m-1}(1+j\kappa).
```

To see the identity directly, insert the last object into a permutation on $`m-1`$ objects. It either forms a new one-cycle, with weight factor $`1`$, or is inserted at one of $`m-1`$ positions in existing cycles, each with weight factor $`\kappa`$. This gives the product inductively.

Multiplying by $`d^m`$ and averaging over $`\phi`$ proves the finite product bound. The exponential bound follows from

```math
\log\frac{1+j\kappa}{1+j/d}
=\log\left(1+\frac{j(\kappa-1/d)}{1+j/d}\right)
\le j(\kappa-1/d)
```

and $`\sum_{j=0}^{m-1}j=m(m-1)/2`$.

### 4. Trace distance

Let $`Y=S^{-1/4}(M-S)S^{-1/4}`$. The support condition gives $`M-S=S^{1/4}YS^{1/4}`$. Schatten Hölder's inequality implies

```math
\|M-S\|_1
\le \|S^{1/4}\|_4^2\|Y\|_2
=\|Y\|_2,
```

since $`\mathrm{Tr}S=1`$. Expanding the square gives

```math
\begin{aligned}
\|Y\|_2^2
&=\mathrm{Tr}
  \left[\left(S^{-1/4}MS^{-1/4}\right)^2\right]
  -2\mathrm{Tr}M+\mathrm{Tr}S \\
&=\chi^2_{1/2}(M\|S).
\end{aligned}
```

Therefore $`T(M,S)\le\tfrac12\sqrt{\chi^2_{1/2}(M\|S)}`$, which proves the trace bounds.

### 5. From a Haar prior to worst-case error

Consider the equal-prior binary problem with received states $`M_m`$ and $`S_m`$. Any protocol with both worst-case errors at most $`\delta`$ has average error at most $`\delta`$ in this binary problem: average its pure-source error over the Haar distribution and keep the null error unchanged.

The [Helstrom formula](../references/RELATED_WORK.md#watrous2018) gives optimal equal-prior success $`(1+T(M_m,S_m))/2`$. It follows that

```math
T(M_m,S_m)\ge1-2\delta,
\qquad
\chi^2_{1/2}(M_m\|S_m)\ge4(1-2\delta)^2.
```

Combining these inequalities with the exponential moment bound proves the stated copy lower bound. If $`\kappa=1/d`$, the finite product equals one, so $`M_m=S_m`$ for every $`m`$ and the average error cannot fall below $`1/2`$.

Adaptive protocols with a deterministic maximum of $`m`$ calls are covered by the same argument. Unused source copies may be appended and ignored, and the entire downstream protocol is a quantum channel followed by a POVM on the $`m`$ supplied copies. Neither ancillas nor this processing increase trace distance. The theorem is stated for a fixed or deterministically bounded copy count; it does not assign a bound to an unbounded stopping rule measured only by its expectation.

## Theorem C2: a bound from maximal output purity

A second bound can improve constants in an exponential lower bound. Define

```math
\gamma=\max_{\phi\ \mathrm{pure}}
          \mathrm{Tr}[\mathcal K(\phi)^2].
```

Let $`D_k`$ be the number of derangements of $`k`$ objects, with $`D_0=1`$ and $`D_1=0`$. Then

```math
1+\chi^2_{1/2}(M_m\|S_m)
\le
\frac{\displaystyle\sum_{k=0}^m
       \binom mkD_k\gamma^{k/2}}
     {\displaystyle\prod_{j=0}^{m-1}(1+j/d)}.
```

To prove this, fix $`\omega=\mathcal K(\phi)`$. For every nontrivial cycle of length $`\ell\ge2`$, Schatten norm monotonicity gives

```math
\mathrm{Tr}\omega^\ell
\le(\mathrm{Tr}\omega^2)^{\ell/2}
\le\gamma^{\ell/2}.
```

A permutation moving exactly $`k`$ objects thus contributes at most $`\gamma^{k/2}`$, and there are $`\binom mkD_k`$ such permutations. Insert this bound in the same exact moment identity used for C1.

Since $`\binom mkD_k\le m^k`$, putting $`x=m\sqrt\gamma\lt 1`$ gives the convenient consequence

```math
\chi^2_{1/2}(M_m\|S_m)
\le\sum_{k=2}^m x^k
\le\frac{x^2}{1-x}.
```

In particular, let $`a=1-2\delta`$ and $`r_\delta=2a(\sqrt{1+a^2}-a)\in(0,1)`$. Every protocol in C1 obeys

```math
m\ge\frac{r_\delta}{\sqrt\gamma}.
```

For $`m\sqrt\gamma\lt 1`$ this follows by solving $`x^2/(1-x)\ge4a^2`$; for $`m\sqrt\gamma\ge1`$ it holds immediately. The finite product in C1 retains the exact replacement-channel limit, so C2 is a complementary bound rather than a uniform improvement.

## An exact second-moment identity

The same derivation also gives an equality useful for checking channels. Let $`\|\mathcal K\|_{\mathrm{HS}}^2=\sum_{a=0}^{d^2-1}\mathrm{Tr}[\mathcal K(F_a)^\dagger\mathcal K(F_a)]`$ for any Hilbert–Schmidt orthonormal operator basis $`\{F_a\}`$. Then

```math
\chi^2_{1/2}(M_2\|S_2)
=\frac{\|\mathcal K\|_{\mathrm{HS}}^2-1}{(d+1)^2}.
```

Indeed, the two permutations give

```math
1+\chi^2_{1/2}(M_2\|S_2)
=\frac{d}{d+1}
 \left(1+\mathbb E_\phi\mathrm{Tr}[\mathcal K(\phi)^2]\right).
```

Applying the second Haar moment once more and using $`\mathcal K(I_A)=I_A`$ yields

```math
\mathbb E_\phi\mathrm{Tr}[\mathcal K(\phi)^2]
=\frac{d+\|\mathcal K\|_{\mathrm{HS}}^2}{d(d+1)},
```

which proves the equality. The identity is illustrated by nonunital amplitude damping in [the examples](examples.md#amplitude-damping-a-nonunital-example).

## Exact scope of the conclusion

The theorem concerns learning the promise about the **source before acquisition noise**. It does not prohibit estimating purity of the received state by a SWAP measurement. It also does not establish equality between classical and quantum sample complexities.

The parameter $`\kappa`$ supplies a sufficient hardness criterion. A large value does not guarantee that every pure source remains distinguishable from the null. [Full dephasing](examples.md#full-dephasing-the-criterion-is-not-complete) gives an exact counterexample.

Independent applications of a fixed channel, the absence of a source-noise record, and the unrestricted pure-state input promise are used in the proof. Correlated noise across replicas, access to an environment or purification, or a source promised to lie in an encoded subspace define different received states or different hypotheses. Encoding and error correction performed after acquisition are already included among the permitted downstream operations; [encoding at the source](examples.md#encoding-before-acquisition-changes-the-hypotheses) changes the input model.
