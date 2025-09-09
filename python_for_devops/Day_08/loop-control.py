"""
3️⃣ Loop Control Statements:

break → exit the loop immediately
continue → skip current iteration, continue next
pass → do nothing (placeholde

"""

#Examples:
# break
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0 1 3 4

# pass
for i in range(3):
    if i == 1:
        pass
    print(i)  # Output: 0 1 2


#EX-
for i in range(1, 11):  # numbers from 1 to 10
    if i == 7:            # check if i is 7
        print("The loop is stopped at 7")
        break             # exit the loop
    print(i)              # print numbers before 7