from typing import Callable

from numpy import linspace
from numpy.typing import NDArray


def euler(func: Callable, y_init: float, t: NDArray) -> float:
    y: float = y_init
    h: float = t[1] - t[0]

    for i in t[:-1]:
        y += h * func(y, i)

    return y


def f(y: float, b: float) -> float:
    return y


t_init: float = 0.0
t_finl: float = 1.0
y_init: float = 1.0
n: int = int(input("n (steps): "))
t: NDArray = linspace(t_init, t_finl, n)

y_euler: float = euler(f, y_init, t)
print("Euler: \t %.16f"%(y_euler))
