
"""4.6 Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Pay should be the normal rate for hours up to 40 and time-
and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to
do the computation of pay in a function called computepay() and use the function
to do the computation. The function should return a value. Use 45 hours and a
rate of 10.50 per hour to test the program (the pay should be 498.75). You should
use input to read a string and float() to convert the string to a number. Do not
worry about error checking the user input unless you want to - you can assume
the user types numbers properly. Do not name your variable sum or use the sum)
function."""
def computepay(hours, rate):
    if hours > 40:
        regularpay = 40 * rate
        overtimehour = hours - 40
        overtimepay = overtimehour * (1.5 * rate)
        totalpay = regularpay + overtimepay
    else:
        totalpay = hours * rate
    return totalpay

try:
    hours_worked = float(input("Enter Hours: "))
    rate_per_hour = float(input("Enter Rate: "))
    gross_pay = computepay(hours_worked, rate_per_hour)
    print("Pay:", gross_pay)

except ValueError:
    print("Error, please enter a numeric input.")
#return function practice
radius=float(input(">enter radius"))
def calculate_circle_area(radius):
    π=3.14
    r=radius
    area=float(π*r*r)
    return area

area=calculate_circle_area(radius)
height=float(input(">enter height"))
def calculate_cylinder_volume(area, height) :
    h=height
    V=area*h
    return V




volume=calculate_cylinder_volume(area,height)
print(volume)

#Challenge: Price Calculator with Discount and Tax
#Your goal is to calculate the final price of an item after first applying a discount and then adding a sales tax. 
# You must use two separate functions that work in sequence.

priceofitem=float(input("enter the price"))

discountpercent=float(input("enter discount you got"))
def discountfun(priceofitem,discountpercent):
    discountpercent=(100)*(discountpercent/100)
    newdiscountprice=priceofitem-discountpercent

    return newdiscountprice

price=discountfun(priceofitem,discountpercent)

tax_percent=float(input("whats the tax"))
def add_tax(price, tax_percent) :
    tax_percent=(tax_percent/100)*price
    finalprice=price+tax_percent
    return finalprice

final=add_tax(price,tax_percent)

print("your final price is", final)


