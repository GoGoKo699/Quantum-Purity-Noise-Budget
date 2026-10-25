# Thirty milestones for the purity noise-budget result

These milestones organize the project by mathematical dependency and scientific purpose. **Phase I contains twelve background milestones**, moving from individual states and operations to the clean collective-testing problem. **Phase II contains eighteen narrative and innovation milestones**, moving from a single acquisition channel to its collective moment bound, the heterogeneous noise threshold, and the boundaries of that conclusion. The allocation follows the proof: its operational and symmetry foundations are substantial, while its main argument requires separate converse, construction, asymptotic, and scope analyses.

John Watrous, *The Theory of Quantum Information* (2018), is the educational anchor throughout. Specific sections supply the background language and results. The repository's scientific files are authoritative for the channel bound, its local calculations, and the threshold theorem; a Watrous pointer does not attribute those project results to the textbook. The [Watrous bridge](WATROUS_BRIDGE.md#source-route) records the source route and the distinction between imported ingredients and local derivations. Other references in the repository serve scientific attribution.

Each milestone states a central question, its understanding target, earlier dependencies and role in the argument, a conceptual connection, and precise source pointers. Dependencies refer to mathematical content rather than a learner's progress.

## Phase I — Background and preliminaries

The phase starts with the geometry of a single quantum state and ends with a complete explanation of why clean repeated copies reveal purity. It establishes the statistical experiment to which the noisy result will apply.

<a id="m01"></a>
### M01 — The source promise as a statement about states

**Central question.** What distinguishes an unknown pure source from the maximally mixed source before any measurement is chosen?

**Understanding target.** A density operator is positive semidefinite with unit trace. In dimension $`d`$, a pure state has rank one and purity $`\mathrm{Tr}(\rho^2)=1`$, while $`I/d`$ has purity $`1/d`$. The promise concerns an arbitrary unknown pure state, so it supplies neither a preferred basis nor its classical description.

**Dependencies and story role.** None. This fixes the two hypotheses and the dimension normalization used throughout the project.

**Conceptual connection.** Purity is a basis-independent spectral property; ignorance of a pure state's direction is different from the source itself being maximally mixed.

