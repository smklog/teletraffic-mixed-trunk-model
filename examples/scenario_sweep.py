"""
examples/scenario_sweep.py

Parameter-sweep experiment for the mixed-traffic trunk model.

Generates two charts:
- Blocking vs outgoing offered load
- Retry load vs outgoing offered load

Use this script to demonstrate how the model behaves under increasing load
and to produce plots for the README or presentations.
"""

import matplotlib.pyplot as plt

from traffic_model import TrunkGroupParameters, solve_trunk_group


def run_sweep():
    # Base configuration of the trunk group
    V = 300
    A_in = 40.0
    A_2p = 20.0
    retry_factor = 0.3
    p_T = 0.3

    # Sweep outgoing offered load from 10 to 80 Erlangs
    loads = list(range(10, 81, 5))

    blocking = []
    retries = []

    for A_out in loads:
        params = TrunkGroupParameters(
            V=V,
            A_in=A_in,
            A_out=float(A_out),
            A_2p=A_2p,
            retry_factor=retry_factor,
            pstn_block_prob=p_T,
        )
        res = solve_trunk_group(params)
        blocking.append(res.blocking_prob)
        retries.append(res.retry_load)

    # Chart 1: Blocking vs Offered Outgoing Load
    plt.figure()
    plt.plot(loads, blocking)
    plt.xlabel("Outgoing Offered Load (Erlangs)")
    plt.ylabel("Blocking Probability (Erlang-B)")
    plt.title("Blocking vs Outgoing Offered Load")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("examples/blocking_vs_load.png", dpi=200)

    # Chart 2: Retry Load vs Offered Outgoing Load
    plt.figure()
    plt.plot(loads, retries)
    plt.xlabel("Outgoing Offered Load (Erlangs)")
    plt.ylabel("Retry Load (Erlangs)")
    plt.title("Retry Load vs Outgoing Offered Load")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("examples/retry_vs_load.png", dpi=200)

    print("Charts generated:")
    print(" - examples/blocking_vs_load.png")
    print(" - examples/retry_vs_load.png")


if __name__ == "__main__":
    run_sweep()
