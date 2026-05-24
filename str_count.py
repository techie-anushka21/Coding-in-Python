'''
String functions- count() : it counts the total no. of substrings in a string.
- SYNTAX: -
  var_name = literal/variable.count('substring'/sub_string_variable)
'''

#Example 1: -
print("BEAUTIFUL".count("U"))    #1st way

# Output: -
# 2

a = "BEAUTIFUL"                  #2nd way
res = a.count("U")
print("Total no. of U's in",a,"=",res)

# Output: -
# Total no. of U's in BEAUTIFUL = 2


#Example 2: -

print("ENVIRONMENT".count("E"))    #1st way

# Output: -
# 2

b = "ENVIRONMENT"                  #2nd way
res2 = b.count("E")
print("No. of E's in",b,"=",res2)

# Output: -
# No. of E's in ENVIRONMENT = 2


#Example 3: Counting the no. of spaces in a String.
c = "Have a nice day ahead everyone!"
res3 = c.count(" ")
print("Total no. of spaces in the sentence = ",res3)

# Output: -
# Total no. of spaces in the sentence =  5