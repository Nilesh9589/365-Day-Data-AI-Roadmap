#breaking out of loop using break 
"""|
while True:
    bcoz=input("<")
    print("i am mad mad boy")

    if bcoz=="done":
        break
print("congrats you are out of this loop bud")"""    

#continue statement end the current iteration and jump top of the loop
#  and start next iteration
""" 
while True :
    line=input("<")
    if line[0]=='#':   #[0] check first character of user input
        continue
    if line=="done":
        break
    print(line)
print("done")    """ 

#for loop

for a in [1,2,3,4,5]:
    print(a)
print("long journey ahead")    

#for loop again

friends=["arpit","bhushan",'vasu','prashant','jay','kanwaljeet','aditya','ritik']
for friend in friends:
    print(friend)

print("sukh ke sb sathi dukh mai na koi")    

#looping through a set

print("before loop")
for thing in [1,5,9,15]:
    print(thing)

print("after loop")

#what is the largest number
largestyet=0
for largestnum in [1,5,9,18,26,89,4,56,5,5,5564,8,89,9]:
    if  largestnum>largestyet:
        largestyet=largestnum
print(largestyet)

#coutning in a loop

count=0
for counting in [5,4,84,9,84,9,12,65,9,894,555]:
    
        count=count+1

print(count)        
#averaging      
count = 0
sum = 0
print ('Before', count,sum)
for value in [9,41, 12, 3, 74, 151] :
    count = count + 1
    sum = sum + value
    print (count, sum,value)
print ('After', count, sum, sum / count)
       
#finding value using boolean
 
find=False

for findingvar in [1,8,9,8,48,98,7,815,8,5,9,4,9,1,21,6,89,4]:
     if findingvar==815:
         find=True
         break

print(find,findingvar) 


#finding smallest from list using None as a constant

smallest=None

for smallestsofar in [8,9,15,98,354,85,98,3]: 

     if smallest is None:
        smallest=smallestsofar
     elif smallestsofar<smallest :
         smallest=smallestsofar
         print(smallest)      

"""
Write a program that repeatedly prompts a user for integer numbers until the
user enters 'done'. Once 'done' is entered, print out the largest and smallest of the
numbers. If the user enters anything other than a valid number catch it with a
try/except and put out an appropriate message and ignore the number. 
"""
largestnum=0
smallestnum=1000       
while True:
    num=input("<")
    if num=="done":
        break
    
    try:
        num=int(num)
        

    except:
        print("enter a valid num")
        continue     

    if num>largestnum:
        largestnum=num
    if num<smallestnum:
        smallestnum=num

print("smallest,largest,",smallestnum,largestnum)            





      

             
