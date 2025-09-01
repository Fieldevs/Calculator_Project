print("=== Calculator Level 2 ===")
print("Avalible Operations: +,-,*,/")

number1 = float(input("Type the first number: "))
number2 = float(input("Type the second number: "))
operation = input("Choose the operation (+,-,*,/): ")

if operation == "+":
    print("Result:", number1 + number2)
elif operation == "-":
    print("Result:", number1 - number2)
elif operation == "*":
    print("Result:", number1 * number2)
elif operation == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Error. Division by ZERO is not allowed!")
else:
    print("Invalid Operation!")