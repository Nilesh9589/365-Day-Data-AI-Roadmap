student={"name": "john" , 'age':28 , 'course':["maths ","compsci"]}#[this are key:valuepairs]
print(student['age'])#to access the key use dictonaryname[nameofkey]

#example2
thisdict = {
  "brand": ["Ford","Ford"],
  "brand": ["Ford","plazo"],
  "model": "Mustang",
  "year": 1964
}
print(thisdict['brand'])#only once the brand would be called no duplicates 

#example3
student_grades={
               'nilesh':100,
               'vasu'  :120,
               'prashant':160,
               'bhushan':180,
               'harsh' :200
}

student_grades["jay"]=81#adding the new element As you can see, the original order of nilesh, vasu,etc  is preserved,
                         #and jay is added to the end. The order is reliable.
print(student_grades)

#example 4 Unordered Example: Python Sets 🎲
"""Sets are the classic example of an unordered collection. They do not maintain any specific order,
and you cannot use an index to access their elements."""

market_list={'tomato',81,'onion',91,'garlic',190}
print(market_list)#The printed order is not guaranteed to match the insertion order.
try:
    print(market_list[0]) # Trying to access an element by index will fail.
except TypeError as e:
    print(f"\nError when trying to use an index: {e}")    


#example 5 length of dictionary
 
student_grades={
               'nilesh':100,
               'vasu'  :120,
               'prashant':160,
               'bhushan':180,
               'harsh' :200
}

print(len(student_grades))

#example 6 dictionary using dict()constructor

thisdictionary=dict(name='john',age=18,employed='NO')
print(thisdictionary['name'])

#example 7 get() 
detail=dict(name='ayush',age=18,classes=12)
thiss=detail.get('name')
print(thiss)

#example08 key()
details={
        'name':'ayush',
         'age':18,
         'class':12
}
print(details.keys()) #this return only names of the keys present not value remember

#example 09 values()

details={
        'name':'ayush',
         'age':18,
         'class':12
}
print(details.values()) #this return only values of the keys present not key themselves

#example10 items()

details={
        'name':'ayush',
         'age':18,
         'class':12
}
print(details.items())# will output both key and their values in the list

#example 11 check if key is present using in operator 
details={
        'name':'ayush',
         'age':18,
         'class':12
}
if "name" in details:  
    print(True)

#example12 change value by key name 
car_details={
          'name':'mustang',
          'model':'x5',
          'year':2020
}

car_details['year']=2024

print(car_details)

#example13 update ()

car_details={
          'name':'mustang',
          'model':'x5',
          'year':2020
}

car_details.update({'fav':'yes'})  #must enter both key and values
print(car_details)

#example adding new item using key and value

car_details=dict(car='mustang',year=2024)
car_details['age']=19
print(car_details)

#example 15  pop() to remove key and value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop('brand')
print(thisdict)

#example 16 popitem()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem()#always remobe the last item wih key 
print(thisdict)

#example 17  the del keyword

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"] #need to mention key only which u want to remove
del thisdict ##this will cause an error because "thisdict" no longer exists.
#print(thisdict)

#example 18 clear ()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #this will get empty liist {}
print(thisdict)

#example 19 looping the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
for i in thisdict:
    print(i)#this prints only the keys of the dictionary not values

#example Print all values in the dictionary, one by one: 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 

for i in thisdict:
    print(thisdict[i]) #this will prinnt only values 

#You can also use the values() method to return values of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
for i in thisdict.values():
    print(i)

#You can use the keys() method to return the keys of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
for i in thisdict.keys():
    print(i)

#Loop through both keys and values, by using the items() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 

for i in thisdict.items():
    print(i)

#exercise
#Create a dictionary with 3 stocks and their prices, then print each stock-price pair.

portfolio={
    
        "reliance":5000,
        "airtel":8000,
         "jio":9000
         
         }

for i in  portfolio.items():
    print(f"stocks and their price {i}")
            