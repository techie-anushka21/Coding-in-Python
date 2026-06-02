'''
7. keys() - Returns all the keys of the Dictionary.
8. values() - Returns all the values of the Dictionary.
'''

students = {1: "Abhi", 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}
print(students)
#Output: {1: 'Abhi', 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}

key  = students.keys()
print(key)    #Output: dict_keys([1, 2, 3, 4, 5])

value = students.values()
print(value)  #Output: dict_values(['Abhi', 'Dipti', 'Divyanka', 'Esha', 'Harry'])