#converting integer data of string type to integer type.

a = "10"    #here the numbers in a and b are of string types.
b = "25"
print(a,b)
print(a+b)

a = int(a)    #here both the numbers stored in a and b have been converted to integer type.
b = int(b)
print(a,b)
print(a+b)

'''
Output:-

10 25
1025
10 25
35
'''