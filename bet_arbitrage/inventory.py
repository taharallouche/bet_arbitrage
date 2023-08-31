from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class _FOOTBALL_LINEAR_PROG:
    """Linear programming problem for football betting:
    max z
    s.t.
        x1 + x2 + x3 <= a * x1
        x1 + x2 + x3 <= b * x2
        x1 + x2 + x3 <= d * x3
        x1 + x2 + x3 <= budget
        z <= a * x1
        z <= b * x2
        z <= d * x3
    """

    obj = [0, 0, 0, -1]
    A_ub = lambda odds: [  # noqa: E731
        [1 - odds[0], 1, 1, 0],
        [1, 1 - odds[1], 1, 0],
        [1, 1, 1 - odds[2], 0],
        [1, 1, 1, 0],
        [-odds[0], 0, 0, 1],
        [0, -odds[1], 0, 1],
        [0, 0, -odds[2], 1],
    ]

    b_ub = lambda budget: [0, 0, 0, budget, 0, 0, 0]  # noqa: E731


class Sport(Enum):
    football = "football"


FOOTBALL_LINEAR_PROG = _FOOTBALL_LINEAR_PROG()
SPORTS_LINEAR_PROG = {Sport.football: FOOTBALL_LINEAR_PROG}
