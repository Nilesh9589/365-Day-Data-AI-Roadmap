friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
contibution=[999,454,888,787,48,8,988]
friendname=friends[0]
friendcontribution=contibution[0]
mergelist=[friendname,friendcontribution]
print(mergelist)

#Just like strings, we can get at any single element in a list using an
#index specified in square brackets

friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
print(friends[0:])

#lists are mutable and strings are not means content cant be changed once assigned 

fruit='banana'
print(fruit[0])   #here the print gets to first character of string that is b .
#fruit[0]='a'   #here we are trying to check if sting content can be changed once assigned 
#print(fruit[0]) #TypeError: 'str' object does not support item assignment

#now lets check in case of a  string

friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
friends[0]='nilesh'
print(friends[0]) #here nilesh got printed means list was changed with element 

#to check how long is a list 

lists=[0,1,2,3,4,5,89,9,45,98,45,498,98,779,95,9, ]
print(len(lists)) #here 16 is prited which tell how many elements present in above list no space is counted like string.

#range function 1. range(stop)

for number in range(5):
    print(number)  #print the number from 0 to 4 not including the 5.

#2.range(start, stop)

for number in range(2,6): # Generate numbers from 2 up to (but not including) 6
    print(number)

#3.range(start, stop, step)

for number in range(0,10,2): #This generates numbers from start to stop, incrementing by the step value each time.
        print(number)

#main use is to repeat the for loop

for time in range(3):
     print("hello")

#Accessing list elements by index.
#You can combine range() with len() to get the index for each element in a list.   
friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
for check in range(len(friends)):
     print(f"friend at index{check} is {friends[check]}") 

#concatenating lists using plus
list1=[1,2,3,2,4,5]
friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
list3=list1+friends
print(list3)

#list slicing 
list1=[1,2,3,4,5]
print(list1[0:2])
print(list1[:])

#building a list from scratch
stuff=list()   #this list() create a new empty list
stuff.append('aish') #append need to be called to add the elements of the list
stuff.append(4)
print(stuff[:])

#is something in  my list

lists=[1,23,4,5,6,78,8]
for some in lists: 
     if some==8:
          print(True)
if 58 not in lists:
    print(True)      

#list ordering using sort()
friends=['vasu','bhushan','harsh','kanwaljeet','aditya']
friends.sort()
print(friends)

#built in functions and list
num=[1,85,9,6,12,9,9,156,9]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))
#exercise  to find average of the num entered by user and press done once to get exit 


numlist = [] # A simpler way to create an empty list

# Part 1: Collect all inputs and add them to the list
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == 'done':
        break # Exit the input loop
    
    try:
        number = float(user_input)
        numlist.append(number) # Add the converted number to the list
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Part 2: Process the list you created
total = 0
for num in numlist:
    total = total + num

# Calculate the final average
if len(numlist) > 0:
    average = total / len(numlist)
    print(f"/nYour list: {numlist}")
    print(f"Your average value is {average}")
else:
    print("No numbers were entered.")

#best friends string and list 
#split()
abc='with three words ,    '  
split=abc.split()# split breaks the string into individual words and give the list of words
print(split)

#example of split in action stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

sentence='stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
spl=sentence.split()
print(spl)

#opening email from file using split functon/
file_path='D:/365-Day-Data-AI-Roadmap/notes/mbox-short.txt'
search_term='from'
try:
     with open(file_path,"r") as file:
          for line_number, line in enumerate(file, 1):
            # Check if the search term is in the current line
            if search_term in line:
                print(f"Found '{search_term}' on line number: {line_number}")
                
                # Print the line itself (using .strip() to remove extra whitespace)
                print(f"Line content: {line.strip()}")
                print("---") # Add a separator

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#double split pattern 
email='stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words=email.split()
piece=words[0]
piece=piece.split('@') #['stephen.marquard', 'uct.ac.za'] would be priented 

print(piece)

#the guardian pattern
file_path='D:/365-Day-Data-AI-Roadmap/notes/mbox-short.txt'
try:
    with open(file_path,'r') as file:
        for line in file:
         line=line.rstrip()
         words=line.split()
         #guardian 
         if len(words)<3 or words[0]!='From':
             continue
         print(words[2])
except FileNotFoundError:
    print(f'your {file_path} not found')        

#D:/365-Day-Data-AI-Roadmap/notes/romeo.txt
file_path='D:/365-Day-Data-AI-Roadmap/notes/romeo.txt'
unique_senders=[]
print("trying to access the file")

newlist=[]

try:
    with open(file_path,'r') as file:
        for line in file:
            line=line.rstrip()
            words=line.split()
            
            for word in words :
             if word not in newlist:
                newlist.append(word)
    newlist.sort()            
    print(newlist)                       
except:
    print(f'unable to view the {file_path}')            

#exercisw 2 for today

