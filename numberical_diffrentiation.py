x_points = [0, 1, 2, 3, 4]
y_points = [1, 2, 0, 2, 1]  # f(x) values at corresponding x

# Central difference approximation for the derivative
# We'll compute the derivative at each interior point (not endpoints)
derivatives = []

for i in range(1, len(x_points) - 1):
    # Central difference formula
    derivative = (y_points[i + 1] - y_points[i - 1]) / (x_points[i + 1] - x_points[i - 1])
    derivatives.append((x_points[i], derivative))

# Forward difference at the first point
forward_diff = (y_points[1] - y_points[0]) / (x_points[1] - x_points[0])
derivatives.insert(0, (x_points[0], forward_diff))

# Backward difference at the last point
backward_diff = (y_points[-1] - y_points[-2]) / (x_points[-1] - x_points[-2])
derivatives.append((x_points[-1], backward_diff))

# Output the results
print("Numerical Differentiation (Forward, Central, Backward):")
for x, derivative in derivatives:
    print(f"f'({x}) ≈ {derivative}")