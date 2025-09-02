"""What is your name? >Nilesh
What year were you born in? >1995
Your name has 6 characters.
You are approximately 30 years old.

What is your favorite number (e.g., 3.14)? >27.8
Your favorite number is 27.8, and rounded it is 28.
You are 20 years away from 50.

--- Summary ---
Hello Nilesh, you are 30 years old and your name is 6 letters long."""
print("what is your name ?")
name=input(">")


print("What year were you born in?")
year=input()

year=int(year)
print("your name has ", len(name) , "characters",".")
yearold=2025-year
print("you are approximately", yearold ,"yearold" )
print("What is your favorite number (e.g., 3.14)")
favnum=input()
favnum=float(favnum)
print("Your favorite number is" , favnum , "and rounded it is " , round(favnum,1))
yearaway=50-yearold
print("you are " , yearaway , "from 50" )
print("--- Summary ---")
print("hello", name ,"," ,"you are ",yearold ," and your name is" ,len(name) , "letter long." )



