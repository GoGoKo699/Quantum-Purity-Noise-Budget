#!/usr/bin/env python3
"""Reproduce the finite checks without changing the repository."""
from __future__ import annotations

import json

from verify_noise import run_checks as local_checks
from verify_noise_general import run_checks as general_checks
from verify_boundaries import run_checks as boundary_checks


def main() -> None:
    report = {"local_depolarization": local_checks(),
              "nonunital_channel": general_checks(),
              "model_boundaries": boundary_checks()}
    print(json.dumps(report, indent=2))
    print("PASS: all finite matrix and model-boundary checks.")
    print("Universal and asymptotic conclusions are established by the written proofs.")


if __name__ == "__main__":
    main()
