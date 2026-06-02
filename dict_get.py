#Example:-
students = {1:"Abhi", 2:"Vidhi", 3:"Khyati", 4:"Vineet"}
print(students)    #Output: {1: 'Abhi', 2: 'Vidhi', 3: 'Khyati', 4: 'Vineet'}

s1 = students.get(1)    #To access the value of key 1
print(s1)               #Output: Abhi

s2 = students.get(4)    #To access the value of key 4
print(s2)               #Output: Vineet

s3 = students.get(5)    #To access the value of key 5 (which does not exists)
print(s3)               #Output: None