print("=== Calculator Level 4 ===")
print("Available operations: +, -, *, /")
print("Type 'q' to quit")

while True:
    operation = input("\nChoose the operation (+, -, *, /) or 'q' to quit: ")

    if operation.lower() == "q":
        print("Exiting calculator... Goodbye!")
        break

    numbers_input = input("Enter numbers separated by spaces: ")

    numbers = [float(num) for num in numbers_input.split()]

    if operation == "+":
        result = sum(numbers)
        print("Result:", result)

    elif operation == "-":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print("Result:", result)

    elif operation == "*":
        result = 1
        for num in numbers:
            result *= num
        print("Result:", result)

    elif operation == "/":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operation! Please choose +, -, *, / or q.")
