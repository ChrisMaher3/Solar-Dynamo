import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system of ODEs
def system(t, variables):
    x, y = variables
    dxdt = x**2 + x*y - 2*x
    dydt = x*y**2 + 3*y
    return [dxdt, dydt]

# Time span for integration
t_span = (0, 10)  # From t=0 to t=10
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Evaluation points

# Fixed points and nearby initial conditions
fixed_points = [
    {'fp': (0, 0), 'init': (0.1, 0.1), 'label': 'Near (0, 0)'},
    {'fp': (2, 0), 'init': (1.9, 0.1), 'label': 'Near (2, 0)'},
    {'fp': (3, -1), 'init': (2.9, -1.1), 'label': 'Near (3, -1)'},
    {'fp': (-1, 3), 'init': (-1.1, 2.9), 'label': 'Near (-1, 3)'}
]

# Loop over each initial condition
for idx, point in enumerate(fixed_points, 1):
    x_fp, y_fp = point['fp']
    x0, y0 = point['init']
    label = point['label']
    
    # Solve the system
    sol = solve_ivp(system, t_span, [x0, y0], t_eval=t_eval, method='RK45')
    
    # Extract solutions
    t = sol.t
    x = sol.y[0]
    y = sol.y[1]
    
    # Plot x(t) and y(t)
    plt.figure(figsize=(12, 5))
    
    # Plot x(t)
    plt.subplot(1, 2, 1)
    plt.plot(t, x, label='x(t)')
    plt.xlabel('Time t')
    plt.ylabel('x(t)')
    plt.title(f'Solution x(t) starting near {label}')

    
    # Plot y(t)
    plt.subplot(1, 2, 2)
    plt.plot(t, y, label='y(t)', color='orange')
    plt.xlabel('Time t')
    plt.ylabel('y(t)')
    plt.title(f'Solution y(t) starting near {label}')
    
    
    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(f'solution_{idx}.png', dpi=300)
    plt.show()
