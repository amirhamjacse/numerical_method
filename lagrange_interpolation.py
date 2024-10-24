# Known data points
x_points = [0, 1, 2]
y_points = [1, 3, 2]

# Point to estimate
x_to_estimate = 1.5

# Step-by-step calculation of the Lagrange Interpolating Polynomial

# Number of points
n = len(x_points)

# Initialize the result to 0
result = 0.0

# Loop over each point to calculate the interpolation
for i in range(n):
    # Start with y_i
    term = y_points[i]
    
    # Multiply by the Lagrange basis polynomial for the current i
    for j in range(n):
        if i != j:
            term *= (x_to_estimate - x_points[j]) / (x_points[i] - x_points[j])
    
    # Add the term to the result
    result += term

# Output the result
print(f"Estimated value at x = {x_to_estimate}: {result}")
