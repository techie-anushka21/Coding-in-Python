#if statements in Python

# Example 1: read a number and check whether it is +ve, -ve, or 0.
num = int(input("Enter a no.: "))
print("The no. is:",num)
if (num>0):
    print("POSITIVE")
if (num==0):
    print("ZERO")
if (num<0):
    print("NEGATIVE")

''' 
Output: - (on 3 runs)

1. 1st Run: -

Enter a no.: 6
The no. is: 6
POSITIVE

2. 2nd Run: -

Enter a no.: 0
The no. is: 0
ZERO

3. 3rd Run: -

Enter a no.: -7
The no. is: -7
NEGATIVE
'''


#Example 2: read radius of a circle. if >=5, calculate area, else, calculate circumference.
rad = float(input("Enter the radius of the circle: "))
print("Radius =",rad)
if (rad>=5):
    area = 3.14*rad**2
    print("Area of Circle =",area)
if (rad<5):
    circum = 2*3.14*rad
    print("Circumference of Circle =",circum)

''' 
Output: -

Enter the radius of the circle: 5.2
Radius = 5.2
Area of Circle = 84.9056
'''


#Example 3: add 2 nos., if greater than or equal to 10, add 2 to the sum, else subtract 2.
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
sum = num1+num2
print("Sum =",sum)
if (sum>=10):
    res = sum+2
    print("Result =",res)
if (sum<10):
    res = sum-2
    print("Result =",res)

'''
Output: - (on 3 runs)

1. 1st Run: -

Enter the 1st no.: 3
Enter the 2nd no.: 7
Sum = 10
Result = 12

2. 2nd Run: -

Enter the 1st no.: 7
Enter the 2nd no.: 9
Sum = 16
Result = 18

3. 3rd Run: -

Enter the 1st no.: 6
Enter the 2nd no.: 2
Sum = 8
Result = 6
'''