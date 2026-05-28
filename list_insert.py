list1 = []        #list creation
print(list1)      #Output: []    (An empty list)

list1.insert(0,2)    #insert 2 at index 0
print(list1)         #Output: [2]

list1.insert(0,1)    #insert 1 at index 0, 2 will shift to index 1
print(list1)         #Output: [1, 2]

print(list1.index(1))    #Output: 0

list1.insert(2,3)    #insert 3 at index 2
list1.insert(3,4)    #insert 4 at index 3
list1.insert(4,5)    #insert 5 at index 4
list1.insert(5,6)    #insert 6 at index 5

print(list1)         #Output: [1, 2, 3, 4, 5, 6]