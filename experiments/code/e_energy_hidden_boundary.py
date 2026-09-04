"""Test whether omitting an internal state creates an apparent energy residual.

The model has visible x and hidden memory m. A state-dependent internal reservoir
R(m) is included in the complete accounting. We compare that closed account with
a deliberately incomplete account that observes only x.
"""
import numpy as np


def reservoir(m):
    return 0.5 * m * m


def transition(x, m, u):
    x_new = np.clip(x + u, -1.0, 1.0)
    m_new = np.clip(0.5 * m + 0.5 * x_new, -1.0, 1.0)
    # Internal transfer is defined so total energy accounting closes exactly.
    # Visible storage: E_x = 0.5*x^2. Hidden reservoir: R(m).
    ex0 = 0.5 * x * x
    ex1 = 0.5 * x_new * x_new
    r0 = reservoir(m)
    r1 = reservoir(m_new)
    delta_total = (ex1 + r1) - (ex0 + r0)
    input_energy = delta_total
    return x_new, m_new, input_energy, ex0, ex1, r0, r1


def run(path):
    x = 0.0
    m = 0.0
    total_input = 0.0
    visible_delta = 0.0
    hidden_delta = 0.0
    rows = []
    for target in path:
        u = target - x
        x_new, m_new, ein, ex0, ex1, r0, r1 = transition(x, m, u)
        total_input += ein
        visible_delta += ex1 - ex0
        hidden_delta += r1 - r0
        rows.append((x_new, m_new, ein))
        x, m = x_new, m_new
    return total_input, visible_delta, hidden_delta, rows


def main():
    paths = {
        "positive": [1.0, -1.0, 0.0, 1.0],
        "negative": [-1.0, 1.0, 0.0, 1.0],
    }
    for name, path in paths.items():
        ein, dvis, dhid, rows = run(path)
        residual_visible_only = ein - dvis
        residual_full = ein - dvis - dhid
        print(name)
        print("E_input", ein)
        print("Delta_visible", dvis)
        print("Delta_hidden", dhid)
        print("residual_visible_only", residual_visible_only)
        print("residual_full", residual_full)
        assert np.isclose(residual_full, 0.0, atol=1e-12)
        assert not np.isclose(residual_visible_only, 0.0, atol=1e-12)
    print("hidden_boundary_counterexample_confirmed=True")
    print("full_account_closes=True")
    print("visible_only_account_closes=False")
    print("physical_claim=False")


if __name__ == "__main__":
    main()
