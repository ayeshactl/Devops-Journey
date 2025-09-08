"""
3️⃣ elif Statement:
The elif (else if) statement lets you check multiple conditions in order.

Syntax:

if condition1:
    # Code if condition1 True
elif condition2:
    # Code if condition2 True
else:
    # Code if none of the above are True

"""
#EX-1
x = 6
if x > 15:
    print("x is less the 15")
elif x > 4:
    print("x is greater than 4 bt not less than 4")
else:
    print("x is 4 or greater than 4 ")    


#EX-2
grade = 66

if grade >= 90:
    print("Grade is A")
elif grade >=75:
    print("Grade is B")
elif grade >=50:
    print("Grade is C")
else:
    print("Grade is D")