import numpy as np
import matplotlib.pyplot as plt

a = 0.5
c = 1.5

def f(B, v):
    return -a * B + 2 * B * v

def g(B, v):
    return c - B**2 - v**2

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

def jacobian(B, v):
    df_dB = -a + 2 * v
    df_dv = 2 * B
    dg_dB = -2 * B
    dg_dv = -2 * v
    return np.array([[df_dB, df_dv], [dg_dB, dg_dv]])
for point in fixed_points:
    B_fp, v_fp = point
    J = jacobian(B_fp, v_fp)
    det_J = np.linalg.det(J)
    trace_J = np.trace(J)
    
    print(f"Fixed point at (B, v) = ({B_fp}, {v_fp})")
    print(f"Determinant of Jacobian: {det_J}")
    print(f"Trace of Jacobian: {trace_J}")
    if det_J > 0 and trace_J < 0:
        print("Stable node\n")
    elif det_J > 0 and trace_J > 0:
        print("Unstable node\n")
    elif det_J < 0:
        print("Saddle point\n")




plt.legend(loc="upper right")
#plt.savefig("a=0.5,c=1.5.svg", bbox_inches='tight')
plt.show()
