#Accessing string elements with subscript operator ([])- A string manipulation operator
'''
- It retrieves the characters from a string as per the mentioned index. 
-SYNTAX:-
(i) For a particular character:-

 var1_name = "string"
 print(var1_name[index])
 
(ii) For a set of characters:-

 var1_name = "string"
 print(var1_name[starting_index:ending_index])
'''

#Example-1: to access a particular character of the string.
name = "Awesome"
a = name[0]
b = name[1]
c = name[2]
d = name[3]
e = name[4]
f = name[5]
g = name[6]
print(a,b,c,d,e,f,g)    #Output: A w e s o m e

#Example-2: to access characters of a string of particular range.
name = "Awesome"
h = name[0:5]
i = name[1:6]
j = name[2:3]
k = name[2:7]
print(h)    #Output: Aweso
print(i)    #Output: wesom
print(j)    #Output: e
print(k)    #Output: esome

'''
Note:-
- In Example 2, the outputs will include the characters from starting index to ending_index - 1
'''

#Example 3: to access characters from 0th index onwards.
name = "Awesome"
l = name[0:]
o = name[1:]
p = name[3:]
print(l)    #Output: Awesome
print(o)    #Output: wesome
print(p)    #Output: some

'''
Note:-
- In Example 3, the outputs will include the characters from starting index to end of the string.
'''

#Example 4: to access characters till a particular index. 
name = "Awesome"
m = name[:6]    #to access characters till 5th index 
n = name[:7]    #to access characters till 6th index
q = name[:5]    #to access characters till 4th index
r = name[:2]    #to access characters till 1st index
print(m)    #Output: Awesom
print(n)    #Output: Awesome
print(q)    #Output: Aweso
print(r)    #Output: Aw

'''
Note:-
- In Example 4, the outputs will include the characters from starting index to ending_index - 1
'''