# creating list: -
at = int(input("Enter the no. of inputs: "))
list1 = []

for i in range(at):
    item = int(input("Enter no.: "))
    list1.append(item)

print(list1)

'''
Output: -

Enter no.: 10
Enter no.: 20
Enter no.: 30
Enter no.: 40
Enter no.: 50
[10, 20, 30, 40, 50]

'''

# using copy() : -
list2 = list1.copy()
print(list2)    # Output: [10, 20, 30, 40, 50]