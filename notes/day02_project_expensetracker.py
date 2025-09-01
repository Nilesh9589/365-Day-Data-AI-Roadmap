#Objective: Build a Python script (expense_tracker.py) that:

#Stores at least 3 expenses using variables (e.g., category and amount).
#Performs calculations (e.g., total expenses, tax) using expressions.
#Prints a formatted expense report using statements.

user= input("tell me your name ")
print("hi ", user)
expense01=print("first is food")
category=input("whats your order")
print(category)
price=80
#tax would be 10 percent 
tax=price*0.10
total_price=float(price+tax)
print(total_price)

expense01=print("second is travel")
category_01=input("how did you travel")
print ("okay so you used ", category_01)
price_01=120
#tax would be 15 percent

tax_01=price_01*0.15
total_price01=float(price_01+tax_01)
print(total_price01)

expense02=print("third is rent")
category_02=input("how much was rent")
print("okay so you gave ", float(category_02))
price_02=float(category_02)
#tax would be 15 percent

tax_02=float(price_02*0.15)
total_price02= (float(price_02+tax_02))
print(total_price02)


#total expense

totalexpense=total_price+total_price01+total_price02

print("your total expense is",totalexpense)

""""
 Here are your two main mistakes that i made

## Mistake #1: Mixing Up Storing and Printing
Mistake: You wrote code like total_price = print(price + tax).

Problem: This stores an empty value (None) in total_price, not the number. print() only displays things.

Solution: First, calculate and store the value. Then, print it on a new line.

❌ Wrong:
total = print(10 + 5)

✅ Right:

Python

total = 10 + 5
print(total)
## Mistake #2: Using the Wrong Variable
Mistake: Your travel tax calculation used the food price variable.

Problem: This gave an incorrect final total.

Solution: Always double-check that you are using the correct variable for the item you are calculating.

❌ Wrong:
travel_tax = food_price * 0.15

✅ Right:
travel_tax = travel_price * 0.15"""
