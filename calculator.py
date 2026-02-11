a = int(input("Enter first number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Choose an operation (1/2/3/4): ")

b = int(input("Enter second number: "))

if operation == '1':    
    result = a + b
    print("Result:", result)
elif operation == '2':    
    result = a - b
    print("Result:", result)
elif operation == '3':    
    result = a * b
    print("Result:", result)
elif operation == '4':    
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")