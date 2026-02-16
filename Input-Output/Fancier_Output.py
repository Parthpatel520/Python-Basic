name = "John"
age = 25

print(f"My name is {name} and I am {age} years old.")


pi = 3.1415926
print(f"Pi rounded to 2 decimals: {pi:.2f}")

for i in range(1, 5):
    print(f"{i:3} {i*i:4} {i*i*i:10}")
    
#     | Format | Meaning                           |
# | ------ | --------------------------------- |
# | `:5`   | Right align (default for numbers) |
# | `:<5`  | Left align                        |
# | `:^5`  | Center align                      |
# | `:0>5` | Pad with zeros on the left        |


x = "Hello\nWorld"

print(x)
print(repr(x))


