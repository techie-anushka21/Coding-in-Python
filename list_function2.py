'''
A list() can convert another data type into list.
'''

#Example:-
string = (list('Hello'))
print(string)    #Output: ['H', 'e', 'l', 'l', 'o']

#User input: -
string1 = input("Enter string: ")
string2 = list(string1)
print(string2) 

'''
Output: -

Enter string: Awesome
['A', 'w', 'e', 's', 'o', 'm', 'e']

'''

# Note: Spaces are also treated as characters: -
string3 = input("Enter string: ")
string4 = list(string3)
print(string4)

'''
Output: -

Enter string: Hello World!
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

'''