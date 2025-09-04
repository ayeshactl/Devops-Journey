import random                   # random is library

secret_number =random.randint(1,20)  #random se randint ko bolo no. choose krne then wo secret m store hoga..

print("welcome to the number guessing game ")
print("Guess a number between 1-20")


for attempt in range (1,4):  
    guess = int(input(f"attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! you guess right")
        break
    elif guess < secret_number:
        print ("too low! try again") 
    else:
        print ("too high! try again") 


else:
   print (f" Sorry! the number was {secret_number}")     #f"..." → Python ko batata hai: curly braces ke andar variable evaluate karo. 