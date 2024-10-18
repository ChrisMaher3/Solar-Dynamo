import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the functions f(x, y) and g(x, y)
def f(x, y):
    return x**2 + x*y - 2*x

def g(x, y):
    return x*y**2 + 3*y

# Create a grid of x and y values
x_min, x_max = -5, 5
y_min, y_max = -5, 5
x_values = np.linspace(x_min, x_max, 400)
y_values = np.linspace(y_min, y_max, 400)
X, Y = np.meshgrid(x_values, y_values)

# Compute dx/dt and dy/dt on the grid
DX = f(X, Y)
DY = g(X, Y)

# Normalize the arrows for better visualization
M = np.hypot(DX, DY)
M[M == 0] = 1  # Avoid division by zero
DX_norm = DX / M
DY_norm = DY / M

# Plot the nullclines
plt.figure(figsize=(10, 8))

# Plot the nullclines from f(x, y) = 0
# Nullcline x = 0
plt.axvline(x=0, color='blue', linestyle='--', label='f(x, y) = 0 (x = 0)')

# Nullcline y = -x + 2
plt.plot(x_values, -x_values + 2, color='blue', linestyle='-', label='f(x, y) = 0 (y = -x + 2)')

# Plot the nullclines from g(x, y) = 0
# Nullcline y = 0
plt.axhline(y=0, color='red', linestyle='--', label='g(x, y) = 0 (y = 0)')

# Nullcline x*y = -3 => y = -3 / x
# Be careful with x = 0 to avoid division by zero
x_nonzero = x_values[x_values != 0]  # Exclude x = 0
plt.plot(x_nonzero, -3 / x_nonzero, color='red', linestyle='-', label='g(x, y) = 0 (x y = -3)')

# Plot the fixed points
fixed_points = [(0, 0), (2, 0), (3, -1), (-1, 3)]
for point in fixed_points:
    plt.plot(point[0], point[1], 'ko', markersize=8)
    plt.text(point[0] + 0.2, point[1] + 0.2, f'({point[0]}, {point[1]})')

# Plot the quiver plot
# Reduce the density of arrows for clarity
skip = (slice(None, None, 15), slice(None, None, 15))
plt.quiver(X[skip], Y[skip], DX_norm[skip], DY_norm[skip], color='gray')

# Set plot limits and labels
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nullclines and Vector Field of the System')
plt.legend(loc='upper right')
plt.grid(True)

# Save the figure
plt.savefig('nullclines_vector_field.png', dpi=300)
plt.show()
