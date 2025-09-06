"""
"In Python, a SUBSTRING simply means: a smaller part of a string.
Python doesn’t have a direct substring() function, but we can get substrings using slicing or string methods.
"""

#🔹 1. Using slicing
text = "Python is amazing"
print(text[0:6])                # 'Python'   (from index 0 to 5)
print(text[6:9])# 'is'



#🔹 2. Using split() and indexing

text = "Python is amazing"
words = text.split()
print(words [0])         # Python
print(words [1])         # is
print(words [2])         # amazing