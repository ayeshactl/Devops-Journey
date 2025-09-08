# ===============================
# DAY-06: Python Operators Practice
# ===============================

print("===== Arithmetic Operators =====")
a = 15
b = 4
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print("\n===== Assignment Operators =====")
x = 10
print("Initial x =", x)
x += 5
print("x += 5 ->", x)
x *= 2
print("x *= 2 ->", x)
x -= 4
print("x -= 4 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 3
print("x %= 3 ->", x)
x **= 2
print("x **= 2 ->", x)

print("\n===== Bitwise Operators =====")
p = 6   # 110 in binary
q = 3   # 011 in binary
print("p & q =", p & q)
print("p | q =", p | q)
print("p ^ q =", p ^ q)
print("~p =", ~p)
print("p << 1 =", p << 1)
print("p >> 1 =", p >> 1)

print("\n===== Logical Operators =====")
a = True
b = False
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)

print("\n===== Identity Operators =====")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2 ->", list1 is list2)
print("list1 is list3 ->", list1 is list3)
print("list1 is not list3 ->", list1 is not list3)

print("\n===== Membership Operators =====")
print("2 in list1 ->", 2 in list1)
print("5 not in list1 ->", 5 not in list1)

print("\n===== Relational Operators =====")
a = 10
b = 20
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b ->", a > b)
print("a < b ->", a < b)
print("a >= b ->", a >= b)
print("a <= b ->", a <= b)

print("\n===== Operator Precedence =====")
x = 5 + 3 * 2 ** 2  # 5 + 3*4 = 17
print("5 + 3 * 2 ** 2 =", x)

print("\n===== Bonus Challenge =====")
# Small calculator using arithmetic operators
num1 = 8
num2 = 3
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
