print("----Grade Calculator----")
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")
    
print("\n----Simple Calculator ----")
    
a = int(input("\nEnter first number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
choice = input("Enter choice (1/2/3): ")

b = int(input("Enter second number: "))

if choice == "1":
    result = a + b
    print("Result:", result)
elif choice == "2":
    result = a - b
    print("Result:", result)
elif choice == "3":
    result = a * b
    print("Result:", result)
else:
    print("Invalid choice")
