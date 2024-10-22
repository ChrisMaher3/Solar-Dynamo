import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a_stable = 0.5
c_stable = 0.25  # c < a^2 / 4
a_unstable = 2.0
c_unstable = 2.0  # c > a^2 / 4

def system(t, y, a, c):
    B, v = y
    dBdt = -a * B + 2 * B * v
    dvdt = c - B**2 - v**2
    return [dBdt, dvdt]

initial_conditions_stable = [0.1, a_stable / 2]  
initial_conditions_unstable = [1.0, a_unstable / 2]  

t_span = (0, 10)  
t_eval = np.linspace(t_span[0], t_span[1], 100)

sol_stable = solve_ivp(system, t_span, initial_conditions_stable, args=(a_stable, c_stable), t_eval=t_eval)

sol_unstable = solve_ivp(system, t_span, initial_conditions_unstable, args=(a_unstable, c_unstable), t_eval=t_eval)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(sol_stable.t, sol_stable.y[0], 'b--', label='B(t) - Stable')
plt.plot(sol_stable.t, sol_stable.y[1], 'g--', label='v(t) - Stable')
plt.title('Stable Case: B(t) and v(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Plot B(t) and v(t) for unstable case
plt.subplot(1, 2, 2)
plt.plot(sol_unstable.t, sol_unstable.y[0], 'b--', label='B(t) - Unstable')
plt.plot(sol_unstable.t, sol_unstable.y[1], 'g--', label='v(t) - Unstable')
plt.title('Unstable Case: B(t) and v(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.savefig("stable and unstable.svg", bbox_inches='tight')
plt.show()





