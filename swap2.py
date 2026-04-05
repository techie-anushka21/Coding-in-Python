#swapping of 2 integers (using input function)

num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
print("Before swapping:-")
print("num1 =",num1)
print("num2 =",num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping:-")
print("num1 =",num1)
print("num2 =",num2) 

'''
Output:-

Enter the 1st no.: 2 (Value entered by user)
Enter the 2nd no.: 1 (Value entered by user)
Before swapping:-
num1 = 2
num2 = 1
After swapping:-
num1 = 1
num2 = 2
'''