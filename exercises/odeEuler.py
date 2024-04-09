from typing import Callable

from numpy.typing import NDArray


def odeEuler(func: Callable, t_values: NDArray, y_init: float) -> float:
    y: float = y_init
    h: float = t_values[1] - t_values[0]


    return y


