def concat(*args, sep="/"):
    return sep.join((args))

# concat("earth", "mars", "venus")

print(concat("20","earth", "mars", "venus"))

# All elements inside args must be strings, otherwise join() will raise a TypeError.