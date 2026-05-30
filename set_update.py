#Example:-
city_set = {"Pune","Mumbai","Hyderabad","Bangalore"}
print(city_set)
#Output: {'Pune', 'Mumbai', 'Bangalore', 'Hyderabad'}

city_set.update(["Kolkata"])
print(city_set)
#Output: {'Hyderabad', 'Pune', 'Bangalore', 'Mumbai', 'Kolkata'}

city_set.update(("Shimla","Lucknow"))
print(city_set)
#Output: {'Bangalore', 'Mumbai', 'Kolkata', 'Lucknow', 'Pune', 'Shimla', 'Hyderabad'}

# Do not implement a simple string else Output will be: -
city_set.update("Goa")
print(city_set)    
# Output: -

# {'Mumbai', 'Kolkata', 'Lucknow', 'Bangalore', 'G', 'Shimla', 'Pune', 'o', 'Hyderabad', 'a'}

'''
Note: The outputs mentioned are possible outputs, not guaranteed (you might get a different 
      order of output).
'''