import numpy as np

# Define the Jacobian matrix functions
def jacobian(x, y):
    # Compute partial derivatives
    df_dx = 2 * x + y - 2
    df_dy = x
    dg_dx = y**2
    dg_dy = 2 * x * y + 3
    # Form the Jacobian matrix
    J = np.array([[df_dx, df_dy],
                  [dg_dx, dg_dy]])
    return J

# Fixed points
fixed_points = [(0, 0), (2, 0), (3, -1), (-1, 3)]

print("Fixed Point Analysis:")
for idx, (x_fp, y_fp) in enumerate(fixed_points, 1):
    J = jacobian(x_fp, y_fp)
    delta = np.linalg.det(J)
    tau = np.trace(J)
    # Compute discriminant
    discriminant = tau**2 - 4 * delta
    print(f"\nFixed Point {idx}: ({x_fp}, {y_fp})")
    print(f"Jacobian Matrix:\n{J}")
    print(f"Determinant (Δ): {delta}")
    print(f"Trace (τ): {tau}")
    print(f"Discriminant (τ^2 - 4Δ): {discriminant}")
    # Classify the fixed point
    if delta < 0:
        print("Type: Saddle Point")
    elif delta > 0:
        if discriminant > 0:
            if tau > 0:
                print("Type: Unstable Node (source)")
            else:
                print("Type: Stable Node (sink)")
        elif discriminant < 0:
            if tau > 0:
                print("Type: Unstable Focus (spiral source)")
            else:
                print("Type: Stable Focus (spiral sink)")
        else:
            print("Type: Improper Node (further analysis required)")
    else:
        print("Type: Non-hyperbolic (further analysis required)")
