# #Practice 1:
# Q. Write a function welcome() that returns "Welcome to DevOps!" and print it.
# Q. Modify it so it takes no argument but prints inside function instead of returning.

#1
def welcome():
    return "Hi Ayesha"

message = welcome() 

print((message))  

#2
def welcome():
    print("welcome to devops")

welcome()    

# 📌 Difference Explained:
# First version → function returns a string → you can store it in a variable and reuse.
# Second version → function directly prints inside → simpler, but less reusable.


#3 Positional Arguments: Order matters here...
def greet(name, role):
    return f"Hello {name}, you are a {role}"
print (greet("Ayesha", "Devops Engineer"))

#4 Keyword Arguments :Order does not matter...
print(greet(role="DevOps Engineer", name="Ayesha"))

#5 Default Arguments:
##SYNTAX:
'''
def function_name(param1, param2=default_value, param3=default_value, ...):
    # function body
    return something
------------------------------------------------------------------------
 👉 Rule:
Normal (non-default) arguments pehle aate hain
Default arguments baad me aate hain

'''
# EX-1
def greet_user(name, msg = "Welcome to Devops!"):
    print(f"{msg}, {name}")

greet_user("Ayesha")          # Pehle call me msg nahi diya → default "Welcome to Devops!" use hua.
greet_user("Ayesha", "Salam") # Dusre call me "Salam" diya → default overwrite ho gaya.

#EX-2
def server_info(name="Unknown", ip="127.0.0.1", port=80):
    print(f"Server:{name}, IP: {ip}, PORT:{port}")

server_info()               #sab default use honge
server_info("App store")       #sirf name diya, baaki default
server_info("DB-Server", "192.168.1.50", 3306)  #sab custom


#ARGUMENTS

#1️⃣ Normal function bina *args
'''
def add(a, b):
    print(a + b)

add(2, 3)       # ✅ kaam karega
add(2, 3, 4)    # ❌ error: zyada values di hain
'''

#⚠️ Problem: is function me sirf 2 hi arguments le sakte hain.

#2️⃣ Ab *args use karte hain

def add_numbers(*args):
    print("args =", args)  # bas print dekhna
add_numbers(2, 3)
add_numbers(2, 3, 4)
add_numbers(10, 20, 30, 40, 50)

#3️⃣ Ab un numbers ka kaam karwao (sum)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum =", total)

add_numbers(2, 3)               # 5
add_numbers(2, 3, 4)            # 9
add_numbers(10, 20, 30, 40, 50) # 150


#EX 2
def open_ports(server, *ports):
    print(f"Server: {server}")
    print("Opening ports:")
    for port in ports:
        print(port)

open_ports("WebServer", 80, 443)
open_ports("DBServer", 3306, 5432)



##🔹 **kwargs — Keyword Arguments
'''
📌 Meaning:
Agar function me unknown number of keyword arguments pass karne ho → **kwargs use karte hain.
Ye dictionary ke form me saare extra arguments store karta hai.

SYNTAX: **kwargs → key=value pairs
'''

#EX-1
def show_info(**info):
    print(info)
    print(type(info))

show_info(name="Ayesha", role="DevOps Engineer")

#EX-2
def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name="Ayesha", age=20, college="XYZ College")


#🔹 Lambda Functions in Python
'''
📌 What is a Lambda Function?

Lambda function ek chhoti, one-line function hoti hai
Iska name optional hota hai (anonymous function)
Syntax simple aur compact hai
Usually simple operations ke liye use hoti hai

🔹 SYNTAX: lambda arguments: expression

arguments → inputs
expression → single operation, return automatically hota hai
'''


#EX-1: Simple Lambda
add = lambda x, y: x + y
print(add(5,3))


#EX-2 : Lambda without variable
print((lambda x, y: x * y)(4, 5))  # 20   #Yaha humne lambda ko directly call kar diya


#EX-3 :Lambda in list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  #map() → list ke har element pe function apply karta hai
                                               #Lambda → har element ka square nikal raha hai
print(squared)  # [1, 4, 9, 16, 25]


#EX-4 : DevOps Style 
servers = [10, 20, 30]  # server load %
high_load = list(filter(lambda x: x > 15, servers))     #filter() → condition ke basis pe select karta hai
print(high_load)  # [20, 30]
