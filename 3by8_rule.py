import math

# Define the function to integrate
def f(x):
    return math.sin(x)

# Limits of integration
a = 0           # lower limit
b = math.pi     # upper limit
n = 99          # number of intervals (must be a multiple of 3)

# Step size
h = (b - a) / n

# Initialize the integral with the first and last terms
integral = f(a) + f(b)

# Apply Simpson's 3/8 rule: sum terms with coefficients 3 and 2
for i in range(1, n):
    x = a + i * h
    if i % 3 == 0:
        integral += 2 * f(x)  # every third point
    else:
        integral += 3 * f(x)  # other points

# Multiply by 3h/8 to get the final integral value
integral *= 3 * h / 8

# Output the result
print(f"Approximate integral of sin(x) from 0 to pi using Simpson's 3/8 rule: {integral}")
