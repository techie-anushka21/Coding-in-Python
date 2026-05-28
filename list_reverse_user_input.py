at = int(input("Enter the no. of students: "))

students = []

for i in range(at):
    reg_id = int(input("Enter reg. no.: "))
    name = input("Enter name: ")
    cgpa = float(input("Enter cgpa: "))

    students_info = [reg_id,name,cgpa]
    students.append(students_info)

print("\nStudents details: -")

print("[")
for s in students:
    print(" ",s)
print("]")

'''
Output: -

Enter the no. of students: 3
Enter reg. no.: 101
Enter name: Annie
Enter cgpa: 9.6
Enter reg. no.: 102
Enter name: Harry
Enter cgpa: 9.34
Enter reg. no.: 103
Enter name: Isha
Enter cgpa: 9.5

Students details: -
[
  [101, 'Annie', 9.6]
  [102, 'Harry', 9.34]
  [103, 'Isha', 9.5]
]

'''

# Reversing the list: -
students.reverse()

print("[")
for s in students:
    print(" ",s)
print("]")

'''
Output: -

[
  [103, 'Isha', 9.5]
  [102, 'Harry', 9.34]
  [101, 'Annie', 9.6]
]
'''