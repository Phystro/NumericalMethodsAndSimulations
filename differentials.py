from math import exp
from typing import Callable


def euler1(func: Callable, y_init: float, t_init: float, t_finl: float, n: int) -> float:
    """
    Computes the approximation of the initial value ODE problems.

    :param func: callable function representing the first order differential equation;
    :param y_init: initial value of the dependent variable y(t) at time t = 0 i.e. y(t = 0);
    :param t_init: initial value of independent variable, usually time, t;
    :param t_finl: final value of the independent variable;
    :param n: compute iterations. Number of steps to take between the initial and final independent variables;
    :return: float of the approximate value of the function at point b
    """
    # step size
    h: float = (t_finl - t_init) / n
    t: float = t_init
    y: float = y_init

    while t < t_finl:
        y += h * func(t, y)
        t += h

    return y


def rk4(func: Callable, y_init: float, t_init: float, t_finl: float, n: int) -> float:
    """
    Implements the fourth-order Runge-Kutta (RK4) to solve first order ordinary differential equations.

    :param func: callable function representing the first order differential equation;
    :param y_init: initial value of the dependent variable y(t) at time t = 0 i.e. y(t = 0);
    :param t_init: initial value of independent variable, usually time, t;
    :param t_finl: final value of the independent variable;
    :param n: compute iterations. Number of steps to take between the initial and final independent variables;
    :return: float of the approximate value of the function at point t
    """

    h: float = (t_finl - t_init) / n
    t: float = t_init
    y: float = y_init

    while t < t_finl:
        # calculate the intermediate values
        k1 = func(t, y)
        k2 = func(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = func(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = func(t + h, y + h * k3)

        y += ( (h/6) * (k1 + (2*k2) + (2*k3) + k4) )
        t += h

    return y


def f(b: float, y: float) -> float:
    """
    Function under consideration i.e. F(b, y) = y' = e**t
    """
    return y



t_init = 0.0
t_finl = 1.0
y_init = 1.0
n: int = int(input("n (steps): "))


y_euler = euler1(f, y_init, t_init, t_finl, n)
y_rk4 = rk4(f, y_init, t_init, t_finl, n)
# print(euler2(f, y, a, b, 10))
y_exact = exp(t_finl)
print(" Euler: \t %.16f \n RK4: \t\t %.16f \n Exact: \t %.16f \n"%(y_euler, y_rk4, y_exact))

