'''
Set methods in Python:-

1. add()
   - Used to add a single element in a set.
   - SYNTAX: set_name.add(element)        -> It takes exactly 1 argument.

2. clear()
   - Removes all the items from the Set and makes the set empty.
   - SYNTAX: set_name.clear()

3. pop()
   - It removes and returns an arbitrary element.
   - Raises KeyError if the set is empty.
   - SYNTAX: variable_name = set_name.pop()

4. remove()
   - Used to remove an element from the Set.
   - Raises KeyError if the element is not found in the Set.
   - SYNTAX: set_name.remove(element)

5. discard()
   - Also removes an item from the set.
   - But, unlike remove(), it won't raise an error if the element mentioned to remove is not there in the set.
   - Instead, the set remains unchanged.
   - SYNTAX: set_name.discard(element)

6. update()
   - Adds 1+ elements to a set.
   - Possible for iterables.
   - For dictionaries, only key is added.
   - SYNTAX: set_name.update(iterable)

'''

'''
Also: -

set() 
   - It is Constructor function.
   - Another way of creating sets.
   - SYNTAX: 1. set_name = set()
             2. set_name = set(iterable)
'''