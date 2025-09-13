# main.py
import math_utils

print(math_utils.add(5, 3))      # 8
print(math_utils.multiply(4, 2)) # 8


#Example 2: Import Specific Functions
from math_utils import add

print(add(10, 20))  # 30


#Example 3: using Alias

import math_utils as mu
print(mu.add(2,3))

#Example 4: Built-in Modules
import math 
import random

print(math.sqrt(4))        #2.0
print(random.randint(1,20))  #any no. from 1-20




'''
📌 Summary

Module = Python file
import keyword se use karte hain
Built-in modules (math, random, os, sys, etc.) bhi hote hain
'''
