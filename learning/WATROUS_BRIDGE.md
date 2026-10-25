# Watrous bridge to Quantum Purity Noise Budget

**Single selected educational anchor:** John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), [author's book page](https://jhwatrous.github.io/books-and-courses.html). The research references in [RELATED_WORK](../references/RELATED_WORK.md) remain citations, not additional educational anchors.

## Focused reading route

- [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf): finite-dimensional states, measurements, channels, adjoints and trace norms. Map its density operators to the source promises in [model](../science/model.md); map its channels to acquisition noise N and its POVMs to the final binary test.
- [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Theorem 3.4: Holevo–Helstrom discrimination. Translate the book's optimal discrimination statement into the fixed-error minimax implication T(M_m,S_m) >= 1-2 delta used in [C1](../science/channel_bound.md).
- [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), Section 7.1.1, Proposition 7.1, and Section 7.2, Lemma 7.24: symmetric subspace and spherical/Haar moments. Read alongside the permutation-cycle proof of [C1](../science/channel_bound.md).

## Notation and conventions

Watrous's density operator and channel notation are used in finite dimensions. In this project, A is the source input space, B the received output, d=dim A, tau=I_A/d, N:A→B the acquisition CPTP channel, sigma=N(tau), and psi=|psi><psi| the fixed unknown pure source. The source emits either tau or psi. The same psi is used across all m independent channel applications. The two received Bayesian states are M_m=E_psi[N(psi)^{⊗m}] and S_m=sigma^{⊗m}. The trace distance is T(M,S)=||M-S||_1/2. Inverse powers of sigma act only on its support.

The bridge from the textbook to the contribution has three nontrivial additional steps; they are derived in the repository, **not attributed to Watrous**.

### Step 1: Petz round-trip normalization

For sigma=N(I/d), define R(X)=N†(sigma^{-1/2} X sigma^{-1/2})/d on the output support, and K=R∘N. The factor 1/d is necessary. The project proves that K is a unital trace-preserving completely positive map and self-adjoint in the Hilbert–Schmidt inner product. See [channel bound, support and normalization](../science/channel_bound.md#1-support-and-normalization). Petz recovery is an established mathematical ingredient; it is not an operation supplied to the learner.

### Step 2: From symmetric moments to a universal converse

Watrous's symmetric-subspace identity gives E_psi[psi^{⊗m}]=sum_{pi∈S_m} U_pi/(d)_m. Combining it with the Petz round trip gives the exact collision identity

```math
1+\chi^2_{1/2}(M_m\|S_m)
=d^m\mathbb E_{\psi,\phi}
\left[\operatorname{Tr}(\psi\mathcal K(\phi))\right]^m.
```

With kappa=max_pure ||K(phi)||∞, permutation-cycle counting bounds this by product_{j=0}^{m-1}(1+j kappa)/(1+j/d). The trace-distance bound and Helstrom theorem turn this into a lower bound for **every** collective learner. See [C1](../science/channel_bound.md#theorem-c1-finite-moment-and-copy-bounds).

### Step 3: Match the lower bound with a physical test

For N=⊗_i D_{eta_i}, K=⊗_i D_{eta_i²}. The project proves kappa=product_i(1+eta_i²)/2 and introduces B_n=sum_i(1-eta_i²). This yields a lower bound exponential in B_n. Independently, a Pauli-error collision argument gives tr[N(psi)²]≥product_i(1+3eta_i²)/4≥4^{-B_n} for every pure psi. Two-copy SWAP measurements distinguish this from the mixed null with polynomial resources exactly when B_n=O(log n). See [threshold](../science/threshold.md) and [constructive test](../science/constructive_test.md).

## Worked example: one fully replaced qubit

Take n qubits with eta_1=0 and eta_2=...=eta_n=1. Then B_n=1, regardless of n. The output of a pure source can be mixed, but the universal purity floor is 1/4. The null output purity is 2^{-n}. For sufficiently large n this is a constant detectable gap, so the two-copy test uses a constant number of pairs at fixed error. This example is not a claim that every extensive pattern is learnable: replacing half of maximally entangled pairs can make the two promises identical. See [examples](../science/examples.md) and [T1](../science/threshold.md).

## How to study

Use the [30-milestone map](MILESTONES.md) to move from operational objects to the global theorem. For each milestone, follow its one canonical science pointer and the relevant Watrous chapter. Specialist proofs remain in science/, while this bridge explains which textbook ingredient supports each derivation and which research-level steps must be supplied locally.
