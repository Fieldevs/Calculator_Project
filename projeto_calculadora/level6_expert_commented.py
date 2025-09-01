# level6_final_commented.py
import math  # Import math module for advanced operations like sqrt

history = []  # Initialize list to store calculation history

# Function to perform addition
def add(numbers):
    return sum(numbers)  # Return sum of all numbers

# Function to perform subtraction
def subtract(numbers):
    result = numbers[0]  # Start with the first number
    for num in numbers[1:]:  # Subtract remaining numbers
        result -= num
    return result

# Function to perform multiplication
def multiply(numbers):
    result = 1  # Start with 1 for multiplication
    for num in numbers:  # Multiply sequentially
        result *= num
    return result

# Function to perform division
def divide(numbers):
    result = numbers[0]  # Start with the first number
    try:
        for num in numbers[1:]:  # Divide by remaining numbers
            result /= num
        return result
    except ZeroDivisionError:  # Handle division by zero
        return "Error: Division by zero is not allowed!"

# Function to calculate power
def power(base, exponent):
    return base ** exponent  # Return base raised to exponent

# Function to calculate square root
def square_root(number):
    if number < 0:  # Cannot take sqrt of negative number
        return "Error: Cannot take square root of negative number!"
    return math.sqrt(number)  # Return square root

# Function to calculate modulo
def modulo(a, b):
    try:
        return a % b  # Return remainder of division
    except ZeroDivisionError:  # Handle modulo by zero
        return "Error: Division by zero in modulo!"

# Function to evaluate multi-operation expressions
def evaluate_expression(expr):
    try:
        expr = expr.replace("^", "**")  # Convert ^ to ** for power
        expr = expr.replace("√", "math.sqrt")  # Convert √ to math.sqrt
        result = eval(expr)  # Evaluate the expression
        return result
    except Exception as e:  # Handle invalid expression
        return f"Error: {e}"

# Function to display history
def show_history():
    if history:  # Check if history is not empty
        print("\n--- Calculation History ---")
        for item in history:  # Print each historical calculation
            print(item)
        print("---------------------------")
    else:
        print("No calculations yet.")  # If no history

# Main program loop
while True:
    print("\n=== Calculator Level 6 - Final ===")  # Display menu title
    print("1. Single operation mode")  # Menu option 1
    print("2. Multi-operation mode")   # Menu option 2
    print("3. Show history")           # Menu option 3
    print("4. Exit")                   # Menu option 4

    choice = input("Choose an option (1-4): ")  # Get menu choice

    if choice == "4":  # Exit program
        print("Exiting calculator... Goodbye!")
        break

    # Single operation mode
    elif choice == "1":
        while True:  # Loop until user quits single mode
            # Display numbered operation menu
            print("\nChoose an operation (or 'q' to quit, 'h' for history):")
            print("1 → Addition (+)")
            print("2 → Subtraction (-)")
            print("3 → Multiplication (*)")
            print("4 → Division (/)")
            print("5 → Power (^)")
            print("6 → Square Root (√)")
            print("7 → Modulo (%)")

            op_choice = input("Your choice: ")  # Get user operation choice

            if op_choice.lower() == "q":  # Quit single operation mode
                print("Returning to main menu...")
                break

            if op_choice.lower() == "h":  # Show history
                show_history()
                continue  # Return to operation menu

            # Map number choice to operation
            if op_choice == "1":  # Addition
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = add([num1, num2])
                print("Result:", result)
                history.append(f"{num1} + {num2} = {result}")

            elif op_choice == "2":  # Subtraction
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = subtract([num1, num2])
                print("Result:", result)
                history.append(f"{num1} - {num2} = {result}")

            elif op_choice == "3":  # Multiplication
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = multiply([num1, num2])
                print("Result:", result)
                history.append(f"{num1} * {num2} = {result}")

            elif op_choice == "4":  # Division
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = divide([num1, num2])
                print("Result:", result)
                history.append(f"{num1} / {num2} = {result}")

            elif op_choice == "5":  # Power
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                result = power(base, exponent)
                print("Result:", result)
                history.append(f"{base} ^ {exponent} = {result}")

            elif op_choice == "6":  # Square root
                number = float(input("Enter the number: "))
                result = square_root(number)
                print("Result:", result)
                history.append(f"√{number} = {result}")

            elif op_choice == "7":  # Modulo
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = modulo(num1, num2)
                print("Result:", result)
                history.append(f"{num1} % {num2} = {result}")

            else:  # Invalid input
                print("Invalid choice! Please select 1-7, 'q' to quit, or 'h' for history.")

    # Multi-operation mode
    elif choice == "2":
        expr = input("Enter your expression (use +, -, *, /, ^ for power, √ for sqrt, % for modulo): ")
        result = evaluate_expression(expr)
        print("Result:", result)
        history.append(f"{expr} = {result}")

    # Show history
    elif choice == "3":
        show_history()

    # Invalid menu choice
    else:
        print("Invalid choice! Please select 1-4.")
