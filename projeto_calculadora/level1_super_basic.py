number1 = float(input("Enter the first number: ")) 
number2 = float(input("Enter the second number: ")) 

operation = input("Choose the operation (+ or -): ") 

if operation == "+":
    print("Result:", number1 + number2) 

elif operation == "-":
    print("Result:", number1 - number2) 

else:
    print("Invalid operation!") 
