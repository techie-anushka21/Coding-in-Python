'''
del Statement
- Used to delete a specified key-value pair from the dictionary.
- It does not return any value.
- Can delete the entire dictionary also, after which NameError occurs as the variable 
  itself no longer exists.
- SYNTAX: del dictionary_name[key]
'''

students = {1: "Abhi", 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}
print(students)
#Output: {1: 'Abhi', 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}

del students[1]
print(students)    #Output: {2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}

del students
print(students)    #Output: NameError: name 'students' is not defined