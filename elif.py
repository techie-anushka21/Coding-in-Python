#elif statement: used when multiple conditions are present.

#Example 1: check whether a no. (input) is +ve, -ve, or 0.
num = int(input("Enter a no.: "))
print("No. entered:",num)
if (num>0):
    print("POSITIVE")
elif (num<0):
    print("NEGATIVE")
else:
    print("ZERO")

'''
Output: - (on 3 runs)

1. 1st Run: -

Enter a no.: 17
No. entered: 17
POSITIVE

2. 2nd Run: -

Enter a no.: 0
No. entered: 0
ZERO

3. 3rd Run: -

Enter a no.: -46
No. entered: -46
NEGATIVE
'''


"""Example 2: read cp and sp of an article. if sp>cp, calculate profit and profit %age.
if cp>sp, calculate loss and loss %age. else display a message: 'No profit, no loss.'"""

cp = float(input("Enter the Cost Price of the Article: "))
sp = float(input("Enter the Selling price of the Article: "))
print("Cost price =",cp)
print("Selling price =",sp)
if (sp>cp):
    print("It's a Profit!")
    p = sp-cp
    pp = (p/cp)*100
    print("Profit =",p)
    print("Profit percentage =",pp)
elif (cp>sp):
    print("It's a Loss!")
    l = cp-sp
    lp = (l/cp)*100
    print("Loss =",l)
    print("Loss percentage =",lp)
else:
    print("No profit, no loss!")

'''
Output: - (on 3 runs)

1. 1st Run: -

Enter the Cost Price of the Article: 56000.0
Enter the Selling price of the Article: 59000.0
Cost price = 56000.0
Selling price = 59000.0
It's a Profit!
Profit = 3000.0
Profit percentage = 5.357142857142857

2. 2nd Run: -

Enter the Cost Price of the Article: 59000.0
Enter the Selling price of the Article: 56000.0
Cost price = 59000.0
Selling price = 56000.0
It's a Loss!
Loss = 3000.0
Loss percentage = 5.084745762711865

3. 3rd Run: -

Enter the Cost Price of the Article: 59000.0
Enter the Selling price of the Article: 59000.0
Cost price = 59000.0
Selling price = 59000.0
No profit, no loss!
'''