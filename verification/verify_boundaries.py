#!/usr/bin/env python3
"""Direct density-matrix checks of consequential model boundaries."""
from __future__ import annotations

import math
import numpy as np

from verify_noise import local_depolarize


def run_checks() -> dict:
    tolerance = 3e-12
    cases = 0

    # Fully replace one half of a maximally entangled state. The output
    # coincides with the maximally mixed null, including its normalization.
    for half_dimension in (2, 4):
        vector = np.eye(half_dimension).reshape(-1) / math.sqrt(half_dimension)
        pure = np.outer(vector, vector)
        half_qubits = int(math.log2(half_dimension))
        total_qubits = 2 * half_qubits
        output = local_depolarize(pure, [0] * half_qubits + [1] * half_qubits,
                                  total_qubits)
        null = np.eye(half_dimension ** 2) / half_dimension ** 2
        assert np.max(np.abs(output - null)) < tolerance
        cases += 1

    # Full dephasing fixes a basis state (so kappa=1) while mapping
    # a uniform coherent pure state to the null. The general sufficient
    # hardness criterion is not a complete channel classification.
    for dimension in (2, 4):
        uniform = np.ones(dimension) / math.sqrt(dimension)
        pure = np.outer(uniform, uniform)
        dephased = np.diag(np.diag(pure))
        assert np.max(np.abs(dephased - np.eye(dimension) / dimension)) < tolerance
        basis_state = np.diag([1.0] + [0.0] * (dimension - 1))
        assert np.max(np.abs(np.diag(np.diag(basis_state)) - basis_state)) < tolerance
        cases += 1

    # Identically shared Pauli noise has the same completely mixed
    # one-copy marginal as independent noise, but preserves the SWAP
    # expectation of every pure pair. Independence across copies matters.
    identity = np.eye(2, dtype=complex)
    paulis = (identity, np.array([[0, 1], [1, 0]], dtype=complex),
              np.array([[0, -1j], [1j, 0]], dtype=complex),
              np.diag([1, -1]).astype(complex))
    vector = np.array([math.sqrt(0.3), 1j * math.sqrt(0.7)])
    pure = np.outer(vector, vector.conj())
    outputs = [p @ pure @ p.conj().T for p in paulis]
    marginal = sum(outputs) / 4
    shared = sum(np.kron(state, state) for state in outputs) / 4
    independent = np.kron(marginal, marginal)
    swap = np.zeros((4, 4))
    for a in range(2):
        for b in range(2):
            swap[2 * b + a, 2 * a + b] = 1
    assert np.max(np.abs(marginal - identity / 2)) < tolerance
    assert abs(np.trace(swap @ shared) - 1) < tolerance
    assert abs(np.trace(swap @ independent) - 0.5) < tolerance
    cases += 1

    return {"status": "passed", "boundary_cases": cases}


if __name__ == "__main__":
    print(run_checks())
