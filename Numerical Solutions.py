import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 0.5
c = 1.5

def system(t, y):
    B, v = y
    dB_dt = -a * B + 2 * B * v  
    dv_dt = c - B**2 - v**2     
    return [dB_dt, dv_dt]

t_span = (0, 50)  
t_eval = np.linspace(0, 50, 1000)  


initial_conditions = [
    (0.1, np.sqrt(c)),  
    (0.1, -np.sqrt(c)), 
    (np.sqrt(c - a**2 / 4) + 0.1, a / 2), 
    (-np.sqrt(c - a**2 / 4) + 0.1, a / 2) 
]


solutions = []
for init_cond in initial_conditions:
    sol = solve_ivp(system, t_span, init_cond, t_eval=t_eval, method='RK45')
    solutions.append(sol)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
for i, sol in enumerate(solutions):
    plt.plot(sol.t, sol.y[0], label=f"Initial B={initial_conditions[i][0]:.2f}, v={initial_conditions[i][1]:.2f}")
plt.title("B(t) - Magnetic Field Evolution")
plt.xlabel("Time (t)")
plt.ylabel("B(t)")


plt.subplot(1, 2, 2)
for i, sol in enumerate(solutions):
    plt.plot(sol.t, sol.y[1], label=f"Initial B={initial_conditions[i][0]:.2f}, v={initial_conditions[i][1]:.2f}")
plt.title("v(t) - Plasma Velocity Evolution")
plt.xlabel("Time (t)")
plt.ylabel("v(t)")


plt.legend(loc='best')
plt.tight_layout()
plt.show()

