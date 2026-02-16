import Mymath 
# from Mymath import add -> one function import
# from Mymath import add, subtract -> multiple function import
# from Mymath import * -> all function import

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

result = Mymath.add(a, b) 
print(f"The result of adding {a} and {b} is: {result}")

result = Mymath.subtract(a, b)
print(f"The result of subtracting {b} from {a} is: {result}")

result = Mymath.multiply(a, b)
print(f"The result of multiplying {a} and {b} is: {result}")

try:
    result = Mymath.divide(a, b)
    print(f"The result of dividing {a} by {b} is: {result}")    
except ValueError as e:
    print(e)
    
print(dir(Mymath))
