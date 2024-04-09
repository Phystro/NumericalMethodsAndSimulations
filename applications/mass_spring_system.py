
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
from numpy.typing import NDArray


def mass_spring_damper(mass: float,c,k,F,u0,t) -> NDArray:

    def f(u,t) -> NDArray:
        dudt: NDArray = np.zeros(2)
        dudt[0] = u[1]
        dudt[1] = (F(t) - k*u[0] - c*u[1])/mass
        return dudt

    U = spi.odeint(f,u0,t)
    y = U[:,0]

    return y


def F(t: float) -> float:
    return 0


mass: float = 1
c: float = 0
k: float = 1
n: int = 100

t: NDArray = np.linspace(0, 4*np.pi, n)
u0 = [0, 1]

y: NDArray = mass_spring_damper(mass, c, k, F, u0, t)
plt.plot(t, y)
plt.grid(True)
plt.show()
