'''
String functions- replace() : it replaces a substring with another substring in a string.
- SYNTAX: -
  var_name = string_var_name.replace(actual_string, new_string)
'''

#Example 1: -
a = "ENVIRONMENT"
res = a.replace("E","*")    #To replace "E" with "*"
print(res)

# Output: -
# *NVIRONM*NT


#Example 2
b = "UMBRELLA"
res2 = b.replace("L","@")    #To replace "L" with "@"
print(res2)

# Output: -
# UMBRE@@A