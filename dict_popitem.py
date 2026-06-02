#Example: -
students = {1: "Abhi", 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}
print(students)
#Output: {1: 'Abhi', 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}

key,value = students.popitem()
print(key,value)    #Output: 5 Harry

print(students)     #Output: {1: 'Abhi', 2: 'Dipti', 3: 'Divyanka', 4: 'Esha'}