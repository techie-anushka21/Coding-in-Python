list1 = [1,2,3,4,5]    #list1 creation
print(list1)           #Output: [1, 2, 3, 4, 5]

list1.append(6)        #appends(adds) 6 to list1
list1.append(7)        #appends(adds) 7 to list1

print(list1)           #Output: [1, 2, 3, 4, 5, 6, 7]

list2 = [8,9]          #list2 creation
print(list2)           #Output: [8, 9]

list1.append(list2)    #appends(adds) list2 to list1
print(list1)           #Output: [1, 2, 3, 4, 5, 6, 7, [8, 9]]