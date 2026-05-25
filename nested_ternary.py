#nested ternary operator = elif

#Example 1: Find the largest of 3 nos.
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
num3 = int(input("Enter the 3rd no.: "))
print("1st no. =",num1)
print("2nd no. =",num2)
print("3rd no. =",num3)
result = (num1 if (num1>num2 and num1>num3) else (num2) if (num2>num3) else (num3))
print("Largest no. is =",result)

'''
Output: -

Enter the 1st no.: 10
Enter the 2nd no.: 6
Enter the 3rd no.: 9
1st no. = 10
2nd no. = 6
3rd no. = 9
Largest no. is = 10
'''


#Example 2: find the smallest number.
n1 = int(input("Enter the 1st no.: "))
n2 = int(input("Enter the 2nd no.: "))
n3 = int(input("Enter the 3rd no.: "))
print("1st no. =",n1)
print("2nd no. =",n2)
print("3rd no. =",n3)
result1 = (n1 if (n1<n2 and n1<n3) else n2 if (n2<n3) else n3)
print("Smallest no. is =",result1)

'''
Output: -

Enter the 1st no.: 4
Enter the 2nd no.: 6
Enter the 3rd no.: 8
1st no. = 4
2nd no. = 6
3rd no. = 8
Smallest no. is = 4
'''