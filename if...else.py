#if...else statements

# Example 1: check whether the input no. is even or odd.
num = int(input("Enter a no.: "))
print("Number entered:",num)
rem = num%2
if (rem==0):
    print("Even")
else:
    print("Odd")

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter a no.: 5
Number entered: 5
Odd

2. 2nd Run: -

Enter a no.: 6
Number entered: 6
Even
'''


# Example 2: read 2 nos. if both are equal calculate their sum and product, else calculate difference.
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
print("1st no. =",num1)
print("2nd no. =",num2)
if (num1==num2):
    sum = num1+num2
    pro = num1*num2
    print("Sum =",sum)
    print("Product =",pro)
else:
    diff = num1-num2
    print("Difference =",diff)

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter the 1st no.: 6
Enter the 2nd no.: 6
1st no. = 6
2nd no. = 6
Sum = 12
Product = 36

2. 2nd Run: -

Enter the 1st no.: 7
Enter the 2nd no.: 2
1st no. = 7
2nd no. = 2
Difference = 5
'''


# Example 3: Check eligiblity for voting and print status as per the eligibility.
age = float(input("Enter your age: "))
print("Age entered:",age)
if (age>=18):
    print("Eligible to vote!")
else:
    print("Not eligible to vote!")

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter your age: 23
Age entered: 23.0
Eligible to vote!

2. 2nd Run: -

Enter your age: 17.4
Age entered: 17.4
Not eligible to vote!
'''