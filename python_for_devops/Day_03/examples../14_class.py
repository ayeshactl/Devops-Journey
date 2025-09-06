#Use: Define a class (OOP)

class Person:
    def __init__(self, name):
        self.name = name
p = Person("Alice")
print(p.name)


# 15 Use: Import module

import math
print(math.sqrt(16))  # 4.0

# 16 Use: Import specific part of a module
from math import sqrt
print(sqrt(25))  # 5.0


# 17 Use: Alias for a module
import math as m
print(m.sqrt(36))  # 6.0

# 18 Use: Boolean value True
x = True
print(x)  # True


# 19 Use: Boolean value False
x = False
print(x)  # False

# 20 Use: Represents null / no value
x = None
print(x)  # None


# 21 Use: Identity comparison (same object in memory)
a = [1,2]
b = a
print(a is b)  # True

# 22 Use: Small anonymous function
square = lambda x: x**2
print(square(5))  # 25

# 23 Use: Context manager for files, resources
with open("file.txt", "w") as f:
    f.write("Hello")
