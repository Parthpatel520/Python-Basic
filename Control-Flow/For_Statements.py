# checking for students who passed the exam (marks >= 35) and storing their names and marks in a new dictionary
students = {
    "Amit": 85,
    "Riya": 35,
    "John": 90,
    "Sara": 30
}

passed_students = {}

for name, marks in students.items():
    if marks >= 35:
        passed_students[name] = marks

print(passed_students)


# print a number index and its value from a list using a for loop
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])
