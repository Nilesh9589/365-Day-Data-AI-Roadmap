"""🎯 Mini Project for Day 3
Project: ATM Simulator (basic)
Create a Python script (atm_simulator.py) that:
Starts with a balance (say ₹5000).
Asks the user if they want to check balance, deposit, or withdraw.
Performs the chosen action using if/else and updates balance.
Runs in a loop until the user chooses "exit"."""

balance=5000
print("what you want to do check balance , deposit or withdraw")
action=input("<").strip()

while action!="exit" :

    if action==("check balance"):
         print(balance)
         print("what you want to do check balance , deposit or withdraw , enter exit to close")
         action=input("<").strip()     
         
    elif action==('withdraw')  :
        print("how much to withdraw")
        withdraw=input("<").strip()
        withdraw=float(withdraw)
        balance = balance - withdraw
        print("updated balance is",balance)
        print("what you want to do check balance , deposit or withdraw , enter exit to close")
        action=input("<").strip()

    elif action==('deposit'):
        print("how much to depsoit")
        deposit=input("<").strip()
       
        deposit=float(deposit)
        balance = balance + deposit
        print("updated balance is",balance)
        print("what you want to do check balance , deposit or withdraw , enter exit to close")
        action=input("<").strip()
        
    else :
     
     print("enter valid input")
     print("what you want to do check balance , deposit or withdraw nter exit to close")
     
      
