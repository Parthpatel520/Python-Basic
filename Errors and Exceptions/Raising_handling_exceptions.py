# one can raise exceptions using the raise statement. This allows you to signal that an error has occurred and provide information about the error.
def check_value(x):
    if x < 0:
        raise ValueError("Negative value not allowed!")
    if x == 0:
        raise ZeroDivisionError("Cannot be zero!")
    return 10 / x

try:
    print(check_value(int(input("Enter a number: "))))
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
