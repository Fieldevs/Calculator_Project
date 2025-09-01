print("=== Calculator Level 3 ===")
print("Available Operations: +, -, *, / ")
print("Type 'q' to quit ")

while True:
    operation = input("\nChoose the operation (+, -, *, /) or 'q' to quit: ")
    if operation.lower() == 'q':
        print("Exiting Calculator... GoodBye!")
        break

    number1 = float(input("Type the first number: "))
    number2 = float(input("Type the second number: "))

    if operation == "+":
        print("Result:", number1 + number1)
    
    elif operation == "-":
        print("Result:", number1 - number2)
    
    elif operation == "*":
        print("Result:", number1 * number2)

    elif operation == "/":
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("ERROR: Division by zero is not allowed! ")
    else:
        print("Invalid operation! Please choose +, -, *, / or q")        