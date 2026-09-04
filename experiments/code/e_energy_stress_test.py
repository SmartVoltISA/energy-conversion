"""Stress-test energy accounting across random ideal RC/RL/RLC systems.

Computational experiment only. The accounting terms are evaluated analytically
for the ideal models, avoiding false failures caused only by coarse numerical
quadrature. A separate numerical-control section can test discretization.
"""
import math
import numpy as np


def _int_exp(k, T):
    return math.expm1(k * T) / k


def _int_exp_sin2(a, w, T):
    p = 2.0 * a
    I0 = (1.0 - math.exp(-p * T)) / p if p else T
    b = 2.0 * w
    Ic = (p + math.exp(-p * T) * (-p * math.cos(b * T) + b * math.sin(b * T))) / (p * p + b * b)
    return 0.5 * (I0 - Ic)


def rc_charge(Vs, R, C, t_end):
    tau = R * C
    x = t_end / tau
    e = math.exp(-x)
    ein = (Vs * Vs / R) * tau * (1.0 - e)
    ec = 0.5 * C * Vs * Vs * (1.0 - e) ** 2
    er = (Vs * Vs / R) * tau * ((1.0 - e) - 0.5 * (1.0 - e * e))
    return abs(ein - ec - er), max(abs(ein), abs(ec), abs(er), 1e-30)


def rl_step(Vs, R, L, t_end):
    tau = L / R
    x = t_end / tau
    e = math.exp(-x)
    ein = (Vs * Vs / R) * (t_end - tau * (1.0 - e))
    i_end = Vs / R * (1.0 - e)
    el = 0.5 * L * i_end * i_end
    er = (Vs * Vs / R) * (t_end - 2.0 * tau * (1.0 - e) + 0.5 * tau * (1.0 - e * e))
    return abs(ein - el - er), max(abs(ein), abs(el), abs(er), 1e-30)


def rlc_free(R, L, C, V0):
    """Return exact relative accounting residual for a free series RLC response."""
    w0 = 1.0 / math.sqrt(L * C)
    alpha = R / (2.0 * L)
    q0 = C * V0
    e0 = 0.5 * C * V0 * V0

    if alpha < w0:
        wd = math.sqrt(w0 * w0 - alpha * alpha)
        T = 5.0 * 2.0 * math.pi / w0
        expT = math.exp(-alpha * T)
        qT = expT * q0 * (math.cos(wd * T) + (alpha / wd) * math.sin(wd * T))
        iT = expT * (-q0 * w0 * w0 / wd * math.sin(wd * T))
        amp = q0 * w0 * w0 / wd
        loss = R * amp * amp * _int_exp_sin2(alpha, wd, T)
    elif alpha == w0:
        T = 8.0 / alpha
        qT = q0 * math.exp(-alpha * T) * (1.0 + alpha * T)
        iT = -q0 * alpha * alpha * T * math.exp(-alpha * T)
        p = 2.0 * alpha
        integral_t2 = (2.0 - math.exp(-p * T) * (p * p * T * T + 2.0 * p * T + 2.0)) / (p ** 3)
        loss = R * (q0 * alpha * alpha) ** 2 * integral_t2
    else:
        s = math.sqrt(alpha * alpha - w0 * w0)
        r1, r2 = -alpha + s, -alpha - s
        A = (-r2 * q0) / (r1 - r2)
        B = q0 - A
        T = 8.0 / (-r1)
        e1, e2 = math.exp(r1 * T), math.exp(r2 * T)
        qT = A * e1 + B * e2
        iT = A * r1 * e1 + B * r2 * e2
        loss = R * (
            (A * r1) ** 2 * _int_exp(2.0 * r1, T)
            + (B * r2) ** 2 * _int_exp(2.0 * r2, T)
            + 2.0 * A * r1 * B * r2 * _int_exp(r1 + r2, T)
        )

    ef = 0.5 * qT * qT / C + 0.5 * L * iT * iT
    return abs(e0 - ef - loss), max(abs(e0), abs(ef), abs(loss), 1e-30)


def main(seed=20260904, samples=10000, threshold=1e-10):
    rng = np.random.default_rng(seed)
    worst = {"RC": (0.0, None), "RL": (0.0, None), "RLC": (0.0, None)}
    failures = []

    for k in range(samples):
        Vs = 10 ** rng.uniform(-1, 1)
        R = 10 ** rng.uniform(0, 3)
        C = 10 ** rng.uniform(-5, -2)
        a, s = rc_charge(Vs, R, C, 8.0 * R * C)
        rel = a / s
        if rel > worst["RC"][0]: worst["RC"] = (rel, (Vs, R, C))
        if rel > threshold: failures.append(("RC", k, rel))

        L = 10 ** rng.uniform(-5, -1)
        a, s = rl_step(Vs, R, L, 8.0 * L / R)
        rel = a / s
        if rel > worst["RL"][0]: worst["RL"] = (rel, (Vs, R, L))
        if rel > threshold: failures.append(("RL", k, rel))

        Rl = 10 ** rng.uniform(-2, 1)
        Ll = 10 ** rng.uniform(-4, -1)
        Cc = 10 ** rng.uniform(-5, -2)
        a, s = rlc_free(Rl, Ll, Cc, Vs)
        rel = a / s
        if rel > worst["RLC"][0]: worst["RLC"] = (rel, (Rl, Ll, Cc, Vs))
        if rel > threshold: failures.append(("RLC", k, rel))

    print(f"samples={samples}")
    print(f"threshold={threshold:.1e}")
    print(f"failures={len(failures)}")
    for name, (rel, params) in worst.items():
        print(f"{name}: worst_relative_residual={rel:.6e} params={params}")
    if failures:
        print("FIRST_FAILURE", failures[0])
    else:
        print("No residual exceeded threshold.")


if __name__ == "__main__":
    main()
