number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your 2nd  number: "))
operation = input("Enter the operation (+, -, *, /): ")
#perform the operation
if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1/number2
    else:
        result = "undefined(division by zero is not allowed)"
else: 
    result = "invalid operation"
print("The result is", result,)