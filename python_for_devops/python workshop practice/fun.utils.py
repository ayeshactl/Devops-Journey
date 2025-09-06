
## FUNCTION SYNTAX
def function_name(parameters):
    """
    Optional docstring: function kya karta hai
    """
    # function body (statements)
    return value   # optional
###################################


import os
import datetime

def run_command(command):           # defining a function
   return os.system(command)        # print ke jagah return bi likh skte.. and print ka bracket remove bi kr skte..

def run_command(command):          # defining a function
    print(os.system(command))

def run_command(command):           # defining a function
    print(os.system(command))

def show_date():             #define bi kiya
    return datetime.datetime.today()



# ---- function calls ----
run_command("uptime")    # system uptime / load avg
run_command("date")     # current date/time
run_command("free -h")   # memory usage

today = show_date()
print(today)           #call bi kiya..