# Print the last item of the tuple:
a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Original tuple:", a, "\n")
print("* last item of the tuple:",a[-1],"\n")

# Print the length of the tuple:
print("* length of the tuple:",len(a),"\n")

# Print the items in the tuple one by one:
print("* items in the tuple one by one:")       
for i in a:
  print(i)
  
# Return the third, fourth, and fifth items in the tuple:
print("\n* third, fourth, and fifth items in the tuple:",a[2:5],"\n")

# Check if "apple" is present in the tuple:
print("* Check if 'apple' is present in the tuple:", "apple" in a,"\n") 

#This example returns the items from the beginning to, but NOT included, "kiwi":
print("* items from the beginning to, but NOT included, 'kiwi':",a[:4],"\n")  

# Add an item to a tuple:
y = ("pineapple",)
a += y
print("* a after adding pineapple:", a, "\n")




  
