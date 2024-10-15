import numpy as np
import matplotlib.pyplot as plt

a = 1.0
c = 1.5

B_values = np.linspace(-np.sqrt(c), np.sqrt(c), 400)

v_B_nullcline = a / 2 * np.ones_like(B_values)  
v_v_nullcline_pos = np.sqrt(c - B_values**2)    
v_v_nullcline_neg = -np.sqrt(c - B_values**2)  

plt.figure(figsize=(8, 8))

plt.axvline(0, color='r', linestyle='-', label='B-nullcline')
plt.axhline(a/2, color='r', linestyle='-')


plt.plot(B_values, v_v_nullcline_pos, 'g-', label="v-nullcline (dv/dt = 0)")
plt.plot(B_values, v_v_nullcline_neg, 'g-', label=None)  


plt.xlabel("B (Magnetic field)")
plt.ylabel("v (Plasma velocity)")


plt.legend(loc="upper right")

plt.show()
