from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


def f(y: float, t: float) -> float:
    return 2*(1 - y) - np.exp(-4*t)


def euler(func: Callable, y_init: float, t_init: float, t_finl: float,  n: int) -> NDArray:
    h: float = (t_finl - t_init) / n
    y: NDArray = np.zeros(n)
    y[0] = y_init

    for i in range(0, n-1):
        y[i + 1] = y[i] + func( y[i], t[i] ) * h

    return y


def rk4(func: Callable, y_init: float, t_init: float, t_finl: float, n: int) -> NDArray:
    h: float = (t_finl - t_init) / n
    y: NDArray = np.zeros(n)
    y[0] = y_init

    for i in range(0, n-1):
        k1: float = func(y[i], t[i])
        k2: float =func(y[i] + 0.5 * h * k1, t[i] + 0.5  * h)
        k3: float = func(y[i] + 0.5 * h * k2, t[i] + 0.5 * h)
        k4: float = func(y[i] + h*k3, t[i] + h)
        y[i+1] = y[i] + ( (h/6) * (k1 + (2*k2) + (2*k3) + k4 ) )

    return y


y_init: float = 1

t_init: float = 0
t_finl: float = 2

# Independent variable discretization
n: int = 21
t = np.linspace(t_init, t_finl, n)
# step size calculation
h: float = t[2] - t[1]


y_euler: NDArray = euler(f, y_init, t_init, t_finl, n)
y_rk4: NDArray = rk4(f, y_init, t_init, t_finl, n)


# Analytical solution
t_ana: NDArray = np.linspace(t_init, t_finl, 51)
y_ana: NDArray = 1 / (2*np.exp(4*t_ana)) + 1 - 1 / (2*np.exp(2*t_ana))


#### Plotting
plt.figure(num=1, dpi=150, figsize=(7, 5))
plt.rcParams["font.family"] = "serif"
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.facecolor']='white'
plt.plot(t_ana,y_ana,'ro',label = "Analytical Solution",markersize=2.5)
plt.plot(t,euler(f, y_init, t_init, t_finl, n),'b-', label = "Euler")
plt.plot(t,rk4(f, y_init, t_init, t_finl, n),'k-', label = "Runge Kutta")
plt.legend(loc=4)
plt.grid(True, color='lightgray')
plt.xlabel("$t$ (-)")
plt.ylabel("$y$ (-)")
plt.ylim([0.75,1])
plt.text(s='Euler\'s Method Vs. Runge Kutta 4th Order Method', x=1, y=1.03, fontsize=15, ha='center', va='center')
plt.text(s=f'n = {n}, h = {h:.3f}', x=1, y=1.01, fontsize=11, ha='center', va='center')
plt.savefig('euler_rk_output.png', transparent=False, bbox_inches="tight")
plt.show()
