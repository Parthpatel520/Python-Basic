try:
    x = int("abc") 
except ValueError as e:
    raise RuntimeError("Cannot convert input to number") from e
