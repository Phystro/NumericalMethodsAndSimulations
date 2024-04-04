from math import exp
from timeit import default_timer as timer
from typing import Callable


def rectangular(f: Callable, a: float, b: float, n:int) -> float:
    """Function that implements the rectangular approximation algorithm
    Returns the value of the integral (float)
    """
    h: float = float(b - a) / n
    result: float = 0

    for i in range(n):
        result = result + f(a + i * h)

    result = result * h
    return result


def trapezoid(f: Callable, a: float, b: float, n: int) -> float:
    """Function that implements the trapezoid approximation algorithm
    """
    h: float = float(b - a) / n
    result: float = (0.5 * f(a)) + (0.5 * f(b))

    for i in range(1, n):
        result += f(a +  i*h)

    result *= h
    return result


def simpsons(f: Callable, a: float, b: float, n: int) -> float:
    """
    Function the implements simpsons approximation algorithm
    a: interval start
    b: interval end
    n: number of steps
    return: numerical integral evaluation
    """
    h: float = float(b - a) / n
    result: float = f(a) + f(b)

    evensum: float = 0
    oddsum: float = 0

    for i in range(1, n):
        if i % 2 == 0:
            # is even
            evensum += f(a + i*h)
        else:
            # is odd
            oddsum += f(a + i*h)

    # for i in range(1, n, 2):
    #     oddsum += f(a + i*h)
    #
    # for i in range(2, n, 2):
    #     evensum += f(a + i*h)

    result += 4*oddsum + 2*evensum
    result *= h/3

    return result


def v(t: float) -> float:
    """Function f(x) to be integrated"""
    return 3*(t**2)*exp(t**3)

a: float = 0.0
b: float = 1.0
n: int = int(input("n (slices): "))

start_time: float = timer()
rectangular_integral: float = rectangular(v, a, b, n)
rec_end_time: float = timer() - start_time

start_time: float = timer()
trapezoid_integral: float = trapezoid(v, a, b, n)
tra_end_time: float = timer() - start_time

start_time: float = timer()
simpson_integral: float = simpsons(v, a, b, n)
sim_end_time: float =timer() - start_time

print("\nRectangular Integral \t = %.16f"%(rectangular_integral))
print("Trapezoid Integral \t = %.16f"%(trapezoid_integral))
print("Simpson Integral \t = %.16f"%(simpson_integral))

print("""\nExecution Time:
Rectangular: \t %.6f s
Trapezoid: \t %.6f s
Simpson: \t %.6f s"""%(rec_end_time, tra_end_time, sim_end_time))
