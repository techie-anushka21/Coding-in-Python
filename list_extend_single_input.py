student = []

reg_id = int(input("Enter reg no.: "))
name = input("Enter name: ")
cgpa = float(input("Enter cgpa: "))

student_info = [reg_id,name,cgpa]

student.extend(student_info)
print(student)

'''
Output: -

Enter reg no.: 101
Enter name: Annie
Enter cgpa: 9.77
[101, 'Annie', 9.77]

'''