# Raising Exceptions

age = int(input("Enter age: "))

if age < 18:
    raise Exception("You are not eligible!")

print("Access granted")

# 0 value will raise ZeroDivisionError
num = int(input("Enter number: "))

if num == 0:
    raise ZeroDivisionError("You cannot divide by zero!")

print(10 / num)

# Custom Exceptions
try:
    num = int(input("Enter number: "))
    
    if num < 0:
        raise   ("Negative number not allowed!")

except ValueError as e:
    print("Error:", e)
