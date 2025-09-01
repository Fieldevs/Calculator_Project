
import math  

history = [] 

def add(numbers):
    return sum(numbers) 


def subtract(numbers):
    result = numbers[0]  
    for num in numbers[1:]:  
        result -= num
    return result


def multiply(numbers):
    result = 1  
    for num in numbers:  
        result *= num
    return result


def divide(numbers):
    result = numbers[0] 
    try:
        for num in numbers[1:]:  
            result /= num
        return result
    except ZeroDivisionError:  
        return "Error: Division by zero is not allowed!"


def power(base, exponent):
    return base ** exponent  


def square_root(number):
    if number < 0: 
        return "Error: Cannot take square root of negative number!"
    return math.sqrt(number) 


def modulo(a, b):
    try:
        return a % b  
    except ZeroDivisionError:  
        return "Error: Division by zero in modulo!"


def evaluate_expression(expr):
    try:
        expr = expr.replace("^", "**") 
        expr = expr.replace("√", "math.sqrt")  
        result = eval(expr)  
        return result
    except Exception as e: 
        return f"Error: {e}"


def show_history():
    if history:  
        print("\n--- Calculation History ---")
        for item in history:  
            print(item)
        print("---------------------------")
    else:
        print("No calculations yet.") 


while True:
    print("\n=== Calculator Level 6 - Final ===")  
    print("1. Single operation mode") 
    print("2. Multi-operation mode")  
    print("3. Show history")           
    print("4. Exit")                  

    choice = input("Choose an option (1-4): ")  

    if choice == "4": 
        print("Exiting calculator... Goodbye!")
        break

    
    elif choice == "1":
        while True:  
           
            print("\nChoose an operation (or 'q' to quit, 'h' for history):")
            print("1 → Addition (+)")
            print("2 → Subtraction (-)")
            print("3 → Multiplication (*)")
            print("4 → Division (/)")
            print("5 → Power (^)")
            print("6 → Square Root (√)")
            print("7 → Modulo (%)")

            op_choice = input("Your choice: ")  

            if op_choice.lower() == "q":  
                print("Returning to main menu...")
                break

            if op_choice.lower() == "h":  
                show_history()
                continue  

            
            if op_choice == "1":  
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = add([num1, num2])
                print("Result:", result)
                history.append(f"{num1} + {num2} = {result}")

            elif op_choice == "2":  
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = subtract([num1, num2])
                print("Result:", result)
                history.append(f"{num1} - {num2} = {result}")

            elif op_choice == "3":  
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = multiply([num1, num2])
                print("Result:", result)
                history.append(f"{num1} * {num2} = {result}")

            elif op_choice == "4":  
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = divide([num1, num2])
                print("Result:", result)
                history.append(f"{num1} / {num2} = {result}")

            elif op_choice == "5":  
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                result = power(base, exponent)
                print("Result:", result)
                history.append(f"{base} ^ {exponent} = {result}")

            elif op_choice == "6":  
                number = float(input("Enter the number: "))
                result = square_root(number)
                print("Result:", result)
                history.append(f"√{number} = {result}")

            elif op_choice == "7":  
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = modulo(num1, num2)
                print("Result:", result)
                history.append(f"{num1} % {num2} = {result}")

            else:  
                print("Invalid choice! Please select 1-7, 'q' to quit, or 'h' for history.")

    
    elif choice == "2":
        expr = input("Enter your expression (use +, -, *, /, ^ for power, √ for sqrt, % for modulo): ")
        result = evaluate_expression(expr)
        print("Result:", result)
        history.append(f"{expr} = {result}")

    elif choice == "3":
        show_history()

   
    else:
        print("Invalid choice! Please select 1-4.")
