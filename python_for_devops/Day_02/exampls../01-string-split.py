

"""
n Python, split() is a string method that breaks a string into a list using a separator (default = whitespace). ✅
"""


# default: split by spaces
"Hello world Python".split()
# ['Hello', 'world', 'Python']

# split by comma
"apple,banana,grape".split(",")
# ['apple', 'banana', 'grape']

# split with limit
"one-two-three".split("-", 1)
# ['one', 'two-three']
   


text = "Python is awesome"
words = text.split()         #split() → breaks into list   ->>>  # ['Python', 'is', 'awesome']
del words [2]            # pop(index) (or del words[index]) → removes by index
print("Words:", words)