name='nilesh'
age=25
salary=50000
is_employed=True
#string operation
full_name='Nilesh'+" "+'mukati'
greeting=print(f'Hi {name}  your full_name  is  {full_name} you are {age} year old your salary is {salary} you are emplyed? {is_employed}')

monthly_salary=(salary/12)

tax=salary*0.30
portfolio_value=1000000
numofstocks=30
averageprice=portfolio_value/numofstocks
print(f'your porfolio is worth {portfolio_value} ,you have {numofstocks} stocks whose average price is {averageprice}')

#stock price calculator 
stockprice=input("<price of your stock")


try:
    stockprice=float(stockprice)
    
    while True:
        if stockprice <2500:
            print("stock is less expensive")
        elif stockprice>2500:
            print("stock is more expensive")
        elif stockprice==2500:
            print("stock is okay")
      
        text=input("< if you want to exit press done else press continued")  
        if text=='done':
          break   
        elif text=="continued" :
            stockprice=float(input("<price of your stock"))
            continue


   
except:
    print("enter a vaild number boss")       

#A function that takes a list of stock prices and returns the average
sum=0
stockprice=[]
def averagestock():
   
   stockprice=[]
   for  i in range(5):
       stocks=input("<enter stock price")
       stockprice.append(stocks)
   return stockprice[:]


FINAL=averagestock()    

for i in FINAL:
  i=float(i)
  sum=float(i+sum)
average=sum/len(FINAL)
print( average)
   


 # A function to filter stocks above a certain price
stocks=['rel','infotech','wipro','google']
stockprice=[500,800,1200,999]
def checker():


    for check in stockprice:
       if check>300:
          print('normal')
       else:
            print("buy")    
    newstockprice=['normal'  if check>300  else 'buy'  for check in stockprice]
    print(newstockprice)

checker()    