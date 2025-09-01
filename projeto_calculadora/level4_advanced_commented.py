# level4_advanced_commented.py
# Calculator Level 4 - Advanced
# Allows performing operations with multiple numbers in a loop

print("=== Calculator Level 4 ===")  # Print the title of the calculator
print("Available operations: +, -, *, /")  # Show the available operations
print("Type 'q' to quit")  # Inform the user how to exit the program

while True:
    # Ask the user to choose an operation or quit
    operation = input("\nChoose the operation (+, -, *, /) or 'q' to quit: ")

    # Exit the loop if the user types 'q'
    if operation.lower() == "q":
        print("Exiting calculator... Goodbye!")  # Exit message
        break

    # Ask the user to input numbers separated by spaces
    numbers_input = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of floats
    numbers = [float(num) for num in numbers_input.split()]

    # Perform addition if the operation is "+"
    if operation == "+":
        result = sum(numbers)  # Sum all numbers
        print("Result:", result)  # Print the result

    # Perform subtraction if the operation is "-"
    elif operation == "-":
        result = numbers[0]  # Start with the first number
        for num in numbers[1:]:  # Subtract the remaining numbers
            result -= num
        print("Result:", result)  # Print the result

    # Perform multiplication if the operation is "*"
    elif operation == "*":
        result = 1  # Start with 1 for multiplication
        for num in numbers:  # Multiply all numbers
            result *= num
        print("Result:", result)  # Print the result

    # Perform division if the operation is "/"
    elif operation == "/":
        result = numbers[0]  # Start with the first number
        try:
            for num in numbers[1:]:  # Divide by the remaining numbers
                result /= num
            print("Result:", result)  # Print the result
        except ZeroDivisionError:  # Handle division by zero
            print("Error: Division by zero is not allowed!")

    # Handle invalid operation input
    else:
        print("Invalid operation! Please choose +, -, *, / or q.")
