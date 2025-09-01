# level2_basic_commented.py
# Calculator Level 2 - Basic
# Operations: +, -, *, /

print("=== Calculator Level 2 ===")
print("Available operations: +, -, *, /")

# Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Ask the user which operation they want to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the chosen operation
if operation == "+":
    print("Result:", number1 + number2)  # Addition
elif operation == "-":
    print("Result:", number1 - number2)  # Subtraction
elif operation == "*":
    print("Result:", number1 * number2)  # Multiplication
elif operation == "/":
    if number2 != 0:
        print("Result:", number1 / number2)  # Division
    else:
        print("Error: Division by zero is not allowed!")  # Prevents crash
else:
    print("Invalid operation!")  # Handles invalid input

# Atualizado em 01/09/2025 para criação de Pull Request
