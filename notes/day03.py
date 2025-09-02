x=5
if x>4:
 print("greater")
if x<4:
 print("smalller")


#comparison operators


x=5
if x==5:
    print("x is equal")

if x>4:
    print("greater than 4")

if x>=5:
    print("greater than or equal to 5") 

if x<6:
    print("x is less than 6")

if x<=5:
   print("x is less than or equal to 5")

if x!=6:
   print("not equal to 6")       

 #intend and deintend 

x=42
if x>1:
   print("more than one")
   if x<100:
      print("less than hundred")
print("all over and out")      

#

x=4
if x>2:
   print("x is bigger") 
else:
      print("x is smaller")
      

#if elsif and else


x=0
if x<2:
   print("x is small")   #even if one out of if and elif is true that would be printed
elif x<8:
   print("x is medium")
else:
   print("x is large")

print(" all out .")


#try and except 

print("enter a number")

num=input(">")
try:
    num=int(num)
   
except ValueError:
    num=0

if num>1:
     print("nice work")

else:
   print("enter a valid number")



# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above
# 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

print("enter the hour worked")
workhour=input(">")
workhour=float(workhour)


if workhour>40:
     rate=15
     print("good job your extra pay is ",workhour*rate)

elif workhour<40:
      rate=10
      print("your pay is", workhour*rate)     


# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above
# use try expect if user dont give number
      
print("enter the hour worked")
workhour=input(">")


try :

    workhour=float(workhour)      

    if workhour>40:
     rate=15
     print("good job your extra pay is ",workhour*rate)

    elif workhour<40:
      rate=10
      print("your pay is", workhour*rate)

   
except ValueError:
        print("enter a valid number") 