#Objective: Build a Python script (expense_tracker.py) that:

#Stores at least 3 expenses using variables (e.g., category and amount).
#Performs calculations (e.g., total expenses, tax) using expressions.
#Prints a formatted expense report using statements.
"""Tell me your name: Alex
Hi, Alex
First is food
What's your order? pizza
You ordered: pizza

Second is travel
How did you travel? bus
Okay, so you used bus

Third is rent
How much was rent? 500
Okay, so you gave $ 500.0

Expense Report for Alex
-------------------
Category: pizza      | Amount: $80.00 | Tax: $8.00 | Total: $88.00
Category: bus        | Amount: $120.00 | Tax: $18.00 | Total: $138.00
Category: rent       | Amount: $500.00 | Tax: $75.00 | Total: $575.00
-------------------
Total Expense: $801.00
Summary: Alex spent $801.00 on pizza, bus, and rent."""
user= input("tell me your name : ")
print("hi ", user)
print("first is food")
category=input("whats your order")
print("you ordered", category)
print("price of the food is 80")
price=80.0
#tax would be 10 percent 
tax=price*0.10
total_price=float(price+tax)
print("okay so total price after tax is",total_price)

print("second is travel")
category_01=input("how did you travel")
print ("okay so you used ", category_01)
price_01=120
print("price of the" ,category_01, "is" ,price_01)
#tax would be 10 percent

tax_01=price_01*0.10
total_price01=(price_01+tax_01)
print("so the total price after tax would be",total_price01)

print("third is rent")
print("how much was rent")
category_02=input()
try:
    rent = float(category_02)
    print("okay so you gave ", float(rent))  # Redundant float()
    price_02 = float(rent)
    tax_02 = float(price_02 * 0.10)
    total_price02 = (float(price_02 + tax_02))
    print("so the total price after tax would be", total_price02)
    pass  # Unnecessary
except ValueError:
    print("Error: Invalid rent amount. Setting rent to $0.")
    price_02 = 0.0
    tax_02 = 0.0
    total_price02 = 0.0
    print("So the total price after tax would be $", round(total_price02, 2))



#total expense

print("expense report for",user)

totalexpense=total_price+total_price01+total_price02


print("-------------------")
print("\nExpense Report for", user)
print("-------------------")
print("Category:", category, "| Amount: $", round(price, 2), "| Tax: $", round(tax, 2), "| Total: $", round(total_price, 2))
print("Category:", category_01, "| Amount: $", round(price_01, 2), "| Tax: $", round(tax_01, 2), "| Total: $", round(total_price01, 2))
print("Category: ","rent" ,     "| Amount: $", round(price_02, 2), "| Tax: $", round(tax_02, 2), "| Total: $", round(total_price02, 2))
print("-------------------")
print("Total Expense: $", round(totalexpense, 2))
print("Summary:", user, "spent $", round(totalexpense, 2), "on", category, ",", category_01, ", and", " rent")

