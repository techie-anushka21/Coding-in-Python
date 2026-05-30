#Example:-
marks_set = {98,95,99,87,91}
print(marks_set)    #Output: {98, 99, 87, 91, 95}

marks_set.remove(91)
print(marks_set)    #Output: {98, 99, 87, 95}

#If I try to remove an element which is not in the set:-
marks_set.remove(92)    #Output-> KeyError: 92

'''
Note: The outputs mentioned while printing the set are possible outputs, not guaranteed 
      (you might get a different order of output).
'''