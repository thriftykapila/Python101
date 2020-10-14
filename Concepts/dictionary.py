# -*- coding: utf-8 -*-
"""

Contributed by @SowmyaaRamesh 
Dictionary in Python 
A dictionary is an unordered collection in which the items are stored as key value pairs. 
IMPORTANT: Dictionary keys must be immutable.
"""

# Creating dictionary with curly braces  
Dict = {1: "one", 2:"two"} 
print("Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict()
Dict[1] = "one"
Dict[2] = "two"
print("\nDictionary with the use of dict(): ") 
print(Dict) 

'''
Dictionary: 
{1: 'one', 2: 'two'}

Dictionary with the use of dict(): 
{1: 'one', 2: 'two'}
'''

#looping through a dictionary
#printing keys 
for x in Dict:
  print(x, Dict[x])


for key,value in Dict.items():
  print(key, value)

'''
Both the above loops give the same output:

1 one
2 two
'''

# Deleting elements in a dictionary

# using del
del Dict[1]
print("After deleting element with key 1:", Dict)

'''
After deleting element with key 1: {2: 'two'}

'''

#using clear()
Dict.clear()

print("After deleting all elements:", Dict)

'''
After deleting all elements: {}
'''
