import math

# Define the function to integrate
def f(x):
    return math.sin(x)

# Limits of integration
a = 0           # lower limit
b = math.pi     # upper limit
n = 100         # number of intervals (must be even)

# Step size
h = (b - a) / n

# Initialize the integral with the first and last terms
integral = f(a) + f(b)

# Apply Simpson's 1/3 rule: sum terms with coefficients 4 and 2
for i in range(1, n):
    x = a + i * h
    if i % 2 == 0:
        integral += 2 * f(x)  # even index
    else:
        integral += 4 * f(x)  # odd index

# Multiply by h/3 to get the final integral value
integral *= h / 3

# Output the result
print(f"Approximate integral of sin(x) from 0 to pi using Simpson's 1/3 rule: {integral}")
