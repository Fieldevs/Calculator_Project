# level5_professional_commented.py
# Calculator Level 5 - Professional
# Uses functions for each operation and a structured menu

# Define function for addition
def add(numbers):
    result = sum(numbers)  # Sum all numbers
    return result

# Define function for subtraction
def subtract(numbers):
    result = numbers[0]  # Start with the first number
    for num in numbers[1:]:  # Subtract remaining numbers
        result -= num
    return result

# Define function for multiplication
def multiply(numbers):
    result = 1  # Start with 1 for multiplication
    for num in numbers:  # Multiply all numbers
        result *= num
    return result

# Define function for division
def divide(numbers):
    result = numbers[0]  # Start with the first number
    try:
        for num in numbers[1:]:  # Divide sequentially
            result /= num
        return result
    except ZeroDivisionError:  # Handle division by zero
        return "Error: Division by zero is not allowed!"

# Main program
print("=== Calculator Level 5 ===")
print("Available operations: +, -, *, /")
print("Type 'q' to quit")  # Instruction to quit

while True:
    # Display menu and ask for operation
    operation = input("\nChoose the operation (+, -, *, /) or 'q' to quit: ")

    # Exit condition
    if operation.lower() == "q":
        print("Exiting calculator... Goodbye!")
        break

    # Ask user to input numbers separated by spaces
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [float(num) for num in numbers_input.split()]  # Convert input to list of floats

    # Call the corresponding function based on user input
    if operation == "+":
        print("Result:", add(numbers))
    elif operation == "-":
        print("Result:", subtract(numbers))
    elif operation == "*":
        print("Result:", multiply(numbers))
    elif operation == "/":
        print("Result:", divide(numbers))
    else:
        print("Invalid operation! Please choose +, -, *, / or q.")  # Handle invalid input 

# Atualizado em 01/09/2025 para criação de Pull Request

