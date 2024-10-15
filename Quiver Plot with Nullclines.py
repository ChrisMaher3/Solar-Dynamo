import numpy as np
import matplotlib.pyplot as plt

a = 2.0
c = 1.0

def f(B, v):
    return -a * B + 2 * B * v

def g(B, v):
    return c - B**2 - v**2

B_values = np.linspace(-np.sqrt(c), np.sqrt(c), 400)

v_B_nullcline = a / 2 * np.ones_like(B_values) 
v_v_nullcline_pos = np.sqrt(c - B_values**2)   
v_v_nullcline_neg = -np.sqrt(c - B_values**2)  

B_grid_values = np.linspace(-2, 2, 21)
v_grid_values = np.linspace(-2, 2, 21)
B_grid, v_grid = np.meshgrid(B_grid_values, v_grid_values)

dB_dt = f(B_grid, v_grid)
dv_dt = g(B_grid, v_grid)

plt.figure(figsize=(8, 8))


plt.axvline(0, color='r', linestyle='--', label='B-nullcline')
plt.axhline(a / 2, color='r', linestyle='--')
plt.plot(B_values, v_v_nullcline_pos, 'g-', label="v-nullcline")
plt.plot(B_values, v_v_nullcline_neg, 'g-') 

fixed_points = [(0, np.sqrt(c)), (0, -np.sqrt(c))]
if c > a**2 / 4:
    fixed_points.extend([(np.sqrt(c - a**2 / 4), a / 2), (-np.sqrt(c - a**2 / 4), a / 2)])

for i, point in enumerate(fixed_points):
    if i == 0:
        plt.plot(point[0], point[1], 'C1o', markersize=8, label="Fixed Points")
    else:
        plt.plot(point[0], point[1], 'C1o', markersize=8)


plt.streamplot(B_grid, v_grid, dB_dt, dv_dt, color='C7', density=1.2)


plt.xlabel("B (Magnetic field)")
plt.ylabel("v (Plasma velocity)")


plt.legend(loc="upper right")
plt.savefig("a=2,c=1.svg", bbox_inches='tight')
plt.show()

