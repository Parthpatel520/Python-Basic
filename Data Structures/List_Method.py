a = ["Parth","Kunj","Kartik","Vrutik","Bhargav"]
print("Original list:",a)

# append using append() method
a.append("Smit")
print("After appending Smit:",a)

# insert using slicing
a[1:1] = ["vivek"]
print("After adding vivek using slicing:",a)                                                    

# insert using insert() method
a.insert(2,"Smit")
print("After inserting Smit at index 2:",a)

# remove using remove() method
a.remove("Smit")
print("After removing Smit:",a)

# remove using pop() method
a.pop(4)
print("After popping element at index 4:",a)

# remove using del keyword
del a[0:2]
print("After deleting element at index 0:",a)

# remove using clear() method
a.clear()
print("After clearing the list:",a)

# repopulate the list for further methods
a = ["Parth","Kunj","Kartik","Vrutik","Bhargav"]
print("Repopulated list:",a)

# counting occurrences of a letter in the list using count() method
print(("count a letter in the list:"))
count = 0
for name in a:
    count += name.count("a")
    
print("Total 'a' letters:", count)

# counting occurrences of a specific name in the list using count() method
print("count a specific name in the list:") 
count_kunj = a.count("Kunj")
print("Count of 'Kunj':", count_kunj)

# finding index of a specific name using index() method
print("Finding index of a specific name in the list:")
index_kartik = a.index("Kartik")
print("Index of 'Kartik':", index_kartik)

# finding index of a specific name using index() method with start and end parameters
# sequence.index(x, start, end) -- x → value to search for (required)
print("Finding index of a specific name in the list with start and end parameters:")    
index_vrutik = a.index("Vrutik", 1, 4)
print("Index of 'Vrutik' between index 1 and 4:", index_vrutik)

# sorting the list using sort() method
a.sort()
print("Sorted list:",a)

# reversing the list using reverse() method
a.reverse()
print("Reversed list:",a)

# copying the list using copy() method
b = a.copy()
print("Copied list:",b)

# extending the list using extend() method
c = ["Smit","Vivek"]
a.extend(c) 
print("Extended list:",a)

# finding length of the list using len() function
length = len(a) 
print("Length of the list:", length)
