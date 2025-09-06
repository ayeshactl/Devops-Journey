# Use: Declare a global variable inside function


x = 5
def change():
    global x
    x = 10
change()
print(x)  # 10
