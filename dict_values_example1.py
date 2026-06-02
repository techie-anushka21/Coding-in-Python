'''
Example: -
Iterating over values: -
'''

students = {1: "Abhi", 2: 'Dipti', 3: 'Divyanka', 4: 'Esha', 5: 'Harry'}
count = 0
for value in students.values():
    print(value)
    count = count+1
print("No. of values in the dictionary =",count)

'''
Output:
Abhi
Dipti
Divyanka
Esha
Harry
No. of values in the dictionary = 5
'''