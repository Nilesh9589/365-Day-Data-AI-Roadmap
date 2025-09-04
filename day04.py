#practice  Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, 
# and prints Greetings! if anything else is stored in spam.
"""spam=input("<")
try :
    spam=int(spam)
    if spam==1:
        print("hello")
    elif spam==2:
        print("howdy")

except:
    print("greeting for the day")"""

#Write a program that:
#Asks the user for their age.
#Prints “Child”, “Teenager”, “Adult”, or “Senior” depending on age.    
"""print("hey user whats your age")
user=input("enter your age")
try:
   user=float(user)
   if user<=0:
      print("are you fool?, why do you exist")
   elif user>=0 and user<1:
      print("you are a infant bro")
   elif user<=12 and user>1:
      print("you are a child bro")
   elif user>12 and user<=17:
     print("study you are teen now")
   elif user>17 and user<=27:
     print("you are a adult now chess!")
   elif user>27 and user<=110:
      print("you are an senior citizen chill")
   elif user>110:
      print("just for god sake , remeber god names")       
except :
    print("enter correct age you fool")   """ 


"""Write a loop that prints numbers 1–20, but:

Replace multiples of 3 with "Fizz",

Multiples of 5 with "Buzz",

Multiples of both 3 and 5 with "FizzBuzz"."""

#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


""" this was my code 
num=20

while num<=20 and num>0:

    
    if num%3==0:
     print("fizz")
    if num%5==0:
     print("buzz")
    if num%3==0 and num%5==0:
      print("fizzbuzz")
    elif num%3!=0 and num%5!=0:
      print(num)
    num=num-1 
   """

#this is the logic required 

num = 20

while num <= 20 and num > 0:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num = num - 1

#def function at use
def name():
    print("my name is nilesh")
    print("my class is noob")
    print("this is the haard phase of life")

name()

#max and min functions

name=min("nilesh","mukati")
print(name)


name=max("nilesh","mukati")
print(name)

#lets call out def function

x=5
def listz():
    print("my name is nilesh")
    print("hey budz")
print(x)

#see it didnt print def listz because we havent invoke it yet now lets invoke it

listz()

#lets see how paramter work in a function\
choose=input("<")
choose=int(choose)
def nilesh(choose):
    if choose==1:
        print("one")
    elif choose==2:
        print("two")
    elif choose==3:
        print("three")  
    else :
        print("nothing")

nilesh(choose)

#lets see how return work in the function case
choose=input("<")
choose=int(choose)
def nilesh(choose):
    if choose==1:
        return "one"
    elif choose==2:
        return "two"
    elif choose==3:
       return "three" 
    else :
        return "nothing"

igotu=nilesh(choose)
print(igotu)