import numpy as np
import matplotlib.pyplot as plt

a = 0.5
c = 1.5

B_values = np.linspace(-np.sqrt(c), np.sqrt(c), 400)

v_B_nullcline = a / 2 * np.ones_like(B_values)  
v_v_nullcline_pos = np.sqrt(c - B_values**2)    
v_v_nullcline_neg = -np.sqrt(c - B_values**2)  

plt.figure(figsize=(8, 8))

plt.axvline(0, color='r', linestyle='--', label='B-nullcline')
plt.axhline(a/2, color='r', linestyle='--')


plt.plot(B_values, v_v_nullcline_pos, 'g-', label="v-nullcline")
plt.plot(B_values, v_v_nullcline_neg, 'g-', label=None)  


plt.xlabel("B (Magnetic field)")
plt.ylabel("v (Plasma velocity)")

fixed_points = [(0, np.sqrt(c)), (0, -np.sqrt(c))]
if c > a**2 / 4:
    fixed_points.extend([(np.sqrt(c - a**2 / 4), a / 2), (-np.sqrt(c - a**2 / 4), a / 2)])

for i, point in enumerate(fixed_points):
    if i == 0:
        plt.plot(point[0], point[1], 'C1o', markersize=8, label="Fixed Points")
    else:
        plt.plot(point[0], point[1], 'C1o', markersize=8)




plt.legend(loc="upper right")
#plt.savefig("a=0.5,c=1.5.svg", bbox_inches='tight')
plt.show()
