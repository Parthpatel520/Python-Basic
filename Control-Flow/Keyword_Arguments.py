# This code demonstrates the use of keyword arguments in a function.
def add(a, b):
    return a + b

result = add(b=5, a=10)
print("The result is:", result)  # Output: 15

print("\nUsing keyword arguments in a function with more parameters:")
def greet(name, age):
    print(f"{name} is {age} years old.")

greet(age=25, name="Alice") 



