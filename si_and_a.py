#read principle, rate, time then calculate simple interest and amount.

p = float(input("Enter Principle: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
print("Values entered:-")
print("Principle =",p)
print("Rate =",r)
print("Time =",t)
si = (p*r*t)/100
a = p+si
print("Simple interest =",si)
print("Amount =",a)

'''
Output:-

Enter Principle: 75000.0
Enter Rate: 5.6
Enter Time: 4.5
Values entered:-
Principle = 75000.0
Rate = 5.6
Time = 4.5
Simple interest = 18900.0
Amount = 93900.0
'''