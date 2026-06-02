'''
Dictionary Union (| operator) :-
- They are used to combine 2 or more dictionaries.
- SYNTAX = dictionary1 | dictionary2
- Note: If you try to make a union of 2 dictionaries but their keys are same, then the key-value 
 obtained in the output will be of the right-hand side dictionary.
'''

#Example1: Trying to make a union of 2 dictionaries with same keys.
dict1 = {1:'Cheenu'}
dict2 = {1:'Meethi'}
c = dict1|dict2
print(c)    #Output: {1: 'Meethi'}


#Example 2: Dictionaries with unique keys:-
dict3 = {101: 'Isha'}
dict4 = {102:'Anita'}
dict5 = {103:'Abhi'}
dict6 = {104:'Vineet'}

#Union of dict3, dict4, dict5, dict6
dict7 = dict3|dict4|dict5|dict6
print(dict7)    #Output: {101: 'Isha', 102: 'Anita', 103: 'Abhi', 104: 'Vineet'}