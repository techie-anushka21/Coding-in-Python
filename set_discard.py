#Example:-
marks_set = {98,95,99,87,91}
print(marks_set)    #Output: {98, 99, 87, 91, 95}

marks_set.discard(99)
print(marks_set)    #Output: {98, 87, 91, 95}

marks_set.discard(92)
print(marks_set)    #Output: {98, 87, 91, 95}

'''
Note: The outputs mentioned are possible outputs, not guaranteed (you might get a different 
      order of output).
'''