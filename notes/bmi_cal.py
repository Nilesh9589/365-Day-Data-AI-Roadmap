"""The BMI (Body Mass Index) formula is as follows:
Metric Units: BMI = weight (kg) ÷ height (m²). 
2
US Units: BMI = weight (lb) ÷ height (inches)² * 703. 
1
To convert height from centimeters to meters, divide by 100. 
1
For example, if you weigh 70 kg and are 1.75 m tall, your BMI would be 70 ÷ (1.75)² = 22.86. 
1

This formula helps estimate body fat based on weight and height.
d(m) = d(ft) × 0.3048 + d(in) × 0.0254
"""

user=input(">your name"+" ")
print("hello"+" "+user+" "+"what is your weight in kg ")
weight=input(">type your weight"+" ")
print("okay, so your weight is "+ weight +"kg" )
print(">type your height"+" ")
feet=input("how much feet"+">")
inch=input("how much inch"+">")
print("okay so you are " + feet +","+ inch +  "tall")
print("so height in meter would be ")
feet=float(feet)
inch=float(inch)
heightm=float(feet*0.3048+inch*0.0254)
print(heightm)
weight=float(weight)
BMI=weight/(heightm**2)
print("your BMI would be" ,BMI)