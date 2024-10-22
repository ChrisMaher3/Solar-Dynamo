import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters for stable and unstable solutions
a_stable = 1.0
c_stable = a_stable**2 / 4 - 0.1  # Ensure c < a^2 / 4 for stability
a_unstable = 2.0
c_unstable = 2.0  # Ensure c > a^2 / 4 for instability

# Define the system of differential equations
def system(t, y, a, c):
    B, v = y
    dBdt = -a * B + 2 * B * v
    dvdt = c - B**2 - v**2
    return [dBdt, dvdt]

# Time span for the simulation
t_span = (0, 10)  # Simulate for 10 time units
t_eval = np.linspace(t_span[0], t_span[1], 100)

# Initial conditions for stable and unstable scenarios
initial_conditions_stable = [0.1, a_stable / 2]  # Near fixed points
initial_conditions_unstable = [1.0, a_unstable / 2]  # Away from fixed points

# Solve the system for stable parameters
sol_stable = solve_ivp(system, t_span, initial_conditions_stable, args=(a_stable, c_stable), t_eval=t_eval)

# Solve the system for unstable parameters
sol_unstable = solve_ivp(system, t_span, initial_conditions_unstable, args=(a_unstable, c_unstable), t_eval=t_eval)

# Create a figure for time evolution plots
plt.figure(figsize=(12, 6))

# Plot B(t) and v(t) for stable case
plt.subplot(1, 2, 1)
plt.plot(sol_stable.t, sol_stable.y[0], label='B(t) - Stable', color='blue')
plt.plot(sol_stable.t, sol_stable.y[1], label='v(t) - Stable', color='green')
plt.title('Stable Case: B(t) and v(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Plot B(t) and v(t) for unstable case
plt.subplot(1, 2, 2)
plt.plot(sol_unstable.t, sol_unstable.y[0], label='B(t) - Unstable', color='blue')
plt.plot(sol_unstable.t, sol_unstable.y[1], label='v(t) - Unstable', color='green')
plt.title('Unstable Case: B(t) and v(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

plt.tight_layout()
plt.show()

# Phase Plane Analysis for stable parameters
B_values = np.linspace(-2, 2, 20)
v_values = np.linspace(-2, 2, 20)
B, v = np.meshgrid(B_values, v_values)

# Calculate derivatives for stable parameters
dBdt_stable = -a_stable * B + 2 * B * v
dvdt_stable = c_stable - B**2 - v**2

# Calculate derivatives for unstable parameters
dBdt_unstable = -a_unstable * B + 2 * B * v
dvdt_unstable = c_unstable - B**2 - v**2

# Plot Phase Plane for stable and unstable parameters side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Stable Phase Plane
strm_stable = axs[0].streamplot(B, v, dBdt_stable, dvdt_stable, color=np.sqrt(dBdt_stable**2 + dvdt_stable**2), linewidth=1, density=2, cmap='autumn')
axs[0].set_title('Phase Plane (Stable Parameters)')
axs[0].set_xlabel('B (Magnetic Field)')
axs[0].set_ylabel('v (Plasma Velocity)')
axs[0].axhline(y=a_stable/2, color='b', linestyle='--', label='v = a/2')
axs[0].axvline(x=0, color='g', linestyle='--', label='B = 0')
axs[0].set_xlim(-2, 2)
axs[0].set_ylim(-2, 2)
axs[0].legend()

# Unstable Phase Plane
strm_unstable = axs[1].streamplot(B, v, dBdt_unstable, dvdt_unstable, color=np.sqrt(dBdt_unstable**2 + dvdt_unstable**2), linewidth=1, density=2, cmap='winter')
axs[1].set_title('Phase Plane (Unstable Parameters)')
axs[1].set_xlabel('B (Magnetic Field)')
axs[1].set_ylabel('v (Plasma Velocity)')
axs[1].axhline(y=a_unstable/2, color='b', linestyle='--', label='v = a/2')
axs[1].axvline(x=0, color='g', linestyle='--', label='B = 0')
axs[1].set_xlim(-2, 2)
axs[1].set_ylim(-2, 2)
axs[1].legend()

plt.tight_layout()
plt.show()
