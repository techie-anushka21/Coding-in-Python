'''
Some specialities about strings in Python: -
'''

'''
1. string and integer can operate with '*'
'''

# Example 1: -
a = 2
b = 3
text = "@"
result = a*text*b
print(result)          # Output: @@@@@@


# Example 2: -
c = 4
d = 2
a_text = "#"
results = c*a_text*d*d
print(results)         # Output: ################


'''
2. string and string values can operate together with '+'
'''

# Example 3: -
e = "2"
f = 3
Txt = "@"

res = (e+Txt)
print(res)          # Output: 2@

a_res = ((e+Txt)*f)
print(a_res)        # Output: 2@2@2@


# Example 4: -
g = "4"
h = 2
Text = "#"

res2 = g+Text+g
print(res2)          # Output: 4#4

res3 = res2*h
print(res3)          # Output: 4#44#4