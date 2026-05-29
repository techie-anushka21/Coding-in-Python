tuple1 = (10,20,30,20,30,50,60)
print(tuple1)    #Output: (10, 20, 30, 20, 30, 50, 60)

c = tuple1.index(20,0,6)    #1st occurence of 20 is searched. Search starts from index 0 and ends at index 5
print("1st index at which 20 occurs is",c)    #Output: 1st index at which 20 occurs is 1