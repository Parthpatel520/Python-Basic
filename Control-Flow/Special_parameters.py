# positional-only parameters
def greet(name, /):
    print(f"Hello, {name}!")

greet("parth")     
# Error not allowed to use keyword argument
# greet(name="Alice") #


# keyword-only parameters
def describe(*, name, age):
    print(f"{name} is {age} years old.")

describe(name="parth", age=30)  
# Error not allowed to use positional arguments
# describe("Bob", 30)            


# combining both
def info(name, /, age, *, city):
    print(f"{name} is {age} years old and lives in {city}.")   

# both are valid  
info("parth", 25, city="Ahmedabad")
# info(Charlie", age=25, city="New York") 

