def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero!")

print("Calculator")
print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Select an operation (1, 2, 3, or 4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    result = add(num1, num2)
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = subtract(num1, num2)
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = multiply(num1, num2)
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    result = divide(num1, num2)
    if result is not None:
        print(f"The result of division is: {result}")
else:
    print("Invalid operation selection!")
