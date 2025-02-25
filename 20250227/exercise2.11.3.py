#Part 1
# Radius is in centimeters
radius = 5  # Assigning the radius of the sphere in centimeters

# Formula for the volume of a sphere: V = (4/3) * pi * radius^3
import math  # Importing the math module to access pi

# Calculating the volume
volume = (4/3) * math.pi * radius**3  # Volume is in cubic centimeters

# Display the result
print("The volume of the sphere is", volume, "cubic centimeters.")

#Part 2
import math  # Import the math module to use cosine and sine

# Assign the value of x
x = 42  # x is in radians

# Compute the sine and cosine of x
cos_x = math.cos(x)
sin_x = math.sin(x)

# Compute the sum of their squared values
result = cos_x**2 + sin_x**2

# Display the result
print("cos(x)^2 + sin(x)^2 =", result)

#part3
import math

# Method 1: Using math.e and exponentiation operator (**)
result1 = math.e ** 2

# Method 2: Using math.pow
result2 = math.pow(math.e, 2)

# Method 3: Using math.exp
result3 = math.exp(2)

# Printing the results
print("Using ** operator:", result1)
print("Using math.pow:", result2)
print("Using math.exp:", result3)
