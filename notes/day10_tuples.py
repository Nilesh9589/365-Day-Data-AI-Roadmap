#example01 A tuple is a collection which is ordered and unchangeable.
thistuple=('radhe','shyam','sundar')
print(thistuple)
#example02 duplicay of data and indexing
thistuple=("radhe",'radhe','shyam','hare','krishna','hare','ram')
print(thistuple) #duplicate data is allowed

thistuple=("radhe",'radhe','shyam','hare','krishna','hare','ram') 
print(thistuple[-1])#for indexing see  this


#example03 length of tuple

thistuple=('radhe','krishna','radhe','shyam')
print(len(thistuple)) #this prints the length of the tuple

#example04 creating tuple with one item only

thistuple=('radhe',)
print(type(thistuple)) #this is classed as tuple 

#example05 creating tuple using constuctor tuple()
thistuple=tuple(('radhe','shyam'))#remeber to use double round bracket
print(thistuple)

#example 06 ranging of the indexing
thistuple=('radhe','krishna','radhe','shyam')
print(thistuple[1:4]) #The search will start at index 1 (included) and end at index 4 (not included)
#By leaving out the start value, the range will start at the first item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:-5:-1])#The search will start at index -1 (included) and end at index -5 (not included)

#example07 Check if Item Exists
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if 'apple' in thistuple:
    print(True)

#example08 unpacking tuple 
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)   

#example 09 using * for less variable than values
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#example 10 using * to another variaqble than the last

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,*yellow,red)=fruits
print(green)
print(yellow)
print(red)

#example 11 to loop the tupple

thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

#example 12 loop through index using len and range()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i]) 

#example 13 using while loop 

thistuple = ("apple", "banana", "cherry")
i=0

while i<len(thistuple):
        print(thistuple[i])
        i=i+1


#knowledge checking 
#Create a tuple with (stock_name, price, change) and unpack it into 3 variables.

stocklist=('reliance',50,'5%')
(stock_name,price,change)=stocklist
print(stocklist)
