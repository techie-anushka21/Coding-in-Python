'''
Dictionary
- It is an association of Keys & Values.
- It is mutable (changeable).
- It is ordered (since Python 3.7+).
- It is NOT indexed.
- Keys must be unique but values need not to be unique.
- SYNTAX: dictionary_name = {"key-1":"value-1",.....,"key-2":"value-n"}
'''

#Creating our 1st Dictionary in Python:-
dictionary1 = {"Name":"Anita", "Age":37, "Position":"Manager", "Address":"Mumbai"}
print(dictionary1)
#Output-> {'Name': 'Anita', 'Age': 37, 'Position': 'Manager', 'Address': 'Mumbai'}


#Another dictionary:-
marks = {"English":95, "Hindi":98, "Maths":85, "Science":94, "SST":100}
print(marks)
#Output-> {'English': 95, 'Hindi': 98, 'Maths': 85, 'Science': 94, 'SST': 100}


#To access individual element: -
print(dictionary1["Name"])        # Output: Anita
print(dictionary1["Position"])    # Output: Manager

print(marks["English"])           # Output: 95
print(marks["SST"])               # Output: 100


#To change an existing value: -
dictionary1["Position"] = "Director"
print(dictionary1)
#Output: {'Name': 'Anita', 'Age': 37, 'Position': 'Director', 'Address': 'Mumbai'}


marks["Maths"] = 87
print(marks)
#Output: {'English': 95, 'Hindi': 98, 'Maths': 87, 'Science': 94, 'SST': 100}