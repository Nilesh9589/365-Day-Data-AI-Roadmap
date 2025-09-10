#example 01 

thisset = {"apple", "banana", "cherry"}
print(thisset)#Sets are unordered, so you cannot be sure in which order the items will appear,may change everytime

#example 02  Set items are unordered, unchangeable, and do not allow duplicate values.
nameoffriends={'nilesh','bhushan','harsh','prashant','jay','aish'}
print(nameoffriends)#unordered everytime order changes

nameoffriends={'nilesh','bhushan','harsh','prashant','jay','aish','aish','jay'}
print(nameoffriends)#duplicay not allowed it print name value only once.

#example 03 unchangeable means elements value wont change or replace but can add or remove,because they are unordered
nameoffriends={'nilesh','bhushan','harsh','prashant','jay','aish','aish','jay'}
nameoffriends.add('me')#adding of elemets allowed
nameoffriends.remove('me')#removing also randomly removes when pop use otherwise remove() removes exact
print(nameoffriends)

#example04 set() consturctor
nameoffriends=set(('aish',"bhushan",1,True))  #always use double colon or whatever
print(nameoffriends)

#example05 looping to see if accessible or not

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if item is present in the set:  
thisset = {"apple", "banana", "cherry"}
if 'banana' in thisset:
  print(True)

#example06 to add two list using update()

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

#example07 union 
#join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result

set1={'nilesh','bhushan','harsh'}
set2={'ram','radha','shyam'}
set3=set1|set2
print(set3)

#example08 using multiple sets for union

set1={'nilesh','bhushan','harsh'}
set2={'ram','radha','shyam'}
set3={'jay','shri','ram'}
set4={1,2,3,4,45,6}
myset=set1.union(set2,set3,set4)
print(myset)

#When using the | operator, separate the sets with more | operators:
set1={'nilesh','bhushan','harsh'}
set2={'ram','radha','shyam'}
set3={'jay','shri','ram'}
set4={1,2,3,4,45,6}
myset=set1 | set2|set3|set4
print(myset)

#example09 set and tuple or other data type of union
set1={'nilesh','bhushan','harsh'}
set2={'ram','radha','shyam'}
set3=(1,2,3,4,5,6,8)
set4={'name':'nilesh'
      ,'class':12}

mergelist=set2.union(set3,set4)
print(mergelist)

#Note: The  | operator only allows you to join sets with sets,
#  and not with other data types like you can with the  union() method.

#example10 the update() method 

set1 = {"a", "b" , "c",'c'}
set2 = {1, 2, 3}

set1.update(set2) #The update() method inserts the items in set2 into set1: not require new set to merge
print(set1)

#Note: Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c",'c'}
set2 = {1, 2, 3}
set3=set1.union(set2)
print(set3)

#example11 using intersection prints only duplicates

set1 = {"apple", "banana", "cherry"} #set
set2 = ("google", "microsoft", "apple")  #tuple 
set3=set1.intersection(set2)  #set and tuple 
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1 & (set2)   #cant intersect other than set data type
print(set3)

#example12 the intersection_update dont need extra set

set1 = {"apple", "banana", "cherry"} #set
set2 = ("google", "microsoft", "apple")  #tuple .
set1.intersection_update(set2)  #set and tuple 
print(set1)

#example13 the difference method()
set1 = {"apple", "banana", "cherry"} #set
set2 = ("google", "microsoft", "apple")  #tuple .
set3=set1.difference(set2) #Keep all items from set1 that are not in set2:
print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"} #set
set2 = {"google", "microsoft", "apple"}  #set .
set3=(set1)-(set2) #Keep all items from set1 that are not in set2:
print(set3)

#example14 difference_update 

#Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) 

#example15 symmetric difference
#Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"} #sets
set2 = ("google", "microsoft", "apple") #tuple
set3 = set1.symmetric_difference(set2)
print(set3)

#The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"} #sets
set2 = {"google", "microsoft", "apple"}#tuple
set1.symmetric_difference_update(set2)
print(set1)



#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"} #sets
set2 = {"google", "microsoft", "apple"} #sets
set3 = set1^(set2)
print(set3)

