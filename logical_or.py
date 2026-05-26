'''
logical 'or' operator- returns True if at least 1 of the conditions is true or both are true. Returns False only if all conditions are False.
'''

#Example 1:- read a no. and check if the no. is divisible by either 2 or 5.
num = int(input("Enter a no.: "))
print("No. entered:",num)
rem1 = num%2
rem2 = num%5
if(rem1==0 or rem2==0):
    print(True)
else:
    print(False)

'''
Output: - (on 4 Runs)

1. 1st Run: - (divisible by both 2 and 5)

Enter a no.: 10
No. entered: 10
True

2. 2nd Run: - (divisible by 2 but not 5)

Enter a no.: 18
No. entered: 18
True

3. 3rd Run: - (divisible by 5 but not 2)

Enter a no.: 15
No. entered: 15
True

4. 4th Run: - (not divisible by both 2 and 5)
Enter a no.: 17
No. entered: 17
False
'''


#Example 2:- Just proof:-
print(True or True)      # Output: True
print(True or False)     # Output: True
print(False or True)     # Output: True
print(False or False)    # Output: False


#Example 3:- check if the sum of 2 nos. is greater than or equal to 10 or product is greater than or equal to 25.
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
print("1st no.: ",num1)
print("2nd no.: ",num2)
sum = num1+num2
pro = num1*num2
if(sum>=10 or pro>=25):
    print(True)
else:
    print(False)

'''
Output: - (on 3 Runs)

1. 1st Run: - (sum > 10 and product > 25)

Enter the 1st no.: 10
Enter the 2nd no.: 25
1st no.:  10
2nd no.:  25
True

2. 2nd Run: - (sum > 10 but product < 25)

Enter the 1st no.: 7
Enter the 2nd no.: 3
1st no.:  7
2nd no.:  3
True

3. 3rd Run: - (sum < 10 and product < 25)

Enter the 1st no.: 3
Enter the 2nd no.: 6
1st no.:  3
2nd no.:  6
False
'''