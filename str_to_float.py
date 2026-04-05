#converting floating data of string type to floating type.

a = "10.5"    #float data of string type
b = "25.7"
print(a,b)
print(a+b)

a = float(a)    #float data of str type converted to float type
b = float(b)
print(a,b)
print(a+b)

'''
Output:-

10.5 25.7
10.525.7
10.5 25.7
36.2
'''