# Related work and source attribution

This guide distinguishes the problem studied here from nearby access models and records the sources of the standard proof ingredients. Bibliographic records are in [references.bib](references.bib). Each citation key below is also a stable HTML anchor.

The problem is a promise on the state **before** a known acquisition channel: the input is either a fixed unknown pure state or the maximally mixed state. The learner receives independently corrupted copies and may perform a joint measurement on all of them. The channel acts before learner control; its environment is unavailable. See the [general channel bound](../science/channel_bound.md) for the precise model.

The relevant comparisons involve three separate choices: the promise on the original state, the acquisition channel, and the operations allowed after acquisition. A bound for restricted measurements, strong noise, or a different estimation task does not automatically settle all three choices made here.

## Closest comparisons

<a id="cgk2026"></a>
### Cotler, Gong and Kannan: noisy two-copy purity testing

**Jordan Cotler, Weiyuan Gong and Ishaan Kannan.** “Noisy quantum learning theory.” *Nature Communications* **17**, 6979 (2026). [Published article](https://doi.org/10.1038/s41467-026-73693-x); [open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13392386/); [arXiv:2512.10929v2](https://arxiv.org/html/2512.10929v2).

**Locator and assumptions.** Published Theorem 2.4; preprint Appendix E.1, Theorem E.2 and Eq. (31). The learner makes adaptive measurements on pairs of independently depolarized copies, retaining classical information between pairs. With their replacement-noise parameter $\lambda=1-\eta$, the lower bound is

$$
\Omega\!\left(\min\left\{2^{n/2},
\left[\frac{4}{1+3(1-\lambda)^4}\right]^n\right\}\right).
$$

**Relation.** This establishes the fragility of the two-copy advantage and motivates the acquisition-noise model. The theorem here permits a measurement on arbitrarily many copies at once. Its weaker numerical exponent should not be presented as an improvement of the bound above: the measurement classes differ. Their noise-resilient encoded-state example assumes additional structure of the source; it is compatible with a worst-case result for unrestricted pure inputs.

Theorem numbering above was checked in the January 14, 2026 preprint and the published main text; the preprint is explicitly identified where it supplies the formal statement.

<a id="bhalerao2026"></a>
### Bhalerao, Nuradha and Leditzky: arbitrary memory under entanglement-breaking noise

**Sujeet Bhalerao, Theshani Nuradha and Felix Leditzky.** “High quantum local differential privacy breaks entanglement.” [arXiv:2609.13418v1](https://arxiv.org/html/2609.13418v1), September 11, 2026.

**Locator and assumptions.** Section V, Theorems V.1 and V.4. The simulation theorem permits arbitrary quantum memory and binary output, but requires the acquisition channel to be entanglement breaking. For a tensor product of local entanglement-breaking channels, their purity theorem gives an $\Omega(2^{n/2})$ lower bound when success is required for every pure input.

**Relation.** Arbitrary-memory noisy-purity lower bounds therefore already exist. The distinction here is a bound that applies to weak local depolarization as well, without requiring entanglement breaking, and the resulting heterogeneous polynomial-sample criterion. For the convention $\mathcal D_\eta(\rho)=\eta\rho+(1-\eta)I/2$, the qubit entanglement-breaking condition is $\eta\le1/3$; see [Ruskai](#ruskai2003).

Their global high-privacy bounds, including Corollary V.6, impose another channel restriction and should not be conflated with arbitrary weak local noise. This source is a preprint, not a verified journal publication.

<a id="bansal2025"></a>
### Bansal et al.: partial trace and generalized Hilbert–Schmidt ensembles

**Nikhil Bansal, Wai-Keong Mok, Kishor Bharti, Dax Enshan Koh and Tobias Haug.** “Pseudorandom Density Matrices.” *PRX Quantum* **6**, 020322 (2025). [Published article](https://doi.org/10.1103/PRXQuantum.6.020322); [arXiv:2407.11607v2](https://arxiv.org/html/2407.11607v2).

**Locator and assumptions.** Theorem 1 and Appendix D, Theorem D.1. Tracing $k$ qubits out of a Haar state gives a mixed-state ensemble whose $t$-copy average is within $O(t^2/2^k)$ trace distance of the maximally mixed $t$-copy state. This is an information-theoretic statement allowing collective measurements; the computational assumptions used elsewhere for pseudorandom constructions are unnecessary for this theorem.

**Relation.** Partial trace is a direct antecedent and special case of the channel setting. The Petz round trip for $\operatorname{Tr}_E$ is $X\mapsto\operatorname{Tr}_E(X)\otimes I_E/d_E$, with maximum output eigenvalue $1/d_E$. The bound here recovers the $\sqrt{d_E}$ sample lower-bound scale; its generic trace-distance estimate does not improve their sharper small-$t$ estimate. Their permutation-cycle moment expansion is also prior mathematical machinery. The local-depolarizing threshold concerns a different channel family.

Appendix numbering was checked in v2, January 31, 2025.

<a id="duschenes2026"></a>
### Duschenes et al.: moments of noisy channel ensembles

**Matthew Duschenes, Diego García-Martín, Zoë Holmes and M. Cerezo.** “Moments of Quantum Channel Ensembles.” *PRX Quantum* **7**, 033050 (2026). [Published article](https://doi.org/10.1103/grdp-jph9); [arXiv:2511.12700v2](https://arxiv.org/html/2511.12700v2).

**Locator and assumptions.** Section III.3, Theorem 3, Eq. (66), and Appendix C study moment operators of concatenated random-unitary layers interleaved with fixed noise. Their channel-design bounds keep the moment order, number of layers, and dimension-dependent factors explicit.

**Relation.** Channel moments and noise-induced concentration are established frameworks. The result used here instead concerns a fixed acquisition channel acting independently on copies of one unknown Haar-distributed input, and bounds its output-state moment relative to the output of the maximally mixed state. Theorem 3 is not an immediate substitute for this single-channel bound or its heterogeneous threshold: its object and quantitative parameters differ. This is a scope comparison, not a claim that every consequence of their framework has been exhausted.

The version checked is v2, September 9, 2026, the publication date.

## Statistical setting and acquisition-noise boundaries

<a id="chen2022"></a>
### Chen et al.: the noiseless memory separation

**Sitan Chen, Jordan Cotler, Hsin-Yuan Huang and Jerry Li.** “Exponential Separations Between Learning With and Without Quantum Memory.” *2021 IEEE 62nd Annual Symposium on Foundations of Computer Science*, pp. 574–585, proceedings published 2022. [DOI](https://doi.org/10.1109/FOCS52979.2021.00063); [arXiv:2111.05881v2](https://arxiv.org/html/2111.05881v2).

In the full preprint, Theorems 5.11 and 5.13 give matching $\Theta(2^{n/2})$ sample complexity for pure-versus-maximally-mixed testing without quantum memory. Table 1 contrasts this with constant-copy testing with memory. This is the baseline task. The exponent is $n/2$, not $n$. The present lower bound concerns noisy acquisition while granting the learner unrestricted memory.

<a id="berta2021"></a>
### Berta, Brandão and Hirche: composite quantum hypothesis testing

**Mario Berta, Fernando G. S. L. Brandão and Christoph Hirche.** “On Composite Quantum Hypothesis Testing.” *Communications in Mathematical Physics* **385**, 55–77 (2021). [DOI](https://doi.org/10.1007/s00220-021-04133-8); [arXiv:1709.07268v2](https://arxiv.org/html/1709.07268v2).

Section 1, Eqs. (9)–(12) and Theorem 1.1 consider asymmetric testing of mixtures of tensor powers, with fixed finite-dimensional one-copy state spaces and closed convex sets. The result characterizes asymptotic error exponents through regularized relative entropy.

This provides context for composite alternatives and correlated mixture states. It is not an imported finite-sample theorem for the dimension-growing pure-state promise. In particular, forming a convex hull of pure states *before* taking tensor powers would include the maximally mixed state and change the problem. The Haar average of repeated copies must remain $\mathbb E_\psi[\mathcal N(\psi)^{\otimes m}]$.

The checked v2, July 23, 2021, states that it matches the published version and includes corrections.

<a id="yaozhuang2026"></a>
### Yao and Zhuang: testing finite labelled ensembles

**Jian Yao and Quntao Zhuang.** “Hypothesis testing between quantum ensembles.” [arXiv:2608.21321v1](https://arxiv.org/abs/2608.21321v1), August 21, 2026; [author-affiliated institutional abstract](https://cqn-erc.org/arxiv-abstract/hypothesis-testing-between-quantum-ensembles/).

The abstract describes finite labelled ensembles, invariance under label permutations, and power-weighted moments conditional on observed label patterns. That differs from the unlabelled repeated-copy acquisition model here and is relevant context for moment-based discrimination.

**Verification limit:** the primary abstract and metadata were accessible; the full text was not. No theorem-level exclusion or proof dependency is asserted on this basis. This entry records a related recent source that warrants full-text comparison when available.

<a id="takagi2023"></a>
### Takagi, Tajima and Gu: universal mitigation sampling bounds

**Ryuji Takagi, Hiroyasu Tajima and Mile Gu.** “Universal Sampling Lower Bounds for Quantum Error Mitigation.” *Physical Review Letters* **131**, 210602 (2023). [DOI](https://doi.org/10.1103/PhysRevLett.131.210602); [arXiv:2208.09178v4](https://arxiv.org/abs/2208.09178v4).

This work bounds the sample cost of general error-mitigation procedures, including nonlinear postprocessing, and obtains exponential costs in circuit depth for several noise models. It establishes the broader inference-based limitation on correcting noisy data. The result here concerns a particular pre-noise state promise and a single acquisition channel. It does not introduce the general principle that processing cannot restore distinguishability lost in the observations.

The checked v4, November 23, 2023, is identified as the published version.

<a id="quek2024"></a>
### Quek et al.: collective measurements in error-mitigation lower bounds

**Yihui Quek, Daniel Stilck França, Sumeet Khatri, Johannes Jakob Meyer and Jens Eisert.** “Exponentially tighter bounds on limitations of quantum error mitigation.” *Nature Physics* **20**, 1648–1658 (2024). [DOI](https://doi.org/10.1038/s41567-024-02536-7); [arXiv:2210.11505v3](https://arxiv.org/html/2210.11505v3).

Problem 1 explicitly allows collective measurements on noisy circuit outputs, with a classical description of the noiseless circuit and observables. The work proves strong worst-case sampling limitations for mitigation and related tasks using noisy-state indistinguishability.

This is an antecedent for the strength of the downstream measurement model. The present task has an unknown pure input and a pure-versus-maximally-mixed promise, rather than reconstruction of specified ideal-circuit expectations. An unrestricted-memory lower bound alone is therefore not a distinct contribution; the task-specific channel bound and threshold are the statements requiring comparison.

The inspected preprint is v3, March 29, 2024. Journal metadata were checked separately; theorem numbering here refers only to that preprint.

## Standard ingredients and exact source locations

The proofs in this repository give the required specializations explicitly. The following references identify established ingredients, rather than attributing the local bounds to them.

<a id="watrous2018"></a>
### Watrous: states, channels, discrimination, and spherical moments

**John Watrous.** *The Theory of Quantum Information*. Cambridge University Press (2018). [Publisher](https://doi.org/10.1017/9781316848142); [author's book page](https://jhwatrous.github.io/books-and-courses.html).

Chapter 2 supplies states, channels, and measurements. Chapter 3, Theorem 3.4 is the Holevo–Helstrom theorem. Chapter 7, Section 7.1.1, Proposition 7.1 expresses the symmetric projector as a permutation average; Section 7.2, Lemma 7.24, Eq. (7.159) gives the spherical moment. Author-hosted chapters [2](https://jhwatrous.github.io/TQI.2.pdf), [3](https://jhwatrous.github.io/TQI.3.pdf), and [7](https://jhwatrous.github.io/TQI.7.pdf) were checked.

<a id="harrow2013"></a>
### Harrow: the pure-state Haar moment

**Aram W. Harrow.** “The Church of the Symmetric Subspace.” [arXiv:1308.6595v1](https://arxiv.org/abs/1308.6595v1) (2013).

Proposition 6, Eq. (7), gives

$$
\mathbb E_\psi[\psi^{\otimes m}]
=\frac{\sum_{\pi\in S_m}P_\pi}
{d(d+1)\cdots(d+m-1)}.
$$

This is the standard moment identity used in the channel-bound proof. The permutation trace factorization and the cycle-counting product are derived there in the notation of this problem. Harrow's Section 3 also explains higher-moment concentration methods.

<a id="mele2024"></a>
### Mele: a tutorial treatment of Haar moments

**Antonio Anna Mele.** “Introduction to Haar Measure Tools in Quantum Information: A Beginner's Tutorial.” *Quantum* **8**, 1340 (2024). [Published article and PDF](https://quantum-journal.org/papers/q-2024-05-08-1340/); [DOI](https://doi.org/10.22331/q-2024-05-08-1340).

Sections 3–4 develop moment operators and the symmetric subspace. Theorem 22, Eq. (95), and Eq. (103) give the pure-state moment identity. Section 9.1 supplies examples of moment calculations. These locators refer to the published PDF.

<a id="petz1986"></a>
### Petz: sufficiency and recovery

**Dénes Petz.** “Sufficient subalgebras and the relative entropy of states of a von Neumann algebra.” *Communications in Mathematical Physics* **105**, 123–131 (1986). [DOI](https://doi.org/10.1007/BF01212345).

This is historical attribution for the sufficiency/recovery framework. The finite-dimensional recovery formula and support convention used here are stated directly in the proof and can also be found in [Wilde, Section 12.3](#wilde2017). No approximate-recoverability theorem is needed to establish the channel bound.

<a id="petz1988"></a>
### Petz: sufficiency of channels

**Dénes Petz.** “Sufficiency of channels over von Neumann algebras.” *The Quarterly Journal of Mathematics* **39**, 97–108 (1988). [Publisher](https://doi.org/10.1093/qmath/39.1.97).

This is the channel formulation of the sufficiency framework. The Petz map is established prior mathematics; its use as an algebraic round trip here does not imply that the learner implements recovery or that recovery succeeds.

<a id="wilde2017"></a>
### Wilde: a finite-dimensional Petz-map reference

**Mark M. Wilde.** *Quantum Information Theory*, second edition. Cambridge University Press (2017). [Publisher](https://doi.org/10.1017/9781316809976); [author manuscript](https://www.markwilde.com/qit-notes.pdf).

The author manuscript, titled *From Classical to Quantum Shannon Theory* and dated December 5, 2021, was consulted. Section 12.3, Definition 12.3.1, Eq. (12.30) defines the Petz map; Eqs. (12.31)–(12.33) address its trace on the output support. Chapters 4 and 9 cover noisy states, channels, and trace distance. These locators are to the author manuscript, not a claim of identical pagination in the published edition.

<a id="muellerlennert2013"></a>
### Müller-Lennert et al.: the sandwiched Rényi convention

**Martin Müller-Lennert, Frédéric Dupuis, Oleg Szehr, Serge Fehr and Marco Tomamichel.** “On quantum Rényi entropies: A new generalization and some properties.” *Journal of Mathematical Physics* **54**, 122203 (2013). [DOI](https://doi.org/10.1063/1.4838856); [arXiv:1306.3142v4](https://arxiv.org/abs/1306.3142v4).

This is a source for the sandwiched Rényi family. With natural logarithms, the collision quantity used here is $\exp(\widetilde D_2(\rho\Vert\sigma))-1$. It is not the unsandwiched expression $\operatorname{Tr}(\rho^2\sigma^{-1})-1$. The needed trace-distance inequality is proved locally.

<a id="ekert2002"></a>
### Ekert et al.: SWAP measurements of purity

**Artur K. Ekert, Carolina Moura Alves, Daniel K. L. Oi, Michał Horodecki, Paweł Horodecki and L. C. Kwek.** “Direct Estimations of Linear and Nonlinear Functionals of a Quantum State.” *Physical Review Letters* **88**, 217901 (2002). [DOI](https://doi.org/10.1103/PhysRevLett.88.217901); [arXiv:quant-ph/0203016](https://arxiv.org/abs/quant-ph/0203016).

Their controlled-SWAP construction directly estimates state overlaps and purity. The constructive upper bound here uses this established observable, together with an explicit lower bound on the purity of the noisy output and concentration of bounded independent outcomes.

<a id="ruskai2003"></a>
### Ruskai: the qubit entanglement-breaking boundary

**Mary Beth Ruskai.** “Qubit Entanglement Breaking Channels.” *Reviews in Mathematical Physics* **15**, 643–662 (2003). [DOI](https://doi.org/10.1142/S0129055X03001710); [arXiv:quant-ph/0302032v3](https://arxiv.org/html/quant-ph/0302032v3).

Theorem 4 states that a unital qubit channel in canonical Bloch form is entanglement breaking exactly when the sum of the absolute values of its three diagonal parameters is at most one. Substituting $(\eta,\eta,\eta)$ yields the $\eta\le1/3$ boundary used in the comparison above.

## Scope of the comparison

The channel bound and the product-depolarizing criterion are proved in this repository. The cited works establish the surrounding models and the standard ingredients. No claim of absolute priority follows from this bounded comparison.

The polynomial-sample equivalence concerns the specified product-depolarizing family. The general Petz parameter is a sufficient condition for hardness, not a complete classification of acquisition channels. The conclusions do not cover source-side encoding, access to the noise environment, a state-preparation oracle, or promises that restrict the pure states to a protected family.

Bibliographic metadata and the stated locators were checked against primary publisher, author, or arXiv sources on October 25, 2026. Version-dependent statements and the one abstract-only comparison are identified above.
