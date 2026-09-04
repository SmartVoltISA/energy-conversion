"""Search for history-dependent counterexamples to visible-state-only accounting.

Toy hysteresis model. The visible variable x is the same at selected checkpoints,
but an internal memory m changes the next transition cost. This is deliberately
not a physical material model; it tests whether hidden state is necessary in the
architecture.
"""
import numpy as np


def step(x, m, u, alpha=0.8):
    """State transition with explicit internal memory."""
    x_new = np.clip(x + u, -1.0, 1.0)
    m_new = np.clip((1.0 - alpha) * m + alpha * x_new, -1.0, 1.0)
    # Model-defined transfer/dissipation cost; nonnegative by construction.
    cost = abs(u) * (1.0 + 0.5 * abs(m))
    return x_new, m_new, cost


def build_paths():
    # Both paths end at the same visible x=0, but with different internal memory.
    paths = {
        "positive_history": [1.0, -1.0, 0.0],
        "negative_history": [-1.0, 1.0, 0.0],
    }
    return paths


def replay(path):
    x, m = 0.0, 0.0
    rows = []
    for target in path:
        u = target - x
        x, m, cost = step(x, m, u)
        rows.append((x, m, cost))
    return rows


def main():
    paths = build_paths()
    histories = {name: replay(path) for name, path in paths.items()}

    # Compare identical visible state x=0 after the final transition.
    a = histories["positive_history"][-1]
    b = histories["negative_history"][-1]
    assert np.isclose(a[0], 0.0) and np.isclose(b[0], 0.0)
    assert not np.isclose(a[1], b[1])

    # Same visible next transition, x: 0 -> 1, gives different costs.
    xa, ma = a[0], a[1]
    xb, mb = b[0], b[1]
    _, _, ca = step(xa, ma, 1.0)
    _, _, cb = step(xb, mb, 1.0)
    assert not np.isclose(ca, cb)

    print("positive_history_final", a)
    print("negative_history_final", b)
    print("same_visible_state", xa, xb)
    print("different_internal_memory", ma, mb)
    print("same_visible_transition_costs", ca, cb)
    print("counterexample_confirmed=True")
    print("interpretation=visible_state_only_is_insufficient")
    print("physical_claim=False")


if __name__ == "__main__":
    main()
