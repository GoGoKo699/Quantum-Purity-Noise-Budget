#!/usr/bin/env python3
"""Finite check of the arbitrary-channel/Petz extension on amplitude damping."""
import json
import math
import numpy as np
from verify_noise import haar_moment


def amplitude_damp(matrix, loss, qubits):
    out = matrix.astype(complex)
    for q in range(qubits):
        rest = [j for j in range(qubits) if j != q]
        order = [q] + rest + [qubits + q] + [qubits + j for j in rest]
        tensor = np.transpose(out.reshape((2,) * (2 * qubits)), order)
        small = tensor.reshape(2, 2 ** (qubits - 1), 2, 2 ** (qubits - 1))
        updated = np.empty_like(small)
        updated[0, :, 0, :] = small[0, :, 0, :] + loss * small[1, :, 1, :]
        updated[1, :, 1, :] = (1 - loss) * small[1, :, 1, :]
        updated[0, :, 1, :] = math.sqrt(1 - loss) * small[0, :, 1, :]
        updated[1, :, 0, :] = math.sqrt(1 - loss) * small[1, :, 0, :]
        out = np.transpose(updated.reshape((2,) * (2 * qubits)), np.argsort(order)).reshape(matrix.shape)
    return out


def run_checks():
    results = []
    for m in [1, 2, 3, 4, 5]:
        for loss in [0, 0.1, 0.5, 0.9, 1]:
            moment = amplitude_damp(haar_moment(2, m), loss, m)
            null = np.array([1.0])
            for _ in range(m):
                null = np.kron(null, [(1 + loss) / 2, (1 - loss) / 2])
            inverse_fourth = np.zeros_like(null)
            mask = null > 0
            inverse_fourth[mask] = null[mask] ** (-0.25)
            weighted = inverse_fourth[:, None] * moment * inverse_fourth[None, :]
            chi2 = float(np.sum(np.abs(weighted) ** 2) - 1)
            r = math.sqrt((1 - loss) / (1 + loss))
            kappa = (1 + r) / 2
            bound = math.prod((1 + j * kappa) / (1 + j / 2) for j in range(m)) - 1
            delta = moment - np.diag(null)
            trace_distance = float(np.sum(np.abs(np.linalg.eigvalsh(delta))) / 2)
            assert chi2 >= -3e-12
            assert chi2 <= bound + 3e-12
            assert trace_distance <= math.sqrt(max(0, chi2)) / 2 + 3e-12
            if m == 2:
                assert abs(chi2 - (2 * r ** 2 + r ** 4) / 9) < 3e-12
            if loss == 1:
                assert abs(chi2) < 3e-12 and trace_distance < 3e-12
            results.append(dict(copies=m, loss=loss, chi2=chi2, kappa_bound=bound,
                                trace_distance=trace_distance))
    return {"status": "passed", "amplitude_damping_cases": len(results)}


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2))
