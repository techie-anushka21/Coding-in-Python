'''
List of Dictionary Methods in Python:-

1. get()
- Used to access the value of the specified key.
- Does not raise error if key is not found.
- SYNTAX: variable_name = dictionary_name.get(key)

2. items()
- Extracts key and value of a Dictionary.
- Helps in looping through a Dictionary.

3. pop()
- Removes the specified key from the dictionary.
- Returns the value associated with that key.
- SYNTAX: value = dictionary_name.pop(key)

4. popitem()
- It removes and returns the last inserted key-value in the dictionary.
- SYNTAX: key,value = dictionary_name.popitem()
          print(key,value)

5. clear()
- Clears the dictionary.
- Empties the dictionary but keeps the variable.
- SYNTAX: dictionary_name.clear()

6. copy()
- Copies the key-value pairs of 1 dictionary to another.
- It creates a shallow copy.
- SYNTAX: new_dictionary_name = original_dictionary_name.copy()

7. keys()
- Returns all the keys of the Dictionary.

8. values()
- Returns all the values of the Dictionary.

9. update()
- Used to add new key-value pairs or update existing values in a dictionary.
- SYNTAX: dictionary_name.update({key:value})
'''

'''
Also: -

i. dict()
- It is a built-in Constructor function.
- It is used to create a new dictionary object from an iterable or sequence of key:value pairs.
-SYNTAX: dictionary_name = dict(key1 = value1, key2 = value2) 
    OR-> dictionary_name = dict(iterable)

ii. del Statement
- Used to delete a specified key-value pair from the dictionary.
- It does not return any value.
- Can delete the entire dictionary also, after which NameError occurs as the variable 
  itself no longer exists.
- SYNTAX: del dictionary_name[key]

iii. Dictionary Union (| operator) :-
- They are used to combine 2 or more dictionaries.
- SYNTAX = dictionary1 | dictionary2
- Note: If you try to make a union of 2 dictionaries but their keys are same, then the key-value 
 obtained in the output will be of the right-hand side dictionary.

'''