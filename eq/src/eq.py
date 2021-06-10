from sympy import Symbol, Function, Eq
from sympy import Rational
from sympy import pprint
from sympy import solve


def main() -> None:
    x = Symbol("x")
    L = Function("L")(x)
    mu0, A, N = Symbol("mu0"), Symbol("A"), Symbol("N")

    eq = Eq(L, Rational(1, 2) * mu0 * A * N  / x)

    dx = Symbol("dx")
    x0 = Symbol("x0")
    eq = eq.subs(x, x0 + dx)
    pprint(eq)

    k = Symbol("k")
    L = Symbol("L")
    eq = Eq(L, k / (x0 + dx))
    eq1 = eq.subs(L, 1500E-6).subs(dx, -0.05E-3)
    eq2 = eq.subs(L, 500E-6).subs(dx, 0.05E-3)

    ans = solve([eq1, eq2], [k, x0])
    pprint("K: {}, x0: {} [mm]".format(ans[k], ans[x0] * 1000))

    eq3 = eq.subs(k, ans[k]).subs(x0, ans[x0]).subs(dx, 0)
    l0 = solve(eq3)[0]
    pprint("L: {0:>6.0f} [uH] at X0 - dx".format(1500))
    pprint("L: {0:>6.0f} [uH] at X0     ".format(l0 * 1E+6))
    pprint("L: {0:>6.0f} [uH] at X0 + dx".format(500))


    eq = Eq(L, k / (x0 + dx))
    eq1 = eq.subs(L, 1700E-6).subs(dx, -0.1E-3)
    eq2 = eq.subs(L,  300E-6).subs(dx, +0.1E-3)

    ans = solve([eq1, eq2], [k, x0])
    pprint("K: {}, x0: {} [mm]".format(ans[k], ans[x0] * 1000))

    eq3 = eq.subs(k, ans[k]).subs(x0, ans[x0]).subs(dx, 0)
    l0 = solve(eq3)[0]
    pprint("L: {0:>6.0f} [uH] at X0 - dx".format(1500))
    pprint("L: {0:>6.0f} [uH] at X0     ".format(l0 * 1E+6))
    pprint("L: {0:>6.0f} [uH] at X0 + dx".format(500))

if __name__ == "__main__":
    main()
