#calculator for internship project
print("which operation do you want to perform")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. DIVISON")
print("4. MULTIPLY")
print("5. SQUARE ROOT")
print("6. POWER")
 
operation = input()
if operation == "1":
    num1 =input("Enter first Number: ")
    num2 = input("Enter second number: ")
    print("the sum of two numbers are: "+ str(int (num1) + int(num2)))
elif operation =="2":
    num1 =input("Enter first Number: ")
    num2 = input("Enter second number: ")
    print("the differnce is: "+ str(int (num1) - int(num2)))
elif operation =="3":
    num1 =input("Enter first Number: ")
    num2 = input("Enter second number: ")
    print("the reult of division is : "+ str(int (num1) / int(num2)))
elif operation =="4":
    num1 =input("Enter first Number: ")
    num2 = input("Enter second number: 1")
    print("the product is: "+ str(int (num1) * int(num2)))
elif operation =="5":
    num =int(input("Enter Number: "))
    result = num**0.5
    print("square root of",num,"is: ",result)
elif operation =="6":
    num =int(input("Enter Number: "))
    print("The result is %d:" %(pow(num, 2)))
else:
    print("Invalid Entry")