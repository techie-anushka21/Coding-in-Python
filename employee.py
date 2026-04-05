"""read 2 employees' name, designation, age, gender, and salary then display all with proper prompt message."""              

print("Enter details of 1st Employee:-")    #taking details of 1st employee
name1 = input("Enter name: ")
desi1 = input("Enter designation: ")
age1 = int(input("Enter age: "))
gen1 = input("Enter gender: ")
sal1 = float(input("Enter salary: "))
print("")

print("Enter details of 2nd Employee:-")    #taking details of 2nd employee
name2 = input("Enter name: ")
desi2 = input("Enter designation: ")
age2 = int(input("Enter age: "))
gen2 = input("Enter gender: ")
sal2 = float(input("Enter salary: "))
print("")

print("Details of 1st Employee:-")    #printing details of 1st employee
print("Name:",name1)
print("Designation:",desi1)
print("Age:",age1)
print("Gender:",gen1)
print("Salary:",sal1)
print("")

print("Details of 2nd Employee:-")    #printing details of 2nd employee
print("Name:",name2)
print("Designation:",desi2)
print("Age:",age2)
print("Gender:",gen2)
print("Salary:",sal2)
print("")

'''
Output:-

Enter details of 1st Employee:-
Enter name: Anita Thakur
Enter designation: Manager-IT
Enter age: 34
Enter gender: Female
Enter salary: 720000.0

Enter details of 2nd Employee:-
Enter name: Abhijeet Rajput
Enter designation: Manager-HR
Enter age: 40
Enter gender: Male
Enter salary: 900000.0

Details of 1st Employee:-
Name: Anita Thakur
Designation: Manager-IT
Age: 34
Gender: Female
Salary: 720000.0

Details of 2nd Employee:-
Name: Abhijeet Rajput
Designation: Manager-HR
Age: 40
Gender: Male
Salary: 900000.0
'''