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
    def __init__(self, brand, model, year):
        # This part was perfect. It sets up the object's properties.
        self.brand = brand
        self.model = model
        self.year = year
        self.is_engine_on = False  # Engine is always off for a new car.

    def start_engine(self):
        # This method's job is to change the state. No need to check what car it is.
        # It just turns its own engine on.
        self.is_engine_on = True
        print(f"The {self.brand} {self.model}'s engine is now on.")

    def stop_engine(self):
        # This method also just changes its own state.
        self.is_engine_on = False
        print(f"The {self.brand} {self.model}'s engine is now off.")

    def get_info(self):
        # This method returns a description of the car's current state.
        engine_status = "on" if self.is_engine_on else "off"
        return f"A {self.year} {self.brand} {self.model}. The engine is {engine_status}."
    
    # Create an instance of the Car class
my_car = Car("Ford", "Mustang", 2024)

# Check the initial state
print(my_car.get_info())
# Expected Output: A 2024 Ford Mustang. The engine is off.

# Call a method to change the state
my_car.start_engine()
# Expected Output: The Ford Mustang's engine is now on.

# Check the new state
print(my_car.get_info())
# Expected Output: A 2024 Ford Mustang. The engine is on.

# Change the state again
my_car.stop_engine()
# Expected Output: The Ford Mustang's engine is now off.
           
#pracitce question 
             
## The smart_lightbulb Challenge 💡
#Your goal is to create a class for a smart lightbulb. 
#A smart light can be turned on or off, and you can change its brightness.    

class smart_lightbulb:
    def __init__(self,location):
        self.is_on = False
        self.brightness=100
        self.location=location
        
            
    def turn_on(self):
        self.is_on=True
        print(f"your bulb in {self.location} is on as of now ")

    def turn_off(self):
        self.is_on=False
        print(f"your bulb in {self.location} is off as of now ")

    def set_brightness(self,brightness):
        if self.is_on is True:
            if brightness>0 and brightness<100:
                self.brightness = brightness
                print(f"Action: Brightness set to {brightness}%.")
            else:
                # If it's invalid, print a warning and do nothing else
                print(f"Action: Invalid brightness {brightness}%. Brightness remains {self.brightness}%.")

    
           
             

    def  get_status(self):
        
        if self.is_on==True:
                return(f'the {self.location} light is "ON" with {self.brightness}% brightness')

        else :
            return(f'the {self.location} light is "off" ')


print("--- Starting Test ---")

# 1. Create the light and check initial status
kitchen_light = smart_lightbulb("Kitchen")
print(kitchen_light.get_status())
print("-" * 20)

# 2. Turn it on and check the status
kitchen_light.turn_on()
print(kitchen_light.get_status())
print("-" * 20)

# 3. Set a valid brightness and check
kitchen_light.set_brightness(60)
print(kitchen_light.get_status())
print("-" * 20)

# 4. Turn it off, then try to set brightness (should be ignored)
kitchen_light.turn_off()
kitchen_light.set_brightness(40) # This action should be ignored
print(kitchen_light.get_status()) # Brightness should still be 60 if we turn it back on
print("-" * 20)

# 5. Turn it on again and check if old brightness was remembered
kitchen_light.turn_on()
print(kitchen_light.get_status())
print("-" * 20)

# 6. Try to set an invalid brightness (should be rejected)
kitchen_light.set_brightness(150) # This action should be rejected
print(kitchen_light.get_status()) # Brightness should still be 60

print("--- Test Complete ---")