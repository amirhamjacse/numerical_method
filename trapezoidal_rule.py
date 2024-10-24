import math

# Define the function to integrate
def f(x):
    return math.sin(x)

# Limits of integration
a = 0           # lower limit
b = math.pi     # upper limit
n = 100         # number of trapezoids (subdivisions)

# Step size
h = (b - a) / n

# Initialize the result with the first and last terms of the formula
integral = (f(a) + f(b)) / 2.0

# Sum the values at the interior points
for i in range(1, n):
    x = a + i * h
    integral += f(x)

# Multiply by the step size to get the final integral value
integral *= h

# Output the result
print(f"Approximate integral of sin(x) from 0 to pi: {integral}")