**Watrous anchor.** [Section 2.1.2, “Quantum states of registers”](https://jhwatrous.github.io/TQI.2.pdf).

**Project pointers.** [Source promise](../science/model.md#1-operational-model); [identity acquisition](../science/examples.md#identity-acquisition); [states and acquisition bridge](WATROUS_BRIDGE.md#states-and-acquisition).

<a id="m02"></a>
### M02 — A pure source can have a mixed accessible part

**Central question.** How can discarding part of a pure system erase the distinction in M01?

**Understanding target.** Partial trace describes the state available on a subsystem. A pure bipartite state can have a maximally mixed reduction, and the reduced state's rank is bounded by the dimension of the discarded subsystem. These facts separate global source purity from purity of the received state.

**Dependencies and story role.** [M01](#m01). Reduction introduces the simplest physical mechanism by which a source promise may become difficult or impossible to observe.

**Conceptual connection.** Entanglement converts loss of access into mixedness. The same mechanism later gives both a collective hardness example and an exact overlap of the two promises.

**Watrous anchor.** [Section 2.1.3, “Reductions and purifications of quantum states”](https://jhwatrous.github.io/TQI.2.pdf).

**Project pointers.** [Partial-trace example](../science/examples.md#partial-trace-and-the-induced-state-antecedent); [source interface](../science/model.md#1-operational-model); [states and acquisition bridge](WATROUS_BRIDGE.md#states-and-acquisition).

<a id="m03"></a>
### M03 — Acquisition noise as a quantum channel

**Central question.** Which mathematical object describes the corruption occurring before learner access?

**Understanding target.** A completely positive trace-preserving map $`\mathcal N`$ sends the source state to the received state. The received null is $`\sigma=\mathcal N(I/d)`$, which need not be maximally mixed. Local depolarization is a special channel with a retention parameter, while an arbitrary channel may change dimension or have a singular reference output.

**Dependencies and story role.** [M01](#m01), [M02](#m02). This defines the acquisition interface and distinguishes general-channel statements from the later depolarizing specialization.

**Conceptual connection.** The placement of a channel matters: a map acting before access changes the available information, whereas processing after access acts on information already received.

**Watrous anchor.** [Section 2.2.1, “Definitions and basic notions concerning channels,” Definition 2.13](https://jhwatrous.github.io/TQI.2.pdf).

**Project pointers.** [Operational model](../science/model.md#1-operational-model); [local depolarization](../science/model.md#3-local-depolarization-and-total-noise); [states and acquisition bridge](WATROUS_BRIDGE.md#states-and-acquisition).

<a id="m04"></a>
### M04 — A decision rule is a measurement effect

**Central question.** How is a physical measurement translated into the two errors of the purity decision?

**Understanding target.** A two-outcome measurement is specified by an effect $`0\le E\le I`$, with “pure” probability $`\mathrm{Tr}(E\rho)`$. The null error and the error for every pure alternative are bounded separately. A valid test is one effect with guarantees uniform over the unknown pure state.

**Dependencies and story role.** [M01](#m01), [M03](#m03). This turns the source promise into a quantitative statistical task and fixes what success means.

**Conceptual connection.** Linearity of measurement probabilities permits averaging over unknown states in a lower-bound proof without changing the learner's decision rule.

**Watrous anchor.** [Section 2.3.1, “Two equivalent definitions of measurements”](https://jhwatrous.github.io/TQI.2.pdf).

**Project pointers.** [Minimax error criterion](../science/model.md#2-minimax-error-and-charged-resources); [discrimination bridge](WATROUS_BRIDGE.md#discrimination).

<a id="m05"></a>
### M05 — Repeated copies of one unknown state

**Central question.** Which independence assumption preserves the multi-copy information being learned?

**Understanding target.** Conditional on one fixed source state $`\rho`$, independent channel uses produce $`\mathcal N(\rho)^{\otimes m}`$. Averaging a pure source once gives $`\mathbb E_\psi[\mathcal N(\psi)^{\otimes m}]`$, whereas choosing a fresh Haar state on every call gives $`\sigma^{\otimes m}`$. The order of averaging and taking tensor powers changes the experiment.

**Dependencies and story role.** [M01](#m01), [M02](#m02), [M03](#m03). This establishes the repeated-source structure that the collective converse must retain.

**Conceptual connection.** Conditional independence and an unknown common parameter produce correlations in the averaged multi-copy state.

**Watrous anchor.** [Sections 2.1.2–2.1.3](https://jhwatrous.github.io/TQI.2.pdf) for joint states and reductions; [Section 7.2.1, “Uniform spherical measure and Haar measure”](https://jhwatrous.github.io/TQI.7.pdf) for the prior's mathematical setting.

**Project pointers.** [Operational model](../science/model.md#1-operational-model); [legitimacy of Haar averaging](../science/model.md#5-why-averaging-over-pure-states-is-legitimate); [Haar bridge](WATROUS_BRIDGE.md#haar-moments).

<a id="m06"></a>
### M06 — Unlimited downstream processing has one statistical input

**Central question.** Why can a joint-measurement lower bound cover adaptive protocols and arbitrary quantum memory?

**Understanding target.** A protocol with a deterministic maximum of $`m`$ calls acts on the $`m`$ supplied systems, with unused copies appended and ignored if necessary. Ancillas, intermediate operations, classical adaptation, and a final decision induce an effect on that received tensor-product state. The bound counts a maximum number of calls, not an unbounded stopping rule's expected cost.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M05](#m05). This identifies the full measurement class included in the converse.

**Conceptual connection.** Operational complexity after acquisition can be compressed into a statistical decision on the available data without charging or restricting that complexity.

**Watrous anchor.** [Sections 2.2.1 and 2.3.1](https://jhwatrous.github.io/TQI.2.pdf) for channel composition and measurement effects.

**Project pointers.** [Permitted resources](../science/model.md#1-operational-model); [bounded-copy reduction](../science/channel_bound.md#5-from-a-haar-prior-to-worst-case-error); [discrimination bridge](WATROUS_BRIDGE.md#discrimination).

<a id="m07"></a>
### M07 — The norms that connect algebra to observation

**Central question.** Why do trace norm, operator norm, and Hilbert–Schmidt norm all appear in one proof?

**Understanding target.** Trace norm measures the operational separation of states; operator norm controls the largest eigenvalue of a positive output; Hilbert–Schmidt norm records a quadratic overlap. Schatten Hölder inequalities connect these roles, allowing a quadratic moment calculation to bound trace distance.

**Dependencies and story role.** [M01](#m01), [M04](#m04). This supplies the matrix inequalities needed to turn channel spectra into limits on measurement success.

**Conceptual connection.** Different norms retain different information about the same operator. The proof chooses a computable quadratic quantity, then transfers its control to an operational norm.

**Watrous anchor.** [Section 1.1.3, “Operator decompositions and norms,” particularly Eqs. (1.173)–(1.174)](https://jhwatrous.github.io/TQI.1.pdf).

**Project pointers.** [Trace-distance step](../science/channel_bound.md#4-trace-distance); [channel coefficient](../science/channel_bound.md#setup-and-channel-parameter); [weighted-collision bridge](WATROUS_BRIDGE.md#weighted-collision).

<a id="m08"></a>
### M08 — Binary discrimination fixes the error normalization

**Central question.** How much trace distance is necessary when both decision errors are at most $`\delta`$?

**Understanding target.** For equal priors, optimal binary success is $`(1+T(\rho,\sigma))/2`$, where $`T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$. Two errors at most $`\delta\lt 1/2`$ imply average error at most $`\delta`$ and therefore require $`T(\rho,\sigma)\ge1-2\delta`$.

**Dependencies and story role.** [M04](#m04), [M06](#m06), [M07](#m07). This fixes the operational constant later propagated through C1.

**Conceptual connection.** A minimax guarantee implies an equal-prior Bayesian guarantee, which can be bounded by an exact state-discrimination formula.

**Watrous anchor.** [Section 3.1.1, “Discriminating between pairs of quantum states,” Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf).

**Project pointers.** [Worst-case-to-binary reduction](../science/channel_bound.md#5-from-a-haar-prior-to-worst-case-error); [error convention](../science/model.md#2-minimax-error-and-charged-resources); [discrimination bridge](WATROUS_BRIDGE.md#discrimination).

<a id="m09"></a>
### M09 — A Haar prior proves a worst-case lower bound

**Central question.** Why may the proof average pure states when the task asks for success on every pure state?

**Understanding target.** Uniform success implies success after averaging the alternative over any prior. A unitarily invariant pure-state prior yields $`M_m=\mathbb E_\psi[\mathcal N(\psi)^{\otimes m}]`$ and null $`S_m=\sigma^{\otimes m}`$. In particular, $`M_1=\sigma`$, so one copy cannot solve the worst-case promise at error below one half.

**Dependencies and story role.** [M05](#m05), [M08](#m08). This supplies the hard binary experiment for the converse.

**Conceptual connection.** Symmetry removes the unknown direction from the proof while preserving the common-state correlations between copies. It supplies no efficient source-preparation assumption.

**Watrous anchor.** [Section 7.2.1, Definition 7.16 and the spherical-measure setting](https://jhwatrous.github.io/TQI.7.pdf), together with [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf).

**Project pointers.** [Haar prior and its limits](../science/model.md#5-why-averaging-over-pure-states-is-legitimate); [Haar bridge](WATROUS_BRIDGE.md#haar-moments).

<a id="m10"></a>
### M10 — Repetition creates permutation symmetry

**Central question.** Which subspace contains tensor powers of one pure state?

**Understanding target.** The vector $`|\psi\rangle^{\otimes m}`$ is invariant under permutation of its factors. Averaging the permutation operators gives the symmetric-subspace projector, whose dimension is $`\binom{d+m-1}{m}`$. The group acts on copies, not on the qubit sites within a copy.

**Dependencies and story role.** [M02](#m02), [M05](#m05). This identifies the symmetry responsible for an exact finite Haar moment.

**Conceptual connection.** A continuous average over state directions can be represented by a finite sum over copy permutations.

**Watrous anchor.** [Section 7.1.1, “The subspace of permutation-invariant vectors,” Proposition 7.1, Eq. (7.8), and Proposition 7.2, Eq. (7.16)](https://jhwatrous.github.io/TQI.7.pdf).

**Project pointers.** [Permutation-moment proof](../science/channel_bound.md#3-haar-moments-and-permutation-cycles); [identity acquisition](../science/examples.md#identity-acquisition); [Haar bridge](WATROUS_BRIDGE.md#haar-moments).

<a id="m11"></a>
### M11 — The normalized pure-state moment

**Central question.** What exact operator replaces the Haar average of repeated pure states?

**Understanding target.** The normalized symmetric projector gives $`\mathbb E_\psi[\psi^{\otimes m}]=\sum_{\pi\in S_m^{\mathrm{perm}}}U_\pi/(d)_m`$, with $`(d)_m=d(d+1)\cdots(d+m-1)`$. At two copies this becomes $`(I+F)/[d(d+1)]`$, where $`F`$ swaps the copies. The rising factorial is essential to the later denominator and replacement-channel limit.

**Dependencies and story role.** [M09](#m09), [M10](#m10). This is the exact imported identity from which the project develops its noisy collision bound.

**Conceptual connection.** Normalization links the dimension of a symmetry sector to the statistical moments of random states.

**Watrous anchor.** [Section 7.2.1, Lemma 7.24, Eq. (7.159)](https://jhwatrous.github.io/TQI.7.pdf).

**Project pointers.** [Haar moment calculation](../science/channel_bound.md#3-haar-moments-and-permutation-cycles); [two-copy depolarizing identity](../science/examples.md#the-exact-two-copy-moment-under-local-depolarization); [Haar bridge](WATROUS_BRIDGE.md#haar-moments).

<a id="m12"></a>
### M12 — Phase I synthesis: why clean copies reveal purity

**Central question.** How do the state promise, collective measurement, and Haar moment combine in the noiseless problem?

**Understanding target.** For identity acquisition, the averaged alternative is the normalized symmetric projector and the null is $`I/d^m`$. A symmetric-subspace measurement accepts every pure source; its null acceptance is $`\binom{d+m-1}{m}/d^m`$. Four copies suffice for error at most $`1/3`$ for every $`d\ge2`$. The SWAP identity $`\mathrm{Tr}[F(\rho\otimes\rho)]=\mathrm{Tr}(\rho^2)`$ supplies another constant-copy route.

**Dependencies and story role.** [M04](#m04), [M05](#m05), [M08](#m08), [M11](#m11). This closes the background phase with the complete clean-source benchmark that acquisition noise will disrupt.

**Conceptual connection.** A property invisible to one averaged example is visible in correlations across repeated examples.

**Watrous anchor.** [Sections 7.1.1 and 7.2.1](https://jhwatrous.github.io/TQI.7.pdf), combined with [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf). The stated purity-test consequences are derived in the project.

**Project pointers.** [Identity acquisition](../science/examples.md#identity-acquisition); [resource interpretation](../science/interpretation.md#1-a-property-carried-by-correlations-between-examples); [result bridge](WATROUS_BRIDGE.md#reading-the-result).

## Phase II — Narrative and innovation

The phase starts with the reference output of one acquisition channel. It develops a bound on all received copies, specializes that bound to many noisy sites, and joins it to an implementable test. The final milestones place the resulting threshold within its exact statistical and physical scope.

<a id="m13"></a>
### M13 — The correct reference output and its support

**Central question.** How can the general proof normalize a channel whose null output is nonuniform or singular?

**Understanding target.** Positivity implies $`\mathcal N(\rho)\le d\sigma`$ for every input state, so every output lies in $`\Pi=\mathrm{supp}\sigma`$. Inverse powers of $`\sigma`$ act only there. The Petz map for $`\tau=I/d`$ is $`\mathcal R(Y)=d^{-1}\mathcal N^\dagger(\sigma^{-1/2}Y\sigma^{-1/2})`$; both the support convention and the factor $`1/d`$ are required.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M12](#m12). This replaces the noiseless uniform reference by the correct reference for arbitrary acquisition.

**Conceptual connection.** A change of statistical reference requires a compatible operator weighting, including when some output directions never occur.

**Watrous anchor.** [Sections 1.1.3](https://jhwatrous.github.io/TQI.1.pdf) and [2.2.1](https://jhwatrous.github.io/TQI.2.pdf) supply support, adjoint, and channel language. The particular Petz construction and its normalization are established in the local proof.

**Project pointers.** [Support and normalization](../science/channel_bound.md#1-support-and-normalization); [Petz-support bridge](WATROUS_BRIDGE.md#petz-support).

<a id="m14"></a>
### M14 — The normalized channel round trip

**Central question.** Which single-input channel parameters control the collective moment?

**Understanding target.** The composition $`\mathcal K=\mathcal R\circ\mathcal N`$ is completely positive, trace preserving, unital, and Hilbert–Schmidt self-adjoint. Its outputs on pure inputs define $`\kappa=\max_{\phi\ \mathrm{pure}}\|\mathcal K(\phi)\|_\infty`$ and $`\gamma=\max_{\phi\ \mathrm{pure}}\mathrm{Tr}[\mathcal K(\phi)^2]`$. For a bistochastic channel on one space, $`\mathcal K=\mathcal N^\dagger\mathcal N`$.

**Dependencies and story role.** [M03](#m03), [M07](#m07), [M13](#m13). These normalized one-copy parameters are the inputs to C1 and C2.

**Conceptual connection.** The round trip translates an output-space weighted overlap into ordinary input-space geometry. It is an analytical construction, with no recovery operation supplied to the learner.

**Watrous anchor.** [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) for channel properties and [Section 1.1.3](https://jhwatrous.github.io/TQI.1.pdf) for the norms. The round-trip properties are proved locally.

**Project pointers.** [Channel parameter](../science/channel_bound.md#setup-and-channel-parameter); [C2 parameter](../science/channel_bound.md#theorem-c2-a-bound-from-maximal-output-purity); [Petz-support bridge](WATROUS_BRIDGE.md#petz-support).

<a id="m15"></a>
### M15 — A weighted collision quantity bounds observation

**Central question.** Which quadratic quantity remains usable when the reference state is not maximally mixed?

**Understanding target.** The proof uses $`\chi^2_{1/2}(M\|S)=\mathrm{Tr}[(S^{-1/4}MS^{-1/4})^2]-1`$. Applying Schatten Hölder to $`S^{-1/4}(M-S)S^{-1/4}`$ gives $`T(M,S)\le\frac12\sqrt{\chi^2_{1/2}(M\|S)}`$. The ordering of factors matters for noncommuting states.

**Dependencies and story role.** [M07](#m07), [M08](#m08), [M13](#m13), [M14](#m14). This supplies the operational endpoint of the moment calculation.

**Conceptual connection.** Reference-weighted quadratic geometry can control every measurement without itself being an implemented measurement.

**Watrous anchor.** [Section 1.1.3, especially Schatten Hölder in Eq. (1.174)](https://jhwatrous.github.io/TQI.1.pdf), and [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf). The weighted quantity and its particular inequality are defined and derived locally.

**Project pointers.** [Collision convention](../science/channel_bound.md#setup-and-channel-parameter); [trace-distance proof](../science/channel_bound.md#4-trace-distance); [weighted-collision bridge](WATROUS_BRIDGE.md#weighted-collision).

<a id="m16"></a>
### M16 — The exact collision identity across all copies

**Central question.** How does an $`m`$-copy distinguishability calculation reduce to a scalar Haar moment?

**Understanding target.** Expanding the collision square introduces two independently averaged pure states, while each state remains fixed across its own $`m`$ factors. The result is $`1+\chi^2_{1/2}(M_m\|S_m)=d^m\mathbb E_{\psi,\phi}[(\mathrm{Tr}(\psi\mathcal K(\phi)))^m]`$. For fixed $`\phi`$, $`\mathcal K(\phi)`$ is a normalized density operator.

**Dependencies and story role.** [M05](#m05), [M11](#m11), [M14](#m14), [M15](#m15). This is the central algebraic reduction from arbitrary acquisition to a tractable moment.

**Conceptual connection.** Independent integration variables arise from squaring an ensemble average; they do not represent independently redrawn source states during the experiment.

**Watrous anchor.** [Section 7.2.1, Lemma 7.24](https://jhwatrous.github.io/TQI.7.pdf), with the channel formalism of [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf).

**Project pointers.** [Exact collision identity](../science/channel_bound.md#2-exact-collision-identity); [weighted-collision bridge](WATROUS_BRIDGE.md#weighted-collision); [Haar bridge](WATROUS_BRIDGE.md#haar-moments).

<a id="m17"></a>
### M17 — Permutation cycles bound the collective information

**Central question.** How do the spectra of individual round-trip outputs control every order of the Haar moment?

**Understanding target.** A permutation cycle of length $`\ell`$ contributes $`\mathrm{Tr}(\omega^\ell)`$. The bound $`\mathrm{Tr}(\omega^\ell)\le\kappa^{\ell-1}`$ and the cycle-generating product yield C1's ratio $`\prod_{j=0}^{m-1}\frac{1+j\kappa}{1+j/d}`$. Bounding nontrivial cycles instead by $`\gamma^{\ell/2}`$ yields C2's derangement sum. C2 is complementary; it does not uniformly improve C1's replacement limit.

**Dependencies and story role.** [M07](#m07), [M11](#m11), [M16](#m16). This provides the finite bounds before an error tolerance is imposed.

**Conceptual connection.** Copy permutations organize high-order correlations into spectral powers. Retaining fixed points separately explains the alternative purity-based bound.

**Watrous anchor.** [Sections 7.1.1 and 7.2.1](https://jhwatrous.github.io/TQI.7.pdf), and [Section 1.1.3](https://jhwatrous.github.io/TQI.1.pdf) for Schatten norm comparisons. The cycle bounds are local derivations.

**Project pointers.** [Cycle calculation](../science/channel_bound.md#3-haar-moments-and-permutation-cycles); [C2](../science/channel_bound.md#theorem-c2-a-bound-from-maximal-output-purity); [cycle-bound bridge](WATROUS_BRIDGE.md#cycle-bound).

<a id="m18"></a>
### M18 — C1 becomes an unrestricted copy lower bound

**Central question.** What does the collision bound imply for every successful learner?

**Understanding target.** Combining the Haar prior, Helstrom condition, and collision estimate gives $`m(m-1)\ge c_\delta/(\kappa-1/d)`$, where $`c_\delta=2\log[1+4(1-2\delta)^2]`$, when $`\kappa\gt 1/d`$. This holds for every deterministically bounded-copy protocol with both errors at most $`\delta`$. If $`\kappa=1/d`$, every averaged alternative equals its null and no such worst-case test exists.

**Dependencies and story role.** [M06](#m06), [M08](#m08), [M09](#m09), [M15](#m15), [M17](#m17). This completes the general collective converse.

**Conceptual connection.** A bound on available information applies simultaneously to all downstream algorithms, including ones that store every copy coherently.

**Watrous anchor.** [Section 3.1.1, Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf), combined with [Section 7.2.1](https://jhwatrous.github.io/TQI.7.pdf). The channel-dependent lower bound is C1.

**Project pointers.** [C1 statement](../science/channel_bound.md#theorem-c1-finite-moment-and-copy-bounds); [worst-case reduction](../science/channel_bound.md#5-from-a-haar-prior-to-worst-case-error); [discrimination bridge](WATROUS_BRIDGE.md#discrimination).

<a id="m19"></a>
### M19 — Exact local-channel extrema, even for entangled inputs

**Central question.** Why do the depolarizing parameters factorize when the unknown input need not?

**Understanding target.** Expanding local depolarization into retention and replacement bounds each retained-subset term by a reduced-state norm or purity. Product pure states attain every term's bound, giving $`\kappa_n=\prod_i\frac{1+\eta_i^2}{2}`$ and $`\gamma_n=\prod_i\frac{1+\eta_i^4}{2}`$. The argument establishes these extrema without assuming a general multiplicativity theorem.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M14](#m14), [M17](#m17). This connects the abstract channel coefficients to heterogeneous physical noise.

**Conceptual connection.** Entangled inputs are covered by local reduction inequalities, while simultaneous saturation comes from product inputs.

**Watrous anchor.** [Section 2.1.3](https://jhwatrous.github.io/TQI.2.pdf) for reductions, [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) for channels, and [Section 1.1.3](https://jhwatrous.github.io/TQI.1.pdf) for norm bounds.

**Project pointers.** [Exact coefficient](../science/threshold.md#exact-channel-coefficient); [maximal output purity](../science/examples.md#maximal-output-purity-for-the-same-local-channel); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m20"></a>
### M20 — A sitewise channel becomes a total noise budget

**Central question.** Which aggregate of unequal local rates is necessary for polynomial acquisition cost?

**Understanding target.** The budgets $`B_n=\sum_i(1-\eta_i^2)`$ and $`\Lambda_n=\sum_i(1-\eta_i)`$ obey $`\Lambda_n\le B_n\le2\Lambda_n`$. The product coefficient satisfies $`\kappa_n\le e^{-B_n/2}`$, so C1 gives $`M_n(\delta)\ge\sqrt{c_\delta}e^{B_n/4}`$. Consequently, any eventual polynomial copy bound requires $`B_n=O(\log n)`$.

**Dependencies and story role.** [M18](#m18), [M19](#m19). This establishes the necessary half of the threshold and its interpretation as an expected number of locally replaced sites.

**Conceptual connection.** Products of local contractions turn into sums under logarithms, translating many small corruptions into a global sample cost.

**Watrous anchor.** [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) supplies the channel-mixture framework; the total-budget reduction is proved in T1.

**Project pointers.** [Budget definitions](../science/model.md#3-local-depolarization-and-total-noise); [necessity proof](../science/threshold.md#necessity-including-unrestricted-collective-measurements); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m21"></a>
### M21 — Every pure source obeys a uniform output-purity floor

**Central question.** What signal can a single explicit test guarantee uniformly over all pure inputs?

**Understanding target.** A local depolarizing channel is a random Pauli channel. In the expansion of noisy output purity, coincident Pauli errors contribute one and all other terms are nonnegative. Thus $`\mathrm{Tr}[\mathcal N_n(\psi)^2]\ge A_n=\prod_i\frac{1+3\eta_i^2}{4}\ge4^{-B_n}`$, even for entangled $`\psi`$. Orthogonality of the error images is unnecessary.

**Dependencies and story role.** [M01](#m01), [M03](#m03), [M19](#m19). This starts the constructive half with a uniform signal, rather than an average-source guarantee.

**Conceptual connection.** Classical collision probability of two independent error strings lower-bounds a quantum output purity.

**Watrous anchor.** [Sections 2.1.2 and 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) supply state and channel representations. The purity floor and its budget inequality are derived locally.

**Project pointers.** [Output-purity floor and Pauli proof](../science/constructive_test.md#output-purity-has-a-uniform-lower-bound); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m22"></a>
### M22 — A global purity observable from local Bell measurements

**Central question.** How can the constructive test measure global SWAP with linear resources per pair?

**Understanding target.** Global SWAP is the product of corresponding local swaps. Each Bell singlet has swap eigenvalue $`-1`$, and the other Bell states have eigenvalue $`+1`$. CNOT, Hadamard, and computational measurements resolve these signs; their classical product gives a bounded global outcome with mean $`\mathrm{Tr}(\rho^2)`$. Each trial uses two $`n`$-qubit registers and $`O(n)`$ elementary gates.

**Dependencies and story role.** [M04](#m04), [M12](#m12), [M21](#m21). This turns the uniform purity signal into an explicit physical procedure.

**Conceptual connection.** A global observable can have a local measurement implementation when its commuting factors have accessible eigenbases.

**Watrous anchor.** [Section 2.3.1](https://jhwatrous.github.io/TQI.2.pdf) for measurements and [Section 7.1.1](https://jhwatrous.github.io/TQI.7.pdf) for permutation operators. The circuit and resource accounting are given in the project.

**Project pointers.** [Bell-measurement implementation](../science/constructive_test.md#a-circuit-with-linear-gate-count-per-pair); [implementation resources](../science/interpretation.md#3-which-resources-the-positive-procedure-uses); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m23"></a>
### M23 — A positive gap becomes a finite-error algorithm

**Central question.** How are the purity floor, source-copy count, and numerical threshold connected?

**Understanding target.** For a known $`a_n\le A_n`$ with $`\Delta_n=a_n-2^{-n}\gt 0`$, independent bounded SWAP outcomes give each error at most $`\exp(-t\Delta_n^2/8)`$. U1 therefore uses $`2\lceil8\log(1/\delta)/\Delta_n^2\rceil`$ source copies. A known integer $`L_n\ge B_n`$ permits the exact dyadic procedure when $`n\ge2L_n+2`$; when $`L_n=O(\log n)`$, classical counters and comparisons use $`O(\log n)`$ bits.

**Dependencies and story role.** [M20](#m20), [M21](#m21), [M22](#m22). This completes the constructive guarantee, including calibration inputs and the two-copy cost per trial.

**Conceptual connection.** An inverse-polynomial expectation gap is useful only together with concentration and a representable decision threshold.

**Watrous anchor.** [Section 2.3.1](https://jhwatrous.github.io/TQI.2.pdf) grounds the measurement probabilities. The concentration, dyadic threshold, and bit-resource arguments are explicit local calculations.

**Project pointers.** [U1](../science/constructive_test.md#theorem-u1-a-uniform-two-copy-test); [known-budget implementation](../science/constructive_test.md#a-known-budget-is-enough-exact-dyadic-implementation); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m24"></a>
### M24 — T1: the exact polynomial boundary

**Central question.** How do the converse and construction give an if-and-only-if statement for arbitrary rate sequences?

**Understanding target.** At fixed $`0\lt \delta\lt 1/2`$, an eventual bound $`M_n(\delta)\le Cn^k`$ exists exactly when $`B_n=O(\log n)`$, equivalently $`\Lambda_n=O(\log n)`$. In that regime, $`4^{-B_n}`$ is inverse polynomial and eventually dominates $`2^{-n}`$. Failure of an eventual logarithmic bound rules out a uniform polynomial bound, including for oscillating sequences; it need not imply superpolynomial growth at every size.

**Dependencies and story role.** [M18](#m18), [M20](#m20), [M23](#m23). This joins unrestricted collective necessity to a pairwise sufficient procedure.

**Conceptual connection.** Matching a feasibility boundary requires matching quantifiers and scales, even when lower and upper sample counts have different constants in their exponents.

**Watrous anchor.** [Sections 2.2.1 and 2.3.1](https://jhwatrous.github.io/TQI.2.pdf), [3.1.1](https://jhwatrous.github.io/TQI.3.pdf), and [7.2.1](https://jhwatrous.github.io/TQI.7.pdf) supply the background ingredients; T1 is the local synthesis.

**Project pointers.** [T1](../science/threshold.md#theorem-t1-polynomial-learnability-if-and-only-if-the-budget-is-logarithmic); [oscillating rates](../science/threshold.md#oscillating-sequences); [result bridge](WATROUS_BRIDGE.md#reading-the-result).

<a id="m25"></a>
### M25 — What the bounds say beyond the threshold

**Central question.** Which sample-growth claims follow for bounded and subextensive budgets?

**Understanding target.** If $`B_n=o(n)`$, the upper gap is eventually positive and the bounds give $`\log M_n(\delta)=\Theta_\delta(1+B_n)`$. A bounded budget permits constant copies at fixed error for sufficiently large $`n`$, while $`B_n/\log n\to\infty`$ forces superpolynomial cost. The added one covers zero or bounded budgets, and exact exponential constants remain undetermined.

**Dependencies and story role.** [M24](#m24). This separates the sharp polynomial classification from the coarser quantitative rate information.

**Conceptual connection.** A theorem can determine a complexity boundary exactly while retaining substantial slack in the optimal sample count.

**Watrous anchor.** [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf) fixes the error criterion, and [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) fixes the channel family. The asymptotic comparisons come from T1's explicit bounds.

**Project pointers.** [Bounded and subextensive budgets](../science/threshold.md#bounded-and-subextensive-budgets); [homogeneous rates](../science/threshold.md#homogeneous-noise); [local-noise bridge](WATROUS_BRIDGE.md#local-noise-budget).

<a id="m26"></a>
### M26 — Nonunital and singular channels test the general normalization

**Central question.** Does the general construction behave consistently beyond unital depolarization?

**Understanding target.** For amplitude damping, the null output is nonuniform, while the normalized round trip is unital with Bloch contractions $`(q,q,q^2)`$, where $`q=\sqrt{(1-g)/(1+g)}`$. Its parameters are $`\kappa=(1+q)/2`$ and $`\gamma=(1+q^2)/2`$. At complete damping, the support-restricted calculation gives a replacement channel. More generally, $`\kappa=1/d`$ characterizes replacement acquisition.

**Dependencies and story role.** [M13](#m13), [M14](#m14), [M16](#m16), [M18](#m18). These examples test the reference-output convention and singular endpoint of C1.

**Conceptual connection.** A channel can be nonunital while its reference-normalized round trip is unital; normalization is relative to the statistical null.

**Watrous anchor.** [Section 2.2.1](https://jhwatrous.github.io/TQI.2.pdf) for channels and [Section 1.1.3](https://jhwatrous.github.io/TQI.1.pdf) for operator decompositions. The parameter calculations are local.

**Project pointers.** [Amplitude damping](../science/examples.md#amplitude-damping-a-nonunital-example); [replacement acquisition](../science/examples.md#replacement-acquisition-including-singular-outputs); [examples bridge](WATROUS_BRIDGE.md#scope-and-examples).

<a id="m27"></a>
### M27 — Hardness and identifiability are different questions

**Central question.** When can a pure source become exactly indistinguishable from the null?

**Understanding target.** Partial trace can send a maximally entangled pure input to the maximally mixed output. Full dephasing has $`\kappa=1`$ yet maps a uniform coherent superposition to its null. For even $`n`$, completely depolarizing one half of Bell pairs gives $`B_n=n/2`$ and infinite worst-case copy cost. Thus a large coefficient does not certify learnability, and extensive budgets have no universal finite exponential upper bound.

**Dependencies and story role.** [M02](#m02), [M18](#m18), [M24](#m24), [M26](#m26). This fixes the boundary between a sufficient hardness parameter and a complete classification.

**Conceptual connection.** Small average distinguishability and exact overlap of composite hypotheses are different obstructions, although both limit uniform testing.

**Watrous anchor.** [Section 2.1.3](https://jhwatrous.github.io/TQI.2.pdf) and [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf).

**Project pointers.** [Partial trace](../science/examples.md#partial-trace-and-the-induced-state-antecedent); [dephasing](../science/examples.md#full-dephasing-the-criterion-is-not-complete); [extensive overlap](../science/threshold.md#extensive-noise-can-make-the-hypotheses-identical); [examples bridge](WATROUS_BRIDGE.md#scope-and-examples).

<a id="m28"></a>
### M28 — Changing access changes the theorem's input

**Central question.** Which physical modifications lie outside the acquisition model?

**Understanding target.** Source encoding into a protected subspace, access to environment records, restrictions on the pure-state family, and noise correlated across copies alter the received hypotheses. A common random unitary can preserve SWAP information despite maximally mixed one-copy averages. A proper code subspace also changes the null state. Downstream error correction, memory, and adaptation are already allowed by C1.

**Dependencies and story role.** [M06](#m06), [M27](#m27). This identifies precisely which modifications can evade a conclusion by changing its assumptions.

**Conceptual connection.** Physical resources matter through their position relative to the information-losing channel and through the source family they permit.

**Watrous anchor.** [Sections 2.1.3, 2.2.1, and 2.3.1](https://jhwatrous.github.io/TQI.2.pdf) for accessible subsystems, channels, and measurements.

**Project pointers.** [Changes of access](../science/interpretation.md#4-consequential-changes-of-access); [encoded source example](../science/examples.md#encoding-before-acquisition-changes-the-hypotheses); [exact scope](../science/channel_bound.md#exact-scope-of-the-conclusion); [examples bridge](WATROUS_BRIDGE.md#scope-and-examples).

<a id="m29"></a>
### M29 — The theorem, its evidence, and its attribution

**Central question.** Which conclusions are proved here, which ingredients are inherited, and what do the finite checks establish?

**Understanding target.** The channel and threshold claims rest on proofs over all relevant dimensions and pure inputs. Finite matrix checks test specific normalizations, moments, and boundary examples; they do not establish universal quantifiers or optimal exponents. Haar moments, binary discrimination, recovery, and SWAP estimation are established ingredients. The cited noisy-learning models require comparison by source promise, channel, and allowed measurements before any distinct contribution is stated.

**Dependencies and story role.** [M17](#m17), [M23](#m23), [M24](#m24), [M26](#m26), [M27](#m27), [M28](#m28). This separates the mathematical conclusion from stronger claims unsupported by it.

**Conceptual connection.** Proof, finite verification, and attribution answer different scientific questions and support different kinds of confidence.

**Watrous anchor.** [Section 3.1.1, Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf), and [Sections 7.1.1–7.2.1](https://jhwatrous.github.io/TQI.7.pdf) identify key exact imported results. Comparisons with primary research remain attribution, not additional educational anchors.

**Project pointers.** [Related work](../references/RELATED_WORK.md); [verification scope](../verification/README.md#what-the-checks-establish); [exact second moment](../science/channel_bound.md#an-exact-second-moment-identity); [source route](WATROUS_BRIDGE.md#source-route).

<a id="m30"></a>
### M30 — Synthesis: a sharp acquisition boundary with a simple test

**Central question.** What is the complete scientific claim once the converse, construction, and model boundaries are combined?

**Understanding target.** For one fixed arbitrary pure source versus the maximally mixed source, with independent heterogeneous local depolarization before learner access and fixed error tolerance $`0\lt \delta\lt 1/2`$, polynomial-copy learnability is equivalent to $`B_n=O(\log n)`$. C1 proves necessity for unrestricted collective measurements; U1 attains sufficiency with pairwise Bell measurements and polynomial resources given adequate noise information. The result specifies neither an optimal exponential constant nor a quantum-to-classical advantage ratio, and it does not classify arbitrary channels.

**Dependencies and story role.** [M18](#m18), [M23](#m23), [M24](#m24), [M25](#m25), [M27](#m27), [M28](#m28), [M29](#m29). This closes the local-to-global argument and states its conclusion with every operational qualification attached.

**Conceptual connection.** Information lost during acquisition constrains every later computation, while an elementary pair comparison can attain the resulting feasibility boundary.

**Watrous anchor.** [Sections 2.2.1 and 2.3.1](https://jhwatrous.github.io/TQI.2.pdf), [Section 3.1.1](https://jhwatrous.github.io/TQI.3.pdf), and [Sections 7.1.1–7.2.1](https://jhwatrous.github.io/TQI.7.pdf) provide the common channel, decision, and symmetry language for this synthesis.

**Project pointers.** [Precise result map](../science/model.md#4-principal-results-and-their-proof-homes); [T1](../science/threshold.md#theorem-t1-polynomial-learnability-if-and-only-if-the-budget-is-logarithmic); [resource interpretation](../science/interpretation.md); [result bridge](WATROUS_BRIDGE.md#reading-the-result).
