# Break and Continue Statements in Python
numbers = [10, 20, 30, 40, 50]
print("Using break statement:")
for n in numbers:
    if n == 30:
        print("Found 30")
        break
    
print("\nUsing continue statement:")
for n in numbers:   
    if n == 30:
        print("Skipping 30")
        continue
    print(n)

# Nested loops with break statement
print("\nNested loops with break statement:")
for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)
        if j == 2:
         break
    # print("i =", i, "j =", j)
    

    
