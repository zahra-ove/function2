###Calculator App
# Create a simple calculator that performs addition, subtraction, multiplication, and division.

# Instructions:

#step1: Define four functions: add(), subtract(), multiply(), and divide().
#step2: Each function takes two parameters and returns the result of the operation.
#step3: Use a loop to keep asking the user for input until they want to exit.
#step4: Handle errors like division by zero.


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return abs(a - b)

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error Division by zero"
        
#     return a/b



# def add(*args):
#     return sum(args)

# def subtract(a, b):
#     return abs(a - b)

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error Division by zero"
        
#     return a/b


# def calculator(a, b, operation):
#     if operation == "+":
#         return add(a,b)
#     elif operation == "-":
#         return subtract(a, b)
#     elif operation == "*":
#         return multiply(a, b)
#     else:
#         return divide(a, b)



# x = calculator(2, 5, "*") 
# print(x)  













############################# ANSWER ############################# 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation: ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")
