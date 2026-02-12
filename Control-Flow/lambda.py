print("Even numbers from the list: ")
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

print("using map to square the numbers: ")
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, numbers))
print(squared)

print("using square lambda function: ")
square = lambda x: x * x

print(square(5))
