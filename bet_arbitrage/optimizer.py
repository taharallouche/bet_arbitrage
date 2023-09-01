from scipy.optimize import linprog, OptimizeResult
from inventory import Sport, SPORTS_LINEAR_PROG

# Example odds a, b, d = 3.5, 3.45, 2.38


def get_optimal_bet(
    odds: list[float], sport: Sport, budget: float = 100
) -> OptimizeResult:
    linear_prog = SPORTS_LINEAR_PROG[sport]

    opt = linprog(
        c=linear_prog.obj,
        A_ub=linear_prog.A_ub(odds),
        b_ub=linear_prog.b_ub(budget),
        method="revised simplex",
    )

    return opt
