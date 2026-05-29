'''
Below are the List Methods we use in Python:-

1. list()
-It is another way of creating lists in Python.
- SYNTAX:
  1. For empty list: list_name = list()
  2. For non-empty list: list_name = list([element-1, element-2,...., element-n])  

2. append()
- Adds a new element to the existing list.
- If another list is added, then this leads to a nested list.
- SYNTAX: list_name.append(element)

3. extend()
- Expands the existing list.
- All elements are separate. 
- SYNTAX: list_name.extend(iterable)

4. index()
- It returns the starting index of the element mentioned in the parentheses.
- Raises ValueError if the element is not in the list.
- SYNTAX: list_name.index(element)

5. insert()
- It inserts the given element into an existing List.
- SYNTAX: list_name.insert(index_no,element)

6. pop()
- It removes and returns the element at the specified index.
- If no element is given then it removes the last value.
- SYNTAX: list_name.pop(index_of_the_element)  

7. remove()
- It removes the 1st occurrence of the specified element from the list.
- SYNTAX: list_name.remove(element) 

8. reverse()
- It reverses the order of elements in a list.
- SYNTAX: list_name.reverse()

9. count()
- Counts the occurrence of an element in a list.
- SYNTAX: list_name.count(element)

10. sort()
- Sorts the given list in ascending or descending order.
- SYNTAX:
  1. For sorting in Ascending order: list_name.sort()
  2. For sorting in Descending order: list_name.sort(reverse=True)

11. clear()
- It removes all the elements from the list.
- SYNTAX: list_name.clear()

12. copy()
- It creates a shallow copy of the list.
- SYNTAX: list_name.copy() 
'''