
# __init__.py
# Purpose: Is file ka role hai package ke andar se modules ko expose karna.
# Connection: module1.py aur module2.py ke functions ko direct package ke through import karne ka option deta hai.
# Eg: from my_package_demo.my_package import greet, add, multiply

from .module1 import greet
from .module2 import add, multiply
