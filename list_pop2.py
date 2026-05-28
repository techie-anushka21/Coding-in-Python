amt = int(input("Enter the no. of students: "))

students = []

for i in range(amt):
    reg_id = int(input("Enter the reg. no.: "))
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    score = float(input("Enter the score: "))

    students_info = [reg_id,name,age,score]

    students.append(students_info)

print("\nStudents details: -")
print("[")
for s in students:
    print(" ",s)
print("]")

'''
Output: -

Enter the no. of students: 4
Enter the reg. no.: 101
Enter the name: Annie
Enter the age: 21
Enter the score: 90.3
Enter the reg. no.: 102
Enter the name: Harry
Enter the age: 21
Enter the score: 98.4
Enter the reg. no.: 103
Enter the name: Isha
Enter the age: 21
Enter the score: 93.7
Enter the reg. no.: 104
Enter the name: Jenny
Enter the age: 21
Enter the score: 91.6

Students details: -
[
  [101, 'Annie', 21, 90.3]
  [102, 'Harry', 21, 98.4]
  [103, 'Isha', 21, 93.7]
  [104, 'Jenny', 21, 91.6]
]

'''

# If I want to remove the details of Student present at index 2: -
students.pop(2)
print(students)

'''
Output: -

[[101, 'Annie', 21, 90.3], [102, 'Harry', 21, 98.4], [104, 'Jenny', 21, 91.6]]

'''

# If I don't mention index in pop(), then last element will be removed by default: -
students.pop()
print(students)

'''
Output: -

[[101, 'Annie', 21, 90.3], [102, 'Harry', 21, 98.4]]

'''