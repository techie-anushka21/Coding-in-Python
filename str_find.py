"""
String functions- find() : it finds a substring from the given string.
- If string found: starting index of substring is returned
- If string not found: -1 value is returned.
"""

#Example 1: -
a = "The college is filled with talented students."
res = a.find("talented")
print(res)

# Output: -
# 27 (because "talented" is present in the string and starts from index no. 27.)


#Example 2
b = "Stuart Little is a very interesting and funny movie series."
res2 = b.find("Interesting")
print(res2)

#Output: -
# -1 (because "Interesting" is not present in the string, remember that Python is case-sensitive.)