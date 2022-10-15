print("select operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("this is the sum " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("this is the sum " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("this is the sum " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("this is the sum " + str(int(num1) / int(num2)))
else:
    print("wrong input dumbass")