'''
Tuples:-
- A tuple is an immutable sequence of values.
- The sequence is ordered.
- It allows duplicates within a single tuple.
- It also allows multiple data types elements within a single tuple (heterogeneous property).

- SYNTAX:-
- 1. tuple_name = (element1, element2,...,element n)
- 2. tuple_name = element1, element2,...,element n
- 3. tuple_name = tuple([element1, element2, element n])  (only 1 iterable allowed)
'''

#Creating our 1st tuple:-
tuple1 = (101,'Anita','HR',37)
print(tuple1)    #Output: (101, 'Anita', 'HR', 37)

#2nd tuple:-
tuple2 = 103,'Abhi','IT',45
print(tuple2)    #Output: (103, 'Abhi', 'IT', 45)

#Creating an Empty Tuple:-
tuple3 = ()
print(tuple3)    #Output: ()