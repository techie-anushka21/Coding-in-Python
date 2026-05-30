'''
Sets
- They are a collection of unordered elements.
- Each element in a Set must be unique and immutable.
- Sets remove the duplicate elements.
- Sets are mutable, hence they can be modified after their creation.
- SYNTAX:- set_name = {element-1, element-2,..., element-n}
'''

#Creating our 1st Set in Python:-
set1 = {10,20,30,40,50,60}
print(set1)    #Output: {50, 20, 40, 10, 60, 30}

#Trying a Set with duplicate values:-
set2 = {10,10,20,30,30,40,50,60}
print(set2)    #Output: {50, 20, 40, 10, 60, 30}    (the repetitive values of 10 and 30 automatically removed)