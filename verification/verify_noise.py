#!/usr/bin/env python3
"""Finite-dimensional matrix checks for a noisy Haar-moment lower bound.

This constructs the Haar moment by summing permutation matrices, applies
independent local depolarization directly to density matrices, and checks the
analytical chi-square bounds. It is a finite check, not a proof of the theorem.
"""
from __future__ import annotations

import itertools
import json
import math

import numpy as np


def haar_moment(d: int, copies: int) -> np.ndarray:
    size = d ** copies
    columns = np.arange(size)
    tuples = np.array(np.unravel_index(columns, (d,) * copies))
    total = np.zeros((size, size), dtype=np.float64)
    for permutation in itertools.permutations(range(copies)):
        rows = np.ravel_multi_index(tuples[list(permutation)], (d,) * copies)
        total[rows, columns] += 1
    return total / math.prod(d + j for j in range(copies))


def local_depolarize(matrix: np.ndarray, eta: float | list[float], qubits: int) -> np.ndarray:
    out = matrix.copy()
    rates = [eta] * qubits if isinstance(eta, (int, float)) else eta
    assert len(rates) == qubits
    for q in range(qubits):
        rest = [j for j in range(qubits) if j != q]
        order = [q] + rest + [qubits + q] + [qubits + j for j in rest]
        tensor = np.transpose(out.reshape((2,) * (2 * qubits)), order)
        small = tensor.reshape(2, 2 ** (qubits - 1), 2, 2 ** (qubits - 1))
        reduced = np.trace(small, axis1=0, axis2=2)
        replacement = np.einsum("ab,ij->aibj", np.eye(2) / 2, reduced)
        updated = rates[q] * small + (1 - rates[q]) * replacement
        out = np.transpose(updated.reshape((2,) * (2 * qubits)), np.argsort(order)).reshape(matrix.shape)
    return out


def derangements(k: int) -> int:
    if k == 0:
        return 1
    if k == 1:
        return 0
    previous, current = 1, 0
    for j in range(2, k + 1):
        previous, current = current, (j - 1) * (previous + current)
    return current


def check_case(n: int, copies: int, eta: float | list[float]) -> dict:
    d = 2 ** n
    size = d ** copies
    rates = [eta] * n if isinstance(eta, (int, float)) else eta
    moment = local_depolarize(haar_moment(d, copies), rates * copies, n * copies)
    assert np.max(np.abs(moment - moment.T)) < 2e-12
    assert abs(np.trace(moment) - 1) < 2e-12
    chi2 = float(size * np.sum(moment * moment) - 1)
    kappa = math.prod((1 + value ** 2) / 2 for value in rates)
    gamma = math.prod((1 + value ** 4) / 2 for value in rates)
    denominator = math.prod(1 + j / d for j in range(copies))
    finite_bound = math.prod(1 + j * kappa for j in range(copies)) / denominator - 1
    exp_bound = math.expm1(copies * (copies - 1) * (kappa - 1 / d) / 2)
    gamma_bound = sum(math.comb(copies, k) * derangements(k) * gamma ** (k / 2)
                      for k in range(copies + 1)) / denominator - 1
    assert chi2 >= -2e-12
    assert chi2 <= finite_bound + 2e-11
    assert finite_bound <= exp_bound + 2e-11
    assert chi2 <= gamma_bound + 2e-11
    if copies == 2:
        exact_m2 = (math.prod(1 + 3 * value ** 4 for value in rates) - 1) / (d + 1) ** 2
        assert abs(chi2 - exact_m2) < 2e-12
    if all(value == 0 for value in rates):
        assert abs(chi2) < 2e-12
        assert np.max(np.abs(moment - np.eye(size) / size)) < 2e-12
    if all(value == 1 for value in rates):
        exact_identity = math.factorial(copies) / denominator - 1
        assert abs(chi2 - exact_identity) < 2e-11
        assert abs(chi2 - finite_bound) < 2e-11
    return dict(n=n, copies=copies, eta=eta, dimension=size,
                chi2=chi2, kappa_finite_bound=finite_bound,
                kappa_exp_bound=exp_bound, gamma_finite_bound=gamma_bound)


def check_purity_bounds() -> dict:
    rng = np.random.default_rng(20261025)
    cases = 0
    minimum_slack = float("inf")
    for rates in [[0.5], [0, 1], [0, 0, 1], [0.1, 0.4, 0.9],
                  [1, 1, 1, 1], [0, 0, 1, 1], [0.99, 0.98, 0.97, 0.96, 0.95]]:
        n = len(rates)
        d = 2 ** n
        collision_floor = math.prod((1 + 3 * value ** 2) / 4 for value in rates)
        budget = sum(1 - value ** 2 for value in rates)
        kappa = math.prod((1 + value ** 2) / 2 for value in rates)
        assert collision_floor >= math.exp(-math.log(4) * budget) - 2e-12
        assert kappa <= math.exp(-budget / 2) + 2e-12
        vectors = [np.eye(d, dtype=complex)[:, 0],
                   (np.eye(d, dtype=complex)[:, 0] + np.eye(d, dtype=complex)[:, -1]) / math.sqrt(2)]
        for _ in range(10):
            vector = rng.normal(size=d) + 1j * rng.normal(size=d)
            vectors.append(vector / np.linalg.norm(vector))
        for vector in vectors:
            rho = np.outer(vector, vector.conj())
            sigma = local_depolarize(rho, rates, n)
            purity = float(np.trace(sigma @ sigma).real)
            assert purity >= collision_floor - 2e-12
            assert purity >= 1 / d - 2e-12
            minimum_slack = min(minimum_slack, purity - collision_floor)
            cases += 1
    return dict(cases=cases, minimum_purity_floor_slack=minimum_slack,
                scope="Direct finite checks of the pure-output collision floor and budget inequalities.")


def run_checks() -> dict:
    cases = [(n, m, eta) for n, m in [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 3)]
             for eta in [0, 0.2, 0.5, 0.9, 1]]
    results = [check_case(*case) for case in cases]
    for rates in [[0, 1], [0.2, 0.9], [0, 0, 1], [0.1, 0.5, 0.99]]:
        for copies in [2, 3]:
            results.append(check_case(len(rates), copies, rates))
    purity_checks = check_purity_bounds()
    return {"status": "passed", "moment_cases": len(results),
            "maximum_matrix_dimension": max(r["dimension"] for r in results),
            "pure_state_cases": purity_checks["cases"]}


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2))
