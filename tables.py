#printing table in Python using for loop
num = int(input("Enter the no. whose table you want: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Note: 1. range() only supports integers
#      2. ending value is always 1 less than the written no.
#      3. step value is 1 by default