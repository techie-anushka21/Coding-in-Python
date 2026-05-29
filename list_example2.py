'''
List: Example 2:-
Perform dynamic indexing and slicing operations in a list.
'''

list1 = [1,2,3,4,5,6]    #list creation

#indexing:-
index_value = int(input("Enter the index value of the element you want to access: "))
print("Value at",index_value," is:",list1[index_value])

'''
Output: -

Enter the index value of the element you want to access: 4
Value at 4  is: 5

'''

#slicing:-
start_index = int(input("Enter the starting index: "))
ending_index = int(input("Enter the ending index: "))
jump_value = int(input("Enter jump value: "))

list2 = list1[start_index:ending_index:jump_value]
print(list2)

'''
Output: -

Enter the starting index: 1
Enter the ending index: 5
Enter jump value: 2
[2, 4]

'''