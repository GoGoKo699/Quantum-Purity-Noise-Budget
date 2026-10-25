# What the noise budget constrains

The [model](model.md) places noise at the interface between an unknown source and a learner. The learner receives independent noisy examples and has complete control only afterward. This placement isolates a resource limitation that persists under perfect downstream storage, fault-tolerant computation and collective measurement.

## 1. A property carried by correlations between examples

One noisy example cannot distinguish the maximally mixed source from a Haar-averaged pure source: both average to the same state. Repeated copies of one fixed pure state contain additional information because they share a common unknown direction. In the noiseless case, the SWAP operator detects that common purity with a constant number of examples at fixed error.

Independent acquisition noise weakens the repeated-copy correlations. The [general channel theorem](channel_bound.md) bounds their distinguishability for an arbitrary joint measurement, by expressing a collision moment through the Petz round-trip channel. The recovery map is an analytical device in the proof. Its physical implementation is neither assumed nor charged as a free operation.

The converse is stronger than a statement that one particular purity estimator has a small signal. It bounds every decision procedure on the received copies. At the same time, its general-channel parameter is a sufficient hardness criterion rather than a complete classification of all channels. The [dephasing example](examples.md) makes this distinction explicit.

## 2. Why a logarithmic budget is the relevant scale

For local depolarization, define $b_i=1-\eta_i^2$ and $B_n=\sum_i b_i$. The channel parameter factorizes:

```math
\kappa_n=\prod_i\left(1-\frac{b_i}{2}\right)
\le e^{-B_n/2}.
```

The all-copy converse therefore requires a number of examples at least exponential in $B_n$ up to a constant in the exponent. An exponential in the total budget is polynomial in the number of qubits precisely when that budget is logarithmic.

The constructive side reaches the same boundary for a different reason. A depolarizing channel is a random Pauli channel. When the errors on two copies coincide, their contribution to the output purity is exactly one. All other terms are nonnegative. The probability that the two error strings coincide gives a uniform purity floor

```math
A_n=\prod_i\frac{1+3\eta_i^2}{4}\ge4^{-B_n}.
```

For logarithmic $B_n$, this signal is inverse polynomial, whereas the null purity $2^{-n}$ is exponentially small. Pair measurements can resolve the gap with polynomially many copies. This argument holds for entangled pure inputs and does not require different Pauli errors to produce orthogonal states.

The two bounds establish the same polynomial boundary without determining the exact optimal exponential rate. The [threshold theorem](threshold.md) states the finite bounds and the regime in which they give matching exponential dependence up to constants.

## 3. Which resources the positive procedure uses

Each trial compares two received $n$-qubit states. A Bell measurement on each corresponding qubit pair determines the local SWAP eigenvalue; multiplying these signs gives the global SWAP outcome. This uses two registers, $O(n)$ elementary gates and measurements, and $O(n)$ classical operations per trial. Repeating the procedure only needs the current two registers and an accumulated statistic.

This implementation assumes the corresponding qubit pairs can interact after acquisition. A geometric architecture may add routing cost. That cost does not weaken the converse, which already permits unrestricted processing. It does require separate accounting when translating the constructive test to a particular device.

The test needs known noise parameters or a known conservative total-budget bound that yields a positive purity gap. Estimating an unknown acquisition channel is a separate input-calibration task. The theorem supplies no advantage for preparing its unknown data source, loading classical data, or identifying an arbitrary channel from scratch.

## 4. Consequential changes of access

| Change | Consequence |
|---|---|
| Unlimited memory or joint measurements after acquisition | Already included in the converse |
| Noise shared across copies | Changes the joint state; a common random unitary can preserve purity correlations despite completely mixed one-copy marginals |
| Encoding or controlling the source before noise | Changes the source interface and can protect information that the present learner never receives |
| Environment or noise-record access | Supplies additional information absent from the stated channel output |
| Restricting the pure-state family or providing its description | Changes the minimax problem and may remove the hard prior |
| Replacing the maximally mixed null by an arbitrary mixed alternative | Defines a different promise-testing problem |

These are changes to the mathematical model, rather than repairs available inside it. The full-collective lower bound remains compatible with error correction that acts before the irreversible source channel, with learning structured source families, and with quantum advantages for other tasks.

## 5. Strong noise, identifiability and comparison with classical learners

An exponential lower bound does not imply that every extensive noise profile has a finite exponential sample complexity. If half of an even number of qubits are fully replaced and the input consists of Bell pairs across the lost and retained halves, the output is exactly maximally mixed. The two promises then overlap and no number of examples separates them with error below one half. The [worked channels](examples.md) and [threshold account](threshold.md) give the precise construction.

Conversely, when every depolarizing retention parameter is positive, the finite-dimensional channel is invertible as a linear map. Its pure-output image cannot contain the null. Compactness gives a positive separation for each fixed system size, so finite tomography followed by testing is possible, even when the number of examples is very large. Linear invertibility does not supply a physical inverse channel or a polynomial bound.

Finally, an exponential quantum sample lower bound does not determine the ratio between the best quantum and classical strategies. Establishing that ratio would require matched bounds in a separately specified classical measurement model. The statement established here is the unrestricted quantum learner's polynomial threshold for the given source promise.

## 6. Connection to prior work

The distinction from [noisy two-copy learning](../references/RELATED_WORK.md#cgk2026) is the unrestricted collective measurement model. [Entanglement-breaking channels](../references/RELATED_WORK.md#bhalerao2026) already admit strong all-memory lower bounds; the local-noise theorem here reaches arbitrarily weak noise and identifies its vanishing-noise threshold. [Reduced Haar states](../references/RELATED_WORK.md#bansal2025) are an established collective source-channel example and a direct antecedent of the moment method. [Quantum error-mitigation lower bounds](../references/RELATED_WORK.md#takagi2023) establish the wider importance of information lost before downstream processing.

The useful conclusion is specific: for unrestricted unknown pure sources under independent heterogeneous local depolarization, a logarithmic total noise budget is exactly the boundary for polynomial acquisition cost, and a pairwise comparison procedure attains that boundary.
