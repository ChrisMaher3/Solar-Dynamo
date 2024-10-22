import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 0.5
c = 1.5

# Define the system of differential equations
def system(t, y):
    B, v = y
    dB_dt = -a * B + 2 * B * v  # dB/dt
    dv_dt = c - B**2 - v**2      # dv/dt
    return [dB_dt, dv_dt]

# Time span for the integration
t_span = (0, 20)  # Shorter time to avoid blow-up
t_eval = np.linspace(0, 20, 1000)  # Evaluation points for plotting

# Initial conditions near the fixed points for exploration
initial_conditions = [
    (0.1, np.sqrt(c)),  # Near stable point (0, sqrt(c))
    (0.1, -np.sqrt(c)), # Near stable point (0, -sqrt(c))
    (np.sqrt(c - a**2 / 4) + 0.1, a / 2), # Near saddle point (sqrt(c - a^2 / 4), a / 2)
    (-np.sqrt(c - a**2 / 4) + 0.1, a / 2) # Near saddle point (-sqrt(c - a^2 / 4), a / 2)
]

# Solving the system for each initial condition with a stiffer method
solutions = []
for init_cond in initial_conditions:
    sol = solve_ivp(system, t_span, init_cond, t_eval=t_eval, method='LSODA')  # Use stiff solver
    solutions.append(sol)

# Plot B(t) and v(t) for each initial condition
plt.figure(figsize=(12, 6))

# Plot B(t) (Magnetic Field over time)
plt.subplot(1, 2, 1)
for i, sol in enumerate(solutions):
    plt.plot(sol.t, sol.y[0], label=f"Initial B={initial_conditions[i][0]:.2f}, v={initial_conditions[i][1]:.2f}")
plt.title("B(t) - Magnetic Field Evolution")
plt.xlabel("Time (t)")
plt.ylabel("B(t)")
plt.grid(True)

# Plot v(t) (Plasma velocity over time)
plt.subplot(1, 2, 2)
for i, sol in enumerate(solutions):
    plt.plot(sol.t, sol.y[1], label=f"Initial B={initial_conditions[i][0]:.2f}, v={initial_conditions[i][1]:.2f}")
plt.title("v(t) - Plasma Velocity Evolution")
plt.xlabel("Time (t)")
plt.ylabel("v(t)")
plt.grid(True)

plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Phase plane plot with trajectories
plt.figure(figsize=(8, 8))

# Create nullclines
B_values = np.linspace(-np.sqrt(c), np.sqrt(c), 400)
v_B_nullcline = a / 2 * np.ones_like(B_values)
v_v_nullcline_pos = np.sqrt(c - B_values**2)
v_v_nullcline_neg = -np.sqrt(c - B_values**2)

# Plot the nullclines
plt.axvline(0, color='r', linestyle='--', label='B-nullcline')
plt.axhline(a / 2, color='r', linestyle='--', label=None)
plt.plot(B_values, v_v_nullcline_pos, 'g-', label="v-nullcline")
plt.plot(B_values, v_v_nullcline_neg, 'g-', label=None)  # Negative branch of v-nullcline

# Plot fixed points
fixed_points = [(0, np.sqrt(c)), (0, -np.sqrt(c))]
if c > a**2 / 4:
    fixed_points.extend([(np.sqrt(c - a**2 / 4), a / 2), (-np.sqrt(c - a**2 / 4), a / 2)])

for i, point in enumerate(fixed_points):
    plt.plot(point[0], point[1], 'C1o', markersize=8, label="Fixed Points" if i == 0 else None)

# Plot the phase trajectories
for sol in solutions:
    plt.plot(sol.y[0], sol.y[1], label="Phase Trajectory")

# Labels and title
plt.xlabel("B (Magnetic field)")
plt.ylabel("v (Plasma velocity)")
plt.title("Phase Plane with Nullclines and Trajectories")
plt.grid(True)
plt.legend(loc="upper right")
plt.show()
