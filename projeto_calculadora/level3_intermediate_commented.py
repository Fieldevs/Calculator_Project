# level3_intermediate_commented.py
# Calculator Level 3 - Intermediate
# Supports multiple calculations in a loop until the user decides to quit

print("=== Calculator Level 3 ===")
print("Available operations: +, -, *, /")
print("Type 'q' to quit")  # Inform the user how to exit

while True:
    # Ask the user to choose an operation or quit
    operation = input("\nChoose the operation (+, -, *, /) or 'q' to quit: ")

    # Exit the loop if user types 'q'
    if operation.lower() == "q":
        print("Exiting calculator... Goodbye!")
        break

    # Ask for the two numbers to perform the operation
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Perform the chosen operation
    if operation == "+":
        print("Result:", number1 + number2)  # Addition
    elif operation == "-":
        print("Result:", number1 - number2)  # Subtraction
    elif operation == "*":
        print("Result:", number1 * number2)  # Multiplication
    elif operation == "/":
        # Check for division by zero
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Error: Division by zero is not allowed!")  # Prevent crash
    else:
        print("Invalid operation! Please choose +, -, *, / or q.")  # Handle invalid input
