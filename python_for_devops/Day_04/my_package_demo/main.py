# main.py
# Purpose: Ye main script hai jo package (my_package) ke functions use karta hai.
# Connection: Ye my_package ke andar ke functions (via __init__.py) ko call karta hai aur output print karta hai.

from my_package_demo.my_package import greet, add, multiply

print(greet("Ayesha"))
print(add(10, 20))
print(multiply(3, 2))




'''
To pura flow hoga:

main.py imports → my_package
my_package → __init__.py check karega
__init__.py → functions ko expose karega jo module1.py aur module2.py me defined hain

'''