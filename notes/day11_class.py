class dog:
    species = "Canis familiaris" #class attrtibute
    def __init__(self,name,age):
        self.name = name #creates an attribute called name and assigns the value of the name parameter to it.
        self.age = age #creates an attribute called age and assigns the value of the age parameter to it.

    def show(self):
        print(f'basic {self.name} and {self.age} are' )   

miles = dog("Miles", 4) #milees and buddy is object havinf all poweer of class dog 
buddy = dog("Buddy", 9)       


print (miles.species)#see object miles can access even class attribute or function everything
miles.show()  #shows the name and age 


#exercise  for Create a Transaction, set amount and type, create a method to display info.

class Transaction:
    def __init__(self,amount,type):
        self.amount=amount
        self.type=type


    def getinfo(self):
        print(f"your amount for this transaction is {self.amount}")
        print(f"your transaction is of type {self.type} ")

my_transaction=Transaction(5000,'credit')
my_transaction.getinfo()

        

#lets do it claude way

class Account:
    def __init__(self,startingbalance=0):#why have we use staring balance here cant we directly put inside self.balnce=startingbalance=0
        self.balance=startingbalance#why not self.balance=startingbalance
        self.history=[]#why history was not mentioned above as     def __init__(self,startingbalance=0,history)

    def deposit(self,amount):#why amount not mentioned in def__inti__()
        self.balance=self.balance+amount
        self.history.append({"type": "credit", "amount": amount})#why not self.history.append({self.balance})

    def withdraw(self,amount):
        if amount>self.balance:#how self.balance got updated even though it was inside function def deposit()
            raise ValueError("Insufficient funds")
        self.balance -= amount #what this means 
        self.history.append({"type": "debit", "amount": amount})   

    def get_balance(self):
        return self.balance    
# Usage:
account1 = Account(1000)        #where this thousand will go?
account1.deposit(250)           # Add $250
account1.withdraw(150)          # Remove $150
print(f"Final balance: ${account1.get_balance()}")  # Check balance

#another example

class Car:
   def __init__(self, brand, model):
       self.brand=brand
       self.model=model
    
       self.is_engine_on = False

   def start_engine(self):
       
       if self.model=='1tesla' & self.brand=="tesla":
           self.is_engine_on=True
           print("engine is on ")
 

   def stop_engine(self):
       
       if self.model=='2tesla' & self.brand=="tesla":
           self.is_engine_on=False
           print("engine is off")


   def get_info(self):
       if self.is_engine_on ==True:
        print(f"the model and brand u selected is {self.model,self.brand} and its engine is on") 
       else:
           print(f"the model and brand u selected is {self.model,self.brand} and its engine is off") 

myselection=Car('tesla','1tesla')        
myselection.get_info() 
           
 
             
        

            

        


