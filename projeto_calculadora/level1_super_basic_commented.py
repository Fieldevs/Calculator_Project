# simple_calc.py
# Super basic calculator: addition and subtraction

number1 = float(input("Enter the first number: "))  # Asks the user for the first number
number2 = float(input("Enter the second number: ")) # Asks the user for the second number

operation = input("Choose the operation (+ or -): ") # Asks the user to choose a math operation

if operation == "+":
    print("Result:", number1 + number2)  # If operation is "+", perform addition
elif operation == "-":
    print("Result:", number1 - number2)  # If operation is "-", perform subtraction
else:
    print("Invalid operation!")  # If another operation is chosen, show error 

# Atualizado em 01/09/2025 para criação de Pull Request
