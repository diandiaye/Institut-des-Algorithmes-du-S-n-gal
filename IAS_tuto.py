
## 1. Import necessary libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 2. Define total population, N.
N = 1000
# 3. Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# 4. Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# 5. Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 
# 6. A grid of time points (in days)
t = np.linspace(0, 160, 160)

# 7. The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# 8. Initial conditions vector
y0 = S0, I0, R0
# 9. Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T
# 10. Afficher les résultats
print(S)
print(I)
print(R)
