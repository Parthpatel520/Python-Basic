dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)

# Print the value of the "model" key:
print("* The model of the car is:", dict["model"],"\n")

# Print the value of the "year" key:    
print("* The year of the car is:", dict["year"],"\n")

# Print the keys of the dictionary:
print("* The keys of the dictionary are:", dict.keys(),"\n")

# Print the values of the dictionary:
print("* The values of the dictionary are:", dict.values(),"\n")

# Print the items of the dictionary:
print("* The items of the dictionary are:", dict.items(),"\n")

# print key value pair one by one:
print("* The key value pair one by one:")
for x, y in dict.items():
  print(x, ":", y)
  
# Check if "model" is a key in the dictionary:
print("\n* Check if 'model' is a key in the dictionary:", "model" in dict)

# Add a new key-value pair to the dictionary:
dict["color"] = "red"
print("\n* after adding a new key-value pair to the dictionary:", dict)

# Remove a key-value pair from the dictionary, using the pop() method:
dict.pop("model")
print("\n* after removing the 'model' key-value pair from the dictionary:", dict)

# Remove an item from the dictionary, using the del keyword:
del dict["year"]
print("\n* after removing the 'year' key-value pair from the dictionary:", dict)

# Check if "model" is one of the keys in the dictionary:
if "model" in dict:
  print("\n* Yes, 'model' is one of the keys in the dict dictionary")
else:
    print("\n* No, 'model' is not one of the keys in the dict dictionary")
    
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print("\n* myfamily:", myfamily)

# Print the name of child2:
print("\n* The name of child2 is:", myfamily["child2"]["name"])

# print the child2 key value pair one by one:
print("\n* The child2 key value pair one by one:")
for x, y in myfamily["child2"].items():
  print(x, ":", y)
  
  
  