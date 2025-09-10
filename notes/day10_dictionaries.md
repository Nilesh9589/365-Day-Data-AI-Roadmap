Dictionary: 
          Dictionaries are used to store data values in key:value pairs.
          A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
          syntax:
                 Dictionaries are written with curly brackets, and have keys and values:
                  Dictionary items are ordered, changeable, and do not allow duplicates. refer example 2(for duplicacy)
          Ordered or Unordered?:
                 When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.(refer example 3)
                Unordered means that the items do not have a defined order, you cannot refer to an item by using an in dex.
          Dictionary Length:
                To determine how many items a dictionary has, use the len() function:(example 5)    
          Dictionary Items - Data Types:
                The values in dictionary items can be of any data type:
          type():
                 from Python's perspective, dictionaries are defined as objects with the data type 'dict':
                <class 'dict'>       
          T he dict() Constructor:
                It is also poss ible to use the dict() constructor to make a dictionary.(example6)
 
important:
         Python Collections (Arrays)
         There are four collection data types in the Python programming language:
         List is a collection which is ordered and changeable. Allows duplicate members.
         Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
         Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
         Dictionary is a collection which is ordered** and changeable. No duplicate members.          

Accessing Items:
        You can access the items of a dictionary by referring to its key name, inside square brackets:
        There is also a method called get() that will give you the same result:(example 7)

Get Keys:
        The keys() method will return a list of all the keys in the dictionary. (example8)

Get Values: 
         The values() method will return a list of all the values in the dictionary. (example9)
Get Items:
         The items() method will return each item in a dictionary, as tuples in a list.(example 10)

Check if Key Exists:
          To determine if a specified key is present in a dictionary use the in keyword:(example11)

Change Values:
          You can change the value of a specific item by referring to its key name:    (example12)     

Update Dictionary: 
          The update() method will update the dictionary with the items from the given argument. 
          The argument must be a dictionary, or an iterable object with key:value pairs. (example 13)
Adding Items:
           Adding an item to the dictionary is done by using **a new index key ** and assigning a value to it(example 14)
Removing Items
           There are several methods to remove items from a dictionary:
The pop() method:
            removes the item with the specified key name:      (example 15)
The popitem() method:
            removes the last inserted item                     (example 16) 
The del keyword:
            removes the item with the specified key name:   (examplpe 17)
            The del keyword can also delete the dictionary completely:
The clear() method empties the dictionary:  (example 18)

Loop Through a Dictionary:
            You can loop through a dictionary by using a for loop.
            When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.  (example 19)
            