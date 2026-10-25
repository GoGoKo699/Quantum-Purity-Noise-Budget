# Exact examples and boundaries of the channel criterion

These examples compute the Petz composition in [Theorem C1](channel_bound.md#theorem-c1-finite-moment-and-copy-bounds), check its limiting cases, and distinguish a lower-bound criterion from a complete classification of the promise problem. The [operational model](model.md) fixes what the learner receives. The heterogeneous depolarizing result is treated separately in [the threshold theorem](threshold.md) and [the constructive test](constructive_test.md).

Throughout, $`\tau=I/d`$ is the input null state, $`\sigma=\mathcal N(\tau)`$ is its received state, and

```math
\mathcal K(X)
=\frac1d\mathcal N^\dagger
   \bigl(\sigma^{-1/2}\mathcal N(X)\sigma^{-1/2}\bigr).
```

Inverse powers are restricted to $`\mathrm{supp}\sigma`$. We use

```math
\kappa=\max_{\psi\ \mathrm{pure}}\|\mathcal K(\psi)\|_\infty,
\qquad
\gamma=\max_{\psi\ \mathrm{pure}}\mathrm{Tr}[\mathcal K(\psi)^2],
\qquad
c_\delta=2\log\bigl(1+4(1-2\delta)^2\bigr).
```

The input is one fixed unknown pure state under the alternative, with independent acquisition noise on repeated copies.

## Identity acquisition

For $`\mathcal N=\mathrm{id}`$ on dimension $`d`$, $`\sigma=I/d`$, $`\mathcal R=\mathrm{id}`$ and $`\mathcal K=\mathrm{id}`$. Therefore $`\kappa=\gamma=1`$.

Let $`\Pi_{\mathrm{sym}}^{(m)}`$ be the projector onto the symmetric subspace of $`(\mathbb C^d)^{\otimes m}`$, whose dimension is $`s_m=\binom{d+m-1}{m}`$. The [Haar moment formula](../references/RELATED_WORK.md#harrow2013) gives the exact averaged alternative and null:

```math
M_m=\frac{\Pi_{\mathrm{sym}}^{(m)}}{s_m},
\qquad
S_m=\frac{I}{d^m}.
```

It follows directly that

```math
1+\chi^2_{1/2}(M_m\|S_m)
=\frac{d^m}{s_m}
=\frac{m!}{\displaystyle\prod_{j=0}^{m-1}(1+j/d)}.
```

This is equality in the finite product bound of C1. The trace distance is also explicit:

```math
T(M_m,S_m)=1-\frac{s_m}{d^m}.
```

Indeed, $`M_m-S_m`$ is positive on the symmetric subspace and negative on its orthogonal complement. A symmetric-subspace measurement accepts every pure source with probability one and accepts the null with probability $`s_m/d^m`$. At $`m=4`$ and every $`d\ge2`$,

```math
\frac{s_4}{d^4}
=\frac{\prod_{j=0}^{3}(1+j/d)}{4!}
\le\frac5{16}\lt \frac13.
```

Thus four copies suffice for worst-case error at most $`1/3`$. The general lower bound is correspondingly constant in $`d`$. This is the noiseless collective-purity behavior; ordinary pairwise [SWAP purity measurements](../references/RELATED_WORK.md#ekert2002) also give a constant-copy test at fixed error.

## Replacement acquisition, including singular outputs

Let $`\mathcal N(X)=\mathrm{Tr}(X)\omega`$ for any fixed output state $`\omega`$, including a pure state. Then $`\sigma=\omega`$ and

```math
\mathcal N^\dagger(Y)=\mathrm{Tr}(\omega Y)I_A.
```

For an output operator $`Y=\Pi Y\Pi`$, where $`\Pi=\mathrm{supp}\omega`$, and an input operator $`X\in\mathcal L(A)`$, the support inverse gives

```math
\mathcal R(Y)
=\frac{\mathrm{Tr}(Y)}{d}I_A,
\qquad
\mathcal K(X)=\mathrm{Tr}(X)\frac{I_A}{d}.
```

Consequently $`\kappa=\gamma=1/d`$ and $`M_m=S_m=\omega^{\otimes m}`$ for every $`m`$. The collision quantity and trace distance both vanish. Every source produces the same received state, so no number of copies permits error below $`1/2`$ on both hypotheses.

In fact, $`\kappa=1/d`$ characterizes replacement channels in this setting. If $`\kappa=1/d`$, every density operator $`\mathcal K(\psi)`$ has largest eigenvalue at most $`1/d`$ and hence equals $`I_A/d`$. By linearity, $`\mathcal K(X)=0`$ for every traceless Hermitian $`X`$. The quadratic identity proved in C1 then gives

```math
0=\mathrm{Tr}[X\mathcal K(X)]
=\frac1d
 \|\sigma^{-1/4}\mathcal N(X)\sigma^{-1/4}\|_2^2.
```

All outputs are supported on $`\Pi`$, so $`\mathcal N(X)=0`$. Therefore $`\mathcal N(\rho)=\sigma`$ for every input state $`\rho`$. This argument remains valid when $`\sigma`$ is singular.

## Partial trace and the induced-state antecedent

Let the input be $`A=R\otimes E`$, with $`\dim R=r`$, $`\dim E=e`$ and $`d=re`$, and take $`\mathcal N=\mathrm{Tr}_E`$. The output null is $`\sigma=I_R/r`$. Since $`\mathcal N^\dagger(X)=X\otimes I_E`$,

```math
\mathcal R(X)=X\otimes\frac{I_E}{e},
\qquad
\mathcal K(\rho)=\rho_R\otimes\frac{I_E}{e},
\qquad
\rho_R=\mathrm{Tr}_E\rho.
```

For a pure input,

```math
\|\mathcal K(\psi)\|_\infty
=\frac{\|\psi_R\|_\infty}{e}\le\frac1e,
\qquad
\mathrm{Tr}[\mathcal K(\psi)^2]
=\frac{\mathrm{Tr}(\psi_R^2)}{e}\le\frac1e.
```

Both bounds are attained by a product pure state, so $`\kappa=\gamma=1/e`$. If $`r\ge2`$, C1 yields

```math
m(m-1)
\ge c_\delta\frac{re}{r-1}.
```

For fixed $`\delta\lt 1/2`$ this gives an $`\Omega(\sqrt e)`$ copy lower bound, uniformly for $`r\ge2`$. When $`r=1`$, the output is one-dimensional and the channel is a replacement channel.

The ensemble $`\mathrm{Tr}_E\psi`$ for Haar-random $`\psi`$ is the induced-state ensemble studied in [Bansal et al., Appendix D, Theorem D.1](../references/RELATED_WORK.md#bansal2025). That work already proves collective indistinguishability from the maximally mixed state using permutation moments. The calculation here recovers its $`\sqrt e`$ lower-bound scale as a special case of C1; it does not supersede that work's sharper small-copy trace-distance estimate.

This example also separates an average-case lower bound from identifiability for all pure inputs. If $`e\ge r`$, choose

```math
|\Psi\rangle
=\frac1{\sqrt r}\sum_{j=1}^r|j\rangle_R|j\rangle_E.
```

Then $`\mathrm{Tr}_E|\Psi\rangle\langle\Psi|=I_R/r=\sigma`$, making the worst-case promise problem impossible. If $`e\lt r`$, the reduced state of every pure input has rank at most $`e`$, so its purity is at least $`1/e\gt 1/r`$. A SWAP test therefore distinguishes the hypotheses using $`O((1/e-1/r)^{-2}\log(1/\delta))`$ received copies. This last upper bound is not asserted to be optimal.

## The exact two-copy moment under local depolarization

For $`n`$ qubits, let $`d=2^n`$, $`\mathcal N=\bigotimes_i\mathcal D_{\eta_i}`$ and $`\mathcal D_\eta(X)=\eta X+(1-\eta)\mathrm{Tr}(X)I/2`$. For a Hermitian Pauli string $`P`$, define $`\eta_P=\prod_{i:P_i\ne I}\eta_i`$, so $`\mathcal N(P)=\eta_PP`$. Let $`F`$ swap the two $`d`$-dimensional copies. Pauli orthogonality gives

```math
F=\frac1d\sum_P P\otimes P,
\qquad
\mathbb E_\psi[\psi^{\otimes2}]
=\frac{I+F}{d(d+1)}.
```

Apply $`\mathcal N`$ to both copies and subtract the null $`S_2=I/d^2`$. The identity terms cancel, leaving

```math
M_2-S_2
=\frac1{d^2(d+1)}
  \sum_{P\ne I}\eta_P^2 P\otimes P.
```

Because $`\mathrm{Tr}[(P\otimes P)(Q\otimes Q)]=d^2`$ when $`P=Q`$ and zero otherwise,

```math
\begin{aligned}
\chi^2_{1/2}(M_2\|S_2)
&=d^2\mathrm{Tr}[(M_2-S_2)^2] \\
&=\frac{\sum_{P\ne I}\eta_P^4}{(d+1)^2} \\
&=\frac{\prod_{i=1}^n(1+3\eta_i^4)-1}{(d+1)^2}.
\end{aligned}
```

For one qubit this is $`\eta^4/3`$, whereas the finite $`\kappa`$ bound in C1 gives $`\eta^2/3`$. The inequality is therefore generally strict. The [threshold theorem](threshold.md) determines the polynomial-copy boundary without asserting that C1 gives the optimal exponential rate.

### Maximal output purity for the same local channel

The parameter in C2 also has an exact product expression:

```math
\gamma_n=\max_{\psi\ \mathrm{pure}}
\mathrm{Tr}[\mathcal K(\psi)^2]
=\prod_{i=1}^n\frac{1+\eta_i^4}{2}.
```

Here $`\mathcal K=\bigotimes_i\mathcal D_{\eta_i^2}`$ is self-adjoint. Thus

```math
\mathrm{Tr}[\mathcal K(\psi)^2]
=\mathrm{Tr}\!\left[
\psi\left(\bigotimes_i\mathcal D_{\eta_i^4}\right)(\psi)
\right].
```

Expand the last product channel into retained subsets $`S`$, as in the proof of the exact coefficient in [T1](threshold.md#exact-channel-coefficient). A term has overlap

```math
\mathrm{Tr}\!\left[
\psi\left(\psi_S\otimes\frac{I_{\bar S}}{2^{n-|S|}}\right)
\right]
=2^{-(n-|S|)}\mathrm{Tr}(\psi_S^2)
\le2^{-(n-|S|)}.
```

Summing the positive coefficients gives the displayed product. Every product pure input attains it, because all of its reduced states are pure. This derives the parameter used in the finite C2 verification without assuming general multiplicativity of output purity. C2 can sharpen the lower-bound constants in the exponent; T1 needs only C1.

## Amplitude damping: a nonunital example

Consider one-qubit amplitude damping with damping probability $`g\in[0,1]`$, described by Kraus operators

```math
E_0=|0\rangle\langle0|+\sqrt{1-g}|1\rangle\langle1|,
\qquad
E_1=\sqrt g|0\rangle\langle1|,
\qquad
\mathcal N_g(X)=E_0XE_0^\dagger+E_1XE_1^\dagger.
```

These operators satisfy $`E_0^\dagger E_0+E_1^\dagger E_1=I`$. For a density matrix $`\rho`$,

```math
\rho=\begin{pmatrix}u&z\\z^*&v\end{pmatrix},
\qquad
\mathcal N_g(\rho)
=\begin{pmatrix}
u+gv&\sqrt{1-g}\,z\\
\sqrt{1-g}\,z^*&(1-g)v
\end{pmatrix},
\qquad
\sigma_g=\frac12\begin{pmatrix}1+g&0\\0&1-g\end{pmatrix}.
```

For $`g\lt 1`$ the reference output is full rank. The adjoint acts as

```math
\mathcal N_g^\dagger
  \left(\begin{pmatrix}a&b\\c&h\end{pmatrix}\right)
=\begin{pmatrix}
a&\sqrt{1-g}\,b\\
\sqrt{1-g}\,c&ga+(1-g)h
\end{pmatrix}.
```

Insert this expression and $`\sigma_g^{-1/2}`$ into the Petz formula, including its factor $`1/2`$. With

```math
q=\sqrt{\frac{1-g}{1+g}},
```

the result is

```math
\mathcal K_g(\rho)
=\begin{pmatrix}
\dfrac{u+gv}{1+g}&qz\\
qz^*&\dfrac{gu+v}{1+g}
\end{pmatrix}.
```

Equivalently, writing $`X,Y,Z`$ for the Pauli operators,

```math
\mathcal K_g\left(\frac{I+xX+yY+zZ}{2}\right)
=\frac{I+qxX+qyY+q^2zZ}{2}.
```

Although $`\mathcal N_g`$ is nonunital when $`g\gt 0`$, its Petz composition is unital, as required by C1. For a pure input, $`x^2+y^2+z^2=1`$, and the squared length of the output Bloch vector is

```math
q^2(x^2+y^2)+q^4z^2
=q^2-q^2(1-q^2)z^2\le q^2.
```

Equatorial pure states attain this bound. Therefore

```math
\kappa(\mathcal N_g)=\frac{1+q}{2},
\qquad
\gamma(\mathcal N_g)=\frac{1+q^2}{2},
\qquad
m(m-1)\ge\frac{2c_\delta}{q}\qquad(0\le g\lt 1).
```

This is a valid lower bound, without a claim that its dependence on $`g`$ is optimal. The exact two-copy collision quantity follows because $`\mathcal K_g`$ has eigenvalues $`1,q,q,q^2`$ in the normalized Pauli operator basis:

```math
\chi^2_{1/2}(M_2\|\sigma_g^{\otimes2})
=\frac{2q^2+q^4}{9}.
```

At $`g=0`$, $`q=1`$, giving the identity channel and collision quantity $`1/3`$ for $`d=2,m=2`$. At $`g=1`$, the correct calculation uses the support inverse: $`\mathcal N_1(X)=\mathrm{Tr}(X)|0\rangle\langle0|`$, so $`\mathcal K_1(X)=\mathrm{Tr}(X)I/2`$. Thus $`\kappa=\gamma=1/2`$ and every collision quantity vanishes. The formula for $`\mathcal K_g`$ has this same limit; the singular endpoint does not require a full-space inverse.

## Full dephasing: the criterion is not complete

Let $`\mathcal N=\Delta`$ be complete dephasing in a fixed orthonormal basis of dimension $`d\ge2`$:

```math
\Delta(X)=\sum_{j=1}^d
   |j\rangle\langle j|X|j\rangle\langle j|.
```

It is unital, self-adjoint and idempotent, so $`\sigma=I/d`$ and $`\mathcal K=\Delta`$. A basis state is unchanged, which gives $`\kappa=\gamma=1`$.

Nevertheless, the pure state

```math
|+_d\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j\rangle
```

satisfies $`\Delta(|+_d\rangle\langle+_d|)=I/d`$. The two hypotheses therefore have an identical received state for this input, and no protocol can attain worst-case error below $`1/2`$.

The large value $`\kappa=1`$ records that some pure inputs survive dephasing. It does not imply that every pure input is separated from the null. C1 and C2 remain valid, but neither supplies a necessary and sufficient classification for arbitrary channels. The exact classification proved in this repository is the [polynomial-copy threshold for heterogeneous local depolarization](threshold.md).

## Encoding before acquisition changes the hypotheses

Let $`V:\mathbb C^D\to\mathbb C^d`$ be an isometric source encoding and let $`\mathcal E(X)=VXV^\dagger`$. An encoded version of the promise supplies either $`\mathcal E(I_D/D)`$ or $`\mathcal E(\psi)`$ before the physical noise channel $`\mathcal N`$. If a decoder $`\mathcal Q`$ exactly corrects this code, then

```math
\mathcal Q\circ\mathcal N\circ\mathcal E
=\mathrm{id}_D.
```

Decoding reduces the received promise to the identity example on the logical system. The effective logical channel has $`\kappa=1`$, and a fixed-error purity test uses a constant number of encoded source preparations. This statement is conditional on the supplied encoding and recovery; their preparation and implementation are additional physical resources.

There is no contradiction with a lower bound for $`\mathcal N`$ on all physical input states. The encoded null is $`VI_DV^\dagger/D`$, which generally differs from $`I_d/d`$, and the pure alternatives occupy the code subspace. The Haar prior over the full physical input space is no longer a prior over the promised inputs.

By contrast, any encoding, error correction or mitigation applied only **after** the learner receives $`\mathcal N(\rho)`$ is already an allowed downstream quantum operation in C1. Its inclusion cannot increase the trace distance of the received hypotheses. The distinction is the access model, not a restriction on the learner's subsequent computational power; see the corresponding [mitigation and access comparisons](../references/RELATED_WORK.md#takagi2023).
