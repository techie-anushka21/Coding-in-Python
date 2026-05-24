"""
string functions- split() : it separates the substrings of a string with the given 
separator character (space or ,)
"""

#Example 1
a = "The people of a country must be united"
res = a.split(" ")    #Here the split will happen wherever there is a space in the string.
print(res)

# Output: -
# ['The', 'people', 'of', 'a', 'country', 'must', 'be', 'united']

#Example 2
b = "The people of a country must be united"
res2 = b.split(",")    #Here the split will happen wherever there is a comma.
print(res2)    
# Output: -
# ['The people of a country must be united']

#Note: splitting didn't happen here because there was no comma.

#Example 3
c = "The good, the bad, the ugly"
res3 = c.split(",")    #Here the split will happen wherever there is a comma.
print(res3)
# Output: -
# ['The good', ' the bad', ' the ugly']