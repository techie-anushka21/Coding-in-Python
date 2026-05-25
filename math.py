#math module in Python

#math.ceil()- rounds-up a number to the nearest integer.
import math
a = math.ceil(3.4)    # Output: 4
b = math.ceil(3.6)    # Output: 4
print(a,b)

#math.exp()- E raised to the power x.
c = math.exp(2)    # Output: 7.38905609893065
d = math.exp(4)    # Output: 54.598150033144236
print(c)
print(d)

#math.fabs()- Returns the absolute value(always +ve) of a number.
e = math.fabs(-7)      # Output: 7.0
f = math.fabs(-7.4)    # Output: 7.4
print(e)
print(f)

#math.factorial()- Returns the factorial of a number.
g = math.factorial(7)    # Output: 5040
h = math.factorial(4)    # Output: 24
print(g,h)

#math.floor()- rounds down a number to the nearest integer.
i = math.floor(5.4)    # Output: 5
j = math.floor(5.6)    # Output: 5
print(i,j)

#math.fmod()- calculates the remainder of 2 numbers.
l = math.fmod(6,2)      # Output: 0.0 
m = math.fmod(5.5,2)    # Output: 1.5
print(l,m)

#math.gcd()- calculates the greatest common divisor of 2 integers.
n = math.gcd(10,3)     # Output: 1
o = math.gcd(10,30)    # Output: 10
print(n,o)

#math.lcm()- calculates the least common multiple of 2 integers.
p = math.lcm(10,3)     # Output: 30
q = math.lcm(20,30)    # Output: 60
print(p,q)

#math.pow()- calculates the value of x to the power y (x^y).
r = math.pow(2,5)    # Output: 32.0
s = math.pow(3,7)    # Output: 2187.0
print(r,s)

#math.sqrt()- calculates the square root a number.
t = math.sqrt(9)      # Output: 3.0
u = math.sqrt(256)    # Output: 16.0
print(t,u)

#math.pi- calculates the value of pi.
print(math.pi)    # Output: 3.141592653589793


# Note: When math library is imported once, then you don't need to import it again in the same file for multiple functions.