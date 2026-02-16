# Enriching Exceptions with Notes
try:
    x = int("abc")
except ValueError as e:
    e.add_note("This happened while converting user input to integer")
    raise


