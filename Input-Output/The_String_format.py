name = "parth"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

print("First: {0}, Second: {1}, Again First: {0}".format("A", "B"))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab}'.format(**table))