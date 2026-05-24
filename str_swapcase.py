'''
String functions- swapcase() : it converts lowercase string to UPPERCASE and vice versa.
- SYNTAX: -
 var_name = string.swapcase() 
'''

#Example 1
print("Python Programming".swapcase())      #1st way

# Output: -
# pYTHON pROGRAMMING

a = "Python Programming"                    #2nd way
res = a.swapcase()        
print(res)

# Output: -
# pYTHON pROGRAMMING


#Example 2
print("aDORABLE dAUGHTER".swapcase())       #1st way

# Output: -
# Adorable Daughter

b = "aDORABLE dAUGHTER"                     #2nd way
res2 = b.swapcase()
print(res2)

# Output: -
# Adorable Daughter


#Example 3
print("adorable daughter".swapcase())       #1st way

# Output: -
# ADORABLE DAUGHTER

c = "adorable daughter"                     #2nd way
res3 = c.swapcase()
print(res3)

# Output: -
# ADORABLE DAUGHTER


#Example 4
print("ADORABLE DAUGHTER".swapcase())       #1st way

# Output: -
# adorable daughter

d = "ADORABLE DAUGHTER"                     #2nd way
res4 = d.swapcase()
print(res4)

# Output: -
# adorable daughter