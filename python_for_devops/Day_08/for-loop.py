"""
1️⃣ For Loop

Definition: Repeats code for each item in a sequence.

Syntax:
for item in sequence:
    # code block

"""
#Ex-1 (Python basics):
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry



#DevOps Use-case:
#EX-2
servers = ["web1", "web2", "db1"]
for s in servers:
    print(f"Checking status of {s}")
# Automates server status check

"""
4️⃣ For Loop DevOps Use-cases:

Automating tasks on multiple servers
Batch file operations
Parsing log files
Deploying updates

"""

#Ex-3
files = ["app.log", "error.log"]
for f in files:
    print(f"Archiving {f}")


#EX-4
for i in range(1,21):
  if i % 2 == 0:
      print(f"Even numbers are: {i}")