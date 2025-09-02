#first program on usecase of type function
e=1
e=e+1

print(type(e))

e='image'
print(type(e))

x = True
print(type(x))       

#conversion from float to int

a=1.2 
a=int(a)
print(type (int(a)))
print(a)

#conversion from int to float

a=1
a=float(a)
print(type (float(a)))
print(a)

#string conversion

name='123'
type(name)
print(type(name))

name=int(name)
print (type(name+1))
print(type(name))
print(name+1)

#input function

name=input('Enter your name')
print('Hello',name)

#converting user input
inp=input('which floor are you on?')
usf=int(inp)+1
print('You will be on',usf,'floor after taking the lift')

#Write a program that uses input to prompt a user for their name and then welcomes them.
name=input('enter your namae')
print('welconme',name)

#write a program to prompt the user for hours and rate per hour to compute gross pay.

hour_str=input("hour worked")
hour_num=float(hour_str)
rph=2.75
gross_pay=hour_num*rph
print("your gross pay is :",gross_pay)

# adding two strings taking  input from user

firstname=input("whats your first name ")
lastname=input("whtas your last name ")
spacestring=(' ')
fullname=firstname+spacestring+lastname
print(fullname ) 


