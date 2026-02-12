# Print the items in the set, one by one:
print("print the items in the set, one by one:")
a = {"apple", "banana", "cherry"}

for x in a:
  print(x)
  
# Check if "banana" is present in the set:
print("\n* Check if 'banana' is present in the set:", "banana" in a)

# Add an item to a set, using the add() method:
a.add("orange")
print("\n* after adding orange to the set:", a)

# Add multiple items to a set, using the update() method:
a.update(["mango", "grapes"])  
print("\n* after adding mango and grapes to the set:", a)

# Get the length of a set:
print("\n* length of the set:", len(a))

# Remove an item from a set, using the remove() method:
a.remove("banana")
print("\n* after removing banana from the set:", a)

# Remove an item from a set if it is present, using the discard() method:
a.discard("mango")
print("\n* after discarding mango from the set:", a)

# Remove the last item from the set, using the pop() method:
a.pop()
print("\n* after popping an item from the set:", a) 




