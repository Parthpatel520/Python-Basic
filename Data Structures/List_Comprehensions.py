# List comprehensions provide a concise way to create lists. The basic syntax is:
squares = []
for x in range(10):
    squares.append(x)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# Using list comprehensions
squares = [(x, x**2) for x in range(6)]
print(squares)

# weapon.strip
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
Weapon = [weapon.strip() for weapon in freshfruit]
print(Weapon)