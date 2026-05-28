at = int(input("Enter the no. of items: "))

list1 = []

for i in range(at):
    item = int(input("Enter the no.: "))
    list2 = [item]
    list1.extend(list2)

print(list1)

'''
Output: -

Enter the no. of items: 7
Enter the no.: 10
Enter the no.: 50
Enter the no.: 20
Enter the no.: 40
Enter the no.: 10
Enter the no.: 30
Enter the no.: 80
[10, 50, 20, 40, 10, 30, 80]

'''

# Suppose I want to find out the frequency of 10: -
req_item = int(input("Enter the item whose frequency you want to count: "))
print("Frequency of",req_item,"=",list1.count(req_item))

'''
Output: -

Enter the item whose frequency you want to count: 10
Frequency of 10 = 2

'''

# If I enter a number which does not exist in the List: -
'''
Output: -

Enter the item whose frequency you want to count: 30
Frequency of 60 = 0

'''