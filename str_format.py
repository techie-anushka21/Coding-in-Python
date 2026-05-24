'''
String functions- format() : it formats the string.
- SYNTAX: -
  "{}, {}, ....".format(argument-1, argument-2, ....)
'''

#Example 1
a = "My name is {}."
res = a.format("Eisha")
print(res)

# Output: -
# My name is Eisha.


#Example 2
b = "I am {} years old."
res2 = b.format(23)
print(res2)

# Output: -
# I am 23 years old.


#Example 3: -
c = "My name is {} and I am {} years old."
res3 = c.format("Eisha",23)
print(res3)

# Output: -
# My name is Eisha and I am 23 years old.