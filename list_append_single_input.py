# Taking a single student information: -

student = []

reg_id = int(input("Enter the reg. no.: "))
name = input("Enter the name: ")    # didn't mention str(input("Enter the name: ")) as input() returns a string by default.
age = int(input("Enter the age: "))
score = float(input("Enter the score: "))

student_info = [reg_id,name,age,score]

student.append(student_info)
print(student)
print(type(student))

'''
Output: -

Enter the reg. no.: 101
Enter the name: Annie
Enter the age: 21
Enter the score: 98.7
[[101, 'Annie', 21, 98.7]]
<class 'list'>

'''