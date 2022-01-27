import random

# There are three diffenret number types in Python: int, float and complex.
# Numeric variables are created when you assign a value to them:
intVariable =  1
floatVariable = 2.8
complexVariable = 1j

print(type(intVariable),type(floatVariable),type(complexVariable))

# Float numbers can also be scientific numbers with an "e" to indicate the power of 10.

scientific = 35e3

print(type(scientific))

# Complex numbers are written with a "j" as the imaginary part:

complexNumber = 4j
complexResult = 3+5j
print(type(complexNumber))
print(type(complexResult))
print()
## To convert types, use the
## int(), float() and complex() methods:

intVal  = 1
floatVal  = 2.8
complexVal  = 1j

# Convert from int to float:

floatResult = float(intVal)

# Convert from float to int:
intResult = int(floatVal)

# Convert from int to complex:
complexResult =  complex(intVal)

print(type(floatResult))
print(type(intResult))
print(type(complexResult))
print()
## Random number
print(random.randrange(1,10))
