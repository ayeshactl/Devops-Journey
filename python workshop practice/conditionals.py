day_of_week = input("Enter the day of week: ").lower() #convert lowercase
print(day_of_week)

if day_of_week == "sunday" or day_of_week == "saturday":
   print("I will learn LIVE devops")
else :
   print("I will practice devops")


   num1 = int(input("Enter num one: ")) #str -> int "type casting"
   num2 = int(input("Enter num two: "))

   choice = input ("Enter the operation (option + - * % )")
   if choice == "+":
    sum_of_num = num1 + num2
    print("Addition: ",sum_of_num)
   elif choice == "-":
    diff_of_num = num1 - num2
    print("Subtraction: ",diff_of_num)
   elif choice == "*":
    product_of_num = num1 * num2
    print("product: ",product_of_num)
   elif choice == "%":
    remainder_of_num = num1 % num2
    print ("remainder: ",remainder_of_num)
   else: 
        print("Invalid")        