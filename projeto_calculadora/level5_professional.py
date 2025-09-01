
def add(numbers):
    result = sum(numbers) 
    return result

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

# Main program
print("=== Calculator Level 5 ===")
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
        print("Result:", add(numbers))
    elif operation == "-":
        print("Result:", subtract(numbers))
    elif operation == "*":
        print("Result:", multiply(numbers))
    elif operation == "/":
        print("Result:", divide(numbers))
    else:
        print("Invalid operation! Please choose +, -, *, / or q.")  
