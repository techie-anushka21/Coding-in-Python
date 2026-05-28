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

Enter the no. of students: 2
Enter the reg. no.: 101
Enter the name: Annie
Enter the age: 21
Enter the score: 98.8
Enter the reg. no.: 103
Enter the name: Harry
Enter the age: 21
Enter the score: 94.4

Students details: -
[
  [101, 'Annie', 21, 98.8]
  [103, 'Harry', 21, 94.4]
]

'''

# Now suppose I missed "Student 102", so: -

students.insert(1,[102,"Dipti",21,91.2])    # students.insert(index,element)

print("\nUpdated Students details: -")
print("[")
for s in students:
    print(" ",s)
print("]")

'''
Output: -

Updated Students details: -
[
  [101, 'Annie', 21, 98.8]
  [102, 'Dipti', 21, 91.2]
  [103, 'Harry', 21, 94.4]
]

'''