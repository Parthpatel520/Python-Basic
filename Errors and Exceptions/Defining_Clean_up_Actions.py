# Defining Clean-up Actions with finally

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("This always runs (clean-up action)")


def bool_return():
    try:
        return True
    finally:
        print("Finally block executed")

bool_return()