# while True print('Hello world') # (:) SyntaxError: invalid syntax

while True:
    print('Hello world')
    break


# 8.2. Exceptions

# print(1/0) # ZeroDivisionError: division by zero
try:
    print(1/0)      
except ZeroDivisionError:
    print("You can't divide by zero!")

# variable 'spam' is not defined
try: 
    print(4 + spam*3)
except NameError:
    print("Variable 'spam' is not defined.")
    
# print('2' + 2) # TypeError: can only concatenate str (not "int") to str
try:
    print('2' + 2)
except TypeError:
    print("You can't concatenate a string and an integer.")
