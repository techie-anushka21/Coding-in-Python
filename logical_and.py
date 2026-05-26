'''
logical 'and' operator- returns True when all conditions are True.
'''

#Example-1:- read a no. and check whether it is divisible by 2 and 5.
num = int(input("Enter a no.: "))
print("No. entered:",num)
rem1 = num%2
rem2 = num%5
if(rem1==0 and rem2==0):
    print("Divisible by both 2 and 5.")
else:
    print("Not divisible by both 2 and 5")

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter a no.: 10
No. entered: 10
Divisible by both 2 and 5.

2. 2nd Run: -

Enter a no.: 17
No. entered: 17
Not divisible by both 2 and 5
'''


#Example 2:- just for knowledge
print(True and True)      # Output: True
print(True and False)     # Output: False
print(False and True)     # Output: False
print(False and False)    # Output: False


#Example 3:- multiply 2 numbers and check if the result is greater than or equal to 25 and sum is greater than or equal to 10.
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
print("1st no.:",num1)
print("2nd no.:",num2)
pro = num1*num2
sum = num1+num2
if(pro>=25 and sum>=10):
    print(True)
else:
    print(False)

'''
Output: - (on 3 runs)

1. 1st Run: - (sum > 10 and product > 25)

Enter the 1st no.: 10
Enter the 2nd no.: 25
1st no.: 10
2nd no.: 25
True

2. 2nd Run: - (sum = 10 but product < 25)

Enter the 1st no.: 7
Enter the 2nd no.: 3
1st no.: 7
2nd no.: 3
False

3. 3rd Run: - (sum < 10 and product < 25)

Enter the 1st no.: 4
Enter the 2nd no.: 5
1st no.: 4
2nd no.: 5
False
'''