import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system of differential equations
def system(t, y, a, c):
    B, v = y
    dB_dt = -a * B + 2 * B * v  # dB/dt
    dv_dt = c - B**2 - v**2     # dv/dt
    return [dB_dt, dv_dt]

# Create a phase diagram using streamline plot with cmap
def phase_plot(a, c):
    B_values = np.linspace(-2.5, 2.5, 400)
    v_values = np.linspace(-2.5, 2.5, 400)
    B, v = np.meshgrid(B_values, v_values)
    
    # Compute dB/dt and dv/dt for the grid
    dB_dt = -a * B + 2 * B * v
    dv_dt = c - B**2 - v**2
    
    # Compute the magnitude of velocity (for cmap)
    speed = np.sqrt(dB_dt**2 + dv_dt**2)

    # Plot streamlines and fixed points
    plt.figure(figsize=(10, 8))
    
    # Streamline plot with colormap
    strm = plt.streamplot(B, v, dB_dt, dv_dt, color=speed, cmap='plasma', linewidth=2)

    # Add colorbar
    plt.colorbar(strm.lines)

    # Fixed points
    fixed_points = [(0, np.sqrt(c)), (0, -np.sqrt(c))]
    if c > a**2 / 4:
        fixed_points.extend([(np.sqrt(c - a**2 / 4), a / 2), (-np.sqrt(c - a**2 / 4), a / 2)])
    
    for point in fixed_points:
        plt.plot(point[0], point[1], 'ko', markersize=8, label="Fixed Point")

    # Plot nullclines for dB/dt = 0 and dv/dt = 0
    B_values = np.linspace(-np.sqrt(c), np.sqrt(c), 400)
    #v_v_nullcline_pos = np.sqrt(c - B_values**2)
    #v_v_nullcline_neg = -np.sqrt(c - B_values**2)
    
    #plt.plot(B_values, v_v_nullcline_pos, 'g--', label="v-nullcline")
    #plt.plot(B_values, v_v_nullcline_neg, 'g--')
    #plt.axhline(a / 2, color='r', linestyle='--', label='B-nullcline')
    
    # Labels and title
    plt.xlabel("B (Magnetic field)")
    plt.ylabel("v (Plasma velocity)")
    plt.legend(loc="upper right")
    #plt.savefig(f"phase_diagram_a_{a}_c_{c}.svg", bbox_inches='tight')

    plt.show()

# Plot stability regions for different values of a and c
def plot_stability_regions():
    a_values = np.linspace(0.1, 2, 100)
    c_values_stable = (a_values**2) / 4

    plt.figure(figsize=(8, 6))
    
    # Stable region below the boundary
    plt.fill_between(a_values, c_values_stable, 3, color='lightgreen', alpha=0.5, label="Stable Region")
    
    # Boundary between stable and unstable regions
    plt.plot(a_values, c_values_stable, 'r--', label=r"$c = \frac{a^2}{4}$ (Stability Boundary)")

    plt.xlabel("a (Magnetic field dissipation rate)")
    plt.ylabel("c (Driving of plasma flows)")
    plt.legend(loc="upper left")
    plt.ylim(0, 3)
    plt.xlim(0, 2)
    plt.savefig("stability regions a versus c.svg", bbox_inches='tight')

    plt.show()

# Example values of a and c to explore different behaviors
a_values = [0.5, 1.0, 1.5]  # Varying a
c_values = [1.0, 1.5, 2.0]  # Varying c

# Generate phase plots for different combinations of a and c
for a in a_values:
    for c in c_values:
        phase_plot(a, c)

# Plot the stability regions in the (a, c) parameter space
plot_stability_regions()
