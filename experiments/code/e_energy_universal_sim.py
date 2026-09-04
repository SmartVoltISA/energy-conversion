"""Computational control experiments for the ENERGY architecture.

Ideal mathematical models only. These validate the accounting architecture
before any physical bench experiment.
"""
import numpy as np


def rc_charge(Vs=5.0, R=100.0, C=1e-3, t_end=1.0, dt=1e-5):
    t = np.arange(0.0, t_end + dt, dt)
    v = Vs * (1.0 - np.exp(-t / (R * C)))
    i = (Vs - v) / R
    e_in = np.trapezoid(Vs * i, t)
    e_c = 0.5 * C * v[-1] ** 2
    e_r = np.trapezoid(v * i, t)
    return e_in, e_c, e_r, e_in - e_c - e_r


def rc_discharge(V0=5.0, R=100.0, C=1e-3, t_end=1.0, dt=1e-5):
    t = np.arange(0.0, t_end + dt, dt)
    v = V0 * np.exp(-t / (R * C))
    i = v / R
    e_c0 = 0.5 * C * V0 ** 2
    e_r = np.trapezoid(v * i, t)
    return e_c0, e_r, e_c0 - e_r, v[-1]


def rl_step(Vs=5.0, R=100.0, L=10e-3, t_end=0.02, dt=1e-6):
    t = np.arange(0.0, t_end + dt, dt)
    i = Vs / R * (1.0 - np.exp(-t / (L / R)))
    e_in = np.trapezoid(Vs * i, t)
    e_l = 0.5 * L * i[-1] ** 2
    e_r = np.trapezoid(R * i ** 2, t)
    return e_in, e_l, e_r, e_in - e_l - e_r


def rlc_free(R=0.5, L=10e-3, C=1e-3, V0=5.0, t_end=0.02, dt=1e-6):
    """Series RLC free response, integrated with RK4."""
    n = int(round(t_end / dt)) + 1
    q = np.empty(n); i = np.empty(n)
    q[0] = C * V0; i[0] = 0.0

    def f(qv, iv):
        return iv, (-qv / C - R * iv) / L

    for k in range(n - 1):
        h = dt
        a, b = f(q[k], i[k])
        c, d = f(q[k] + h*a/2, i[k] + h*b/2)
        e, g = f(q[k] + h*c/2, i[k] + h*d/2)
        j, m = f(q[k] + h*e, i[k] + h*g)
        q[k+1] = q[k] + h*(a + 2*c + 2*e + j)/6
        i[k+1] = i[k] + h*(b + 2*d + 2*g + m)/6

    e_c = 0.5 * q**2 / C
    e_l = 0.5 * L * i**2
    e_loss = np.trapezoid(R * i**2, dx=dt)
    e0 = e_c[0] + e_l[0]
    ef = e_c[-1] + e_l[-1]
    return e0, ef, e_loss, e0 - ef - e_loss


def main():
    tests = {
        "RC charge": rc_charge(),
        "RC discharge": rc_discharge(),
        "RL step": rl_step(),
        "RLC free": rlc_free(),
    }
    print("ENERGY computational control experiments")
    for name, values in tests.items():
        print(name, ":", ", ".join(f"{float(x):.12g}" for x in values))


if __name__ == "__main__":
    main()
