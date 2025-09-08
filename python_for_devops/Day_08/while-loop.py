"""
2️⃣ While Loop:
Definition: Repeats code while a condition is True.

Syntax:
while condition:
    # code block

"""
#EX_1 (Python basics):
count = 0
while count < 3:
    print(count)
    count += 1
# Output: 0 1 2


#DevOps Use-case:
#EX-2
import time
retry = 0
while retry < 3:
    print("Trying to connect...")
    retry += 1
    time.sleep(1)
# Retries connection 3 times

""""
5️⃣ While Loop DevOps Use-cases:

Retrying failed tasks
Monitoring services/resources
Waiting for a process to complete

    """
#Ex-3
status = "down"
while status != "up":
    print("Service not up yet, checking again...")
    status = "up"  # simulate service recovery

#Ex-4
count = 5
while count >= 1:
    print(count)
    count -= 1  # decrease by 1 each time
