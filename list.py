
numbers = [1, 2, 3, 4]
print("Original list:", numbers, "\n")

# Print the first two numbers in the list
print("First number:", numbers[0])
print("Second number:", numbers[1],"\n")

# Print all the numbers in the list
print("All numbers:")
for i in numbers:
  print(i)
  
# Print the last number in the list
print("Last number:",numbers[-1],"\n")

# Print the length of the list
print("Length of the list:", len(numbers),"\n")

# Print the numbers in reverse order
b = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("Original list:", b)

b[1:3] = ["blackcurrant", "watermelon"]
print("updated list ",b,"\n")

# Insert position 1 and value "Pinepple":
b.insert(1, "Pinepple")
print("Insert position 1 with value 'Pinepple':",b)
print(".apppend() method adds an element to the end of the list.\n")

# sort the list
b.sort()
print("Sorted list:", b)


