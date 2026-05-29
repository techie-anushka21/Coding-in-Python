'''
We can obtain a particular element by using its index no.
SYNTAX:-
print(list_name[index])
'''

emp1 = [101,'Anita',34.7,'Manager-HR']    #list creation
print(emp1[2])    #Output: 34.7
print(emp1[0])    #Output: 101
print(emp1[3])    #Output: Manager-HR
print(emp1[1])    #Output: Anita

'''List items can be accessed from the end also:-'''
print(emp1[-1])   #Output: Manager-HR
print(emp1[-2])   #Output: 34.7
print(emp1[-3])   #Output: Anita
print(emp1[-4])   #Output: 101

'''Trying to enter an Index value out of Range:-'''
print(emp1[4])    #Output-> IndexError: list index out of range