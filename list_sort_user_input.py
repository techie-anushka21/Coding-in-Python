amt = int(input("Enter the no. of list items: "))

list1 = []

for i in range(amt):
    item = int(input("Enter no.: "))
    list2 = [item]
    list1.extend(list2)

print(list1)

'''
Output: -

Enter no.: 6 
Enter no.: 2
Enter no.: 4
Enter no.: 12
Enter no.: 10
Enter no.: 8
[6, 2, 4, 12, 10, 8]

'''

# Sorting the list in ASCENDING order: -
list1.sort()
print(list1)    # Output: [2, 4, 6, 8, 10, 12]

# Sorting the list in DESCENDING order: -
list1.sort(reverse=True)
print(list1)    # Output: [12, 10, 8, 6, 4, 2]

# What if I used list1.sort(reverse=False): -
list1.sort(reverse=False)
print(list1)    # Output: [2, 4, 6, 8, 10, 12]

'''
Hence, list_name.sort() and list_name.sort(reverse=False) show the same behaviour 
(arranging the list elements in ASCENDING order).
'''