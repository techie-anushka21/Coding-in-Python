'''
List Slicing
-It is used for creating sub-divisions of a List.
'''

marks = [98,99,95,97,92,91,96]    #creating a list
print(marks)    #Output: [98, 99, 95, 97, 92, 91, 96]

#Slicing:-

#1. Part 1:-
marks_sub_list1 = marks[1:5]      #to slice and extract only elements from index 1 to 4
print(marks_sub_list1)            #Output: [99, 95, 97, 92]
'''Note: Writing 5 in the ending index means the last element will be 5th element, NOT the
         the element at Index 5. '''

#2. Part 2:-
marks_sub_list2 = marks[1:5:2]    #to slice and extract only elements from index 1 to 4 (alternate 2)
print(marks_sub_list2)            #Output: [99, 97]

#3. Part 3:-
marks_sub_list3 = marks[0:]    #to slice and access elements from index 0 to the ending index
print(marks_sub_list3)         #Output: [98, 99, 95, 97, 92, 91, 96]

#4. Part 4:-
marks_sub_list4 = marks[0:6]    #to slice and access elements from index 0 to the index 5
print(marks_sub_list4)          #Output: [98, 99, 95, 97, 92, 91]