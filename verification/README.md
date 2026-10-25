# Reproduce the finite checks

The scientific conclusions are proved in the [channel bound](../science/channel_bound.md), [constructive test](../science/constructive_test.md) and [threshold theorem](../science/threshold.md). This suite independently constructs small density matrices to check the normalizations, finite formulas and consequential boundary examples.

## Run

The recorded environment is Python 3.12.14 with NumPy 2.3.5. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner performs no network access and does not write output files. It exits unsuccessfully if an assertion fails. Its expected summary is 48 local-depolarization Haar-moment cases, 84 pure-state purity-floor cases, 25 amplitude-damping cases and 5 model-boundary checks, followed by `PASS: all finite matrix and model-boundary checks.` The largest matrix dimension in the local-depolarization suite is 512.

## What is checked

| Module | Independent construction | Checks |
|---|---|---|
| [verify_noise.py](verify_noise.py) | Builds the Haar moment by summing permutation matrices, then applies local channels directly to tensor indices | Unit trace, Hermiticity in the real test family, nonnegative collision divergence to tolerance, the finite and exponential channel bounds, the optional maximal-purity bound, identity and complete-depolarization limits, and the exact two-copy formula |
| [verify_noise.py](verify_noise.py) | Applies the channel directly to deterministic and fixed-seed complex pure states | The random-Pauli output-purity floor, the budget inequalities and the state-space purity floor, including heterogeneous and zero retention parameters |
| [verify_noise_general.py](verify_noise_general.py) | Applies amplitude damping to Haar moments and forms the nonuniform reference output directly | The sandwiched collision expression, trace-distance comparison, channel bound, exact two-copy value and rank-deficient full-replacement limit |
| [verify_boundaries.py](verify_boundaries.py) | Constructs entangled, dephased and correlated-noise examples as explicit matrices | Exact overlap of the two promises after replacing half of a maximally entangled state; failure of the channel parameter to classify full dephasing; preservation of SWAP information under shared noise despite identical one-copy marginals |

Haar moments are represented by their exact finite permutation formula and then evaluated in double-precision arithmetic. These are not symbolic exact-arithmetic checks. Tolerances are at most a few times $10^{-11}$ for the tested inequalities; they accommodate floating-point roundoff rather than an analytical error term. The fixed random seed makes the selected pure-state examples reproducible, and their sample count is not evidence for all pure states.

The local suite also checks the independently derived identity

```math
\chi^2\!\left(M_2\middle\|(I/2^n)^{\otimes2}\right)
=\frac{\prod_i(1+3\eta_i^4)-1}{(2^n+1)^2}.
```

The bound can be strict: for one qubit, the exact expression is $\eta^4/3$, whereas the finite maximum-eigenvalue bound gives $\eta^2/3$. The suite does not treat an upper bound as an exact sample rate.

## What the checks establish

Passing these checks supports the tested matrix identities, parameter conventions and finite examples. The all-dimension channel theorem, the uniform guarantee over all pure states, and the asymptotic polynomial threshold require the written proofs. The suite does not certify an optimal exponential constant, an efficient physical preparation of Haar states, or a quantum-to-classical sample-complexity ratio.

The scripts are intentionally independent of any claimed general multiplicativity theorem: the product-channel extrema and the constructive signal floor are proved directly in the scientific account.
