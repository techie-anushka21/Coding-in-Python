'''
List: Example 1:-
Count the total no. of string elements in a list.
'''

list1 = [1,'Manager','HR',31,5.1]
string_count = 0

for i in list1:
    if type(i) == str:
        print(i)
        string_count = string_count + 1

print("Total no. of Strings in the program =",string_count)

'''
Output: -

Manager
HR
Total no. of Strings in the program = 2

'''

# Another example: -
list2 = [10,"AB","CD",20,"HI",30,40]
print(list2)

int_count = 0
for i in list2:
    if type(i) == int:
        print(i)
        int_count = int_count + 1

print("No. of integers in list2 = ",int_count)

'''
Output: -

[10, 'AB', 'CD', 20, 'HI', 30, 40]
10
20
30
40
No. of integers in list2 =  4

'''