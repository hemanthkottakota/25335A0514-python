students = []

n = int(input("enter no of students"))

for i in range(n):
    print(f"\nStudent {i+1}")
    
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    
    students.append((name, roll, marks))
with open("students.txt", "w") as fp:
    for student in students:
        fp.write(f"{student[0]},{student[1]},{student[2]}\n")
