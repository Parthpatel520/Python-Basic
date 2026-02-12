# Default arguments allow you to specify default values for parameters in a function
def person(name="Unknown", age=0):
    print(f"{name} is {age} years old.")

person()                       # Both defaults
person("Kunj")                  # Only age default
person("parth", 25)            # No defaults

print("\nExample with Addition:")
def calculate(x, y=10):
    return x + y

print(calculate(5))          # y uses default 10
print(calculate(5, 20))      # y overridden
