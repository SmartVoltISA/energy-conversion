"""Stress-test the energy-accounting architecture across many parameter sets.

This is a computational experiment, not a physical experiment. It searches for
numerical or architectural counterexamples in standard ideal RC/RL/RLC models.
"""
import numpy as np


def rc_charge(Vs, R, C, dt, t_end):
    t = np.arange(0.0, t_end + dt, dt)
    v = Vs * (1.0 - np.exp(-t / (R * C)))
    i = (Vs - v) / R
    ein = np.trapezoid(Vs * i, t)
    ec = 0.5 * C * v[-1] ** 2
    er = np.trapezoid(v * i, t)
    return abs(ein - ec - er), max(abs(ein), abs(ec), abs(er), 1e-30)


def rl_step(Vs, R, L, dt, t_end):
    t = np.arange(0.0, t_end + dt, dt)
    i = Vs / R * (1.0 - np.exp(-t / (L / R)))
    ein = np.trapezoid(Vs * i, t)
    el = 0.5 * L * i[-1] ** 2
    er = np.trapezoid(R * i ** 2, t)
    return abs(ein - el - er), max(abs(ein), abs(el), abs(er), 1e-30)


def rlc_free(R, L, C, V0, dt, t_end):
    n = int(round(t_end / dt)) + 1
    q = np.empty(n); i = np.empty(n)
    q[0] = C * V0; i[0] = 0.0

    def f(qv, iv):
        return iv, (-qv / C - R * iv) / L

    for k in range(n - 1):
        a, b = f(q[k], i[k])
        c, d = f(q[k] + dt*a/2, i[k] + dt*b/2)
        e, g = f(q[k] + dt*c/2, i[k] + dt*d/2)
        j, m = f(q[k] + dt*e, i[k] + dt*g)
        q[k+1] = q[k] + dt*(a + 2*c + 2*e + j)/6
        i[k+1] = i[k] + dt*(b + 2*d + 2*g + m)/6

    ec = 0.5 * q**2 / C
    el = 0.5 * L * i**2
    e0 = ec[0] + el[0]
    ef = ec[-1] + el[-1]
    loss = np.trapezoid(R * i**2, dx=dt)
    return abs(e0 - ef - loss), max(abs(e0), abs(ef), abs(loss), 1e-30)


def main(seed=20260904, samples=10000):
    rng = np.random.default_rng(seed)
    worst = {"RC": (0.0, None), "RL": (0.0, None), "RLC": (0.0, None)}
    failures = []

    for k in range(samples):
        Vs = 10 ** rng.uniform(-1, 1)
        R = 10 ** rng.uniform(0, 3)
        C = 10 ** rng.uniform(-5, -2)
        tau = R * C
        dt = tau / rng.choice([100, 300, 1000])
        t_end = tau * 8
        absres, scale = rc_charge(Vs, R, C, dt, t_end)
        rel = absres / scale
        if rel > worst["RC"][0]: worst["RC"] = (rel, (Vs, R, C, dt, t_end))
        if rel > 1e-8: failures.append(("RC", k, rel))

        L = 10 ** rng.uniform(-5, -1)
        tau_l = L / R
        dt_l = tau_l / rng.choice([100, 300, 1000])
        absres, scale = rl_step(Vs, R, L, dt_l, tau_l * 8)
        rel = absres / scale
        if rel > worst["RL"][0]: worst["RL"] = (rel, (Vs, R, L, dt_l))
        if rel > 1e-8: failures.append(("RL", k, rel))

        Rl = 10 ** rng.uniform(-2, 1)
        Ll = 10 ** rng.uniform(-4, -1)
        Cc = 10 ** rng.uniform(-5, -2)
        period = 2 * np.pi * np.sqrt(Ll * Cc)
        dt_r = period / rng.choice([1000, 3000])
        absres, scale = rlc_free(Rl, Ll, Cc, Vs, dt_r, period * 5)
        rel = absres / scale
        if rel > worst["RLC"][0]: worst["RLC"] = (rel, (Rl, Ll, Cc, Vs, dt_r))
        if rel > 1e-8: failures.append(("RLC", k, rel))

    print(f"samples={samples}")
    print(f"failures={len(failures)}")
    for name, (rel, params) in worst.items():
        print(f"{name}: worst_relative_residual={rel:.6e} params={params}")
    if failures:
        print("FIRST_FAILURE", failures[0])
    else:
        print("No residual exceeded 1e-8 relative to the energy scale.")


if __name__ == "__main__":
    main()
