def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

result = add(*numbers)
print(result)

print("--- Unpacking with Keyword Arguments ---")
def greet(name, age):
    print(f"{name} is {age} years old.")

person = {"name": "Alice", "age": 25}

greet(**person)


