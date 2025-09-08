"""

5️⃣ Logical Conditions in if:
You can combine multiple conditions using and, or, not.

and → True if both conditions True
or → True if at least one True
not → Reverses True/False

"""
#EX-1
num = 10
if num >= 10 and num <= 20:
  print("number is in the range of 10-20")

  #EX-2
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("yes")
else:
    print("no")
