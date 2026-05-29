at = int(input("Enter the no. of inputs: "))

list1 = []

for i in range(at):
    item = int(input("Enter no.: "))
    list1.append(item)

print(list1)

'''
Output: -

Enter the no. of inputs: 5
Enter no.: 10
Enter no.: 20
Enter no.: 50
Enter no.: 40
Enter no.: 30
[10, 20, 50, 40, 30]

'''

# using clear() function: -
list1.clear()
print(list1)    # Output: []