#Example: -

students = {101:"Annie", 102:"Divyanka"}
print(students)    #Output: {101: 'Annie', 102: 'Divyanka'}

#To add more values: -
students.update({3:"Harry", 4:"Yuvika"})
print(students)    #Output: {101: 'Annie', 102: 'Divyanka', 3: 'Harry', 4: 'Yuvika'}

#To change an existing value: -
students.update({3:"Trisha"})
print(students)    #Output: {101: 'Annie', 102: 'Divyanka', 3: 'Trisha', 4: 'Yuvika'}