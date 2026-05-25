#ternary expressions == inline if...else

#Example 1: check eligibility of a voter.
age = float(input("Enter your age: "))
print("Age entered:",age)
result = ("Eligible to vote!" if age>=18 else "Not eligible to vote!")
print(result)

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter your age: 42.5
Age entered: 42.5
Eligible to vote!

2. 2nd Run: -

Enter your age: 17.9
Age entered: 17.9
Not eligible to vote!
'''

'''
Note: If you enter a value like 17.9 or any value greater than or equal to 17.5, 
      it will not ceil up amd remain as it is.
'''


#Example 2: check if a number is even or odd.
num = int(input("Enter a no.: "))
print("Number entered :",num)
rem = num%2
result2 = ("Even" if rem==0 else "Odd")
print(result2)

'''
Output: - (on 2 runs)

1. 1st Run: -

Enter a no.: 85
Number entered : 85
Odd

2. 2nd Run: -

Enter a no.: 74
Number entered : 74
Even
'''

'''
Note: If you try to enter a float value in int data type input then: -
ValueError: invalid literal for int() with base 10: '74.0'
'''