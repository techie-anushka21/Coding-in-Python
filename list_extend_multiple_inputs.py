at = int(input("Enter the no. of students: "))

students = []

for i in range(at):
    reg_id = int(input("Enter reg. no.: "))
    name = input("Enter name: ")
    cgpa = float(input("Enter cgpa: "))

    students_info = [reg_id,name,cgpa]

    students.extend(students_info)

print("\nStudent details:-")
print(students)

'''
Output: -

Student details:-
[101, 'Annie', 9.77, 102, 'Harry', 9.06]

'''

'''
Note: 
- In the above output, the extend() results into mixing (flattening) of the 2 lists.
- This is not ideal for structured records.
- Hence, for such cases use append().
'''