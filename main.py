from replit import clear
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
  print(f"Available resources are Water : {resources['water']} , Milk : {resources['milk']} , Coffee : {resources['coffee']}")

def check_availability(choice):
  if not choice=='espresso':
    if resources['water'] >= MENU[choice]["ingredients"]["water"] and  resources["milk"] >= MENU[choice]["ingredients"]["milk"] and resources['coffee'] >= MENU[choice]["ingredients"]["coffee"] :
      return True
  elif choice=='espresso':
    if resources['water'] >= MENU[choice]["ingredients"]["water"] and resources['coffee'] >= MENU[choice]["ingredients"]["coffee"] :
      return True

  else:
    return False 
def get_money(choice):
  penny=float(input("Penny :"))
  penny=penny*0.01
  nickel=float(input("Nickel :"))
  nickel=nickel*0.05
  dime=float(input("Dime :"))
  dime=dime*0.10
  quarter=float(input("Penny :"))
  quarter=quarter*0.25

  Total=nickel+dime+penny+quarter

  if(Total>1.50 and choice=="espresso"):
    if(Total==1.50):
      return True
    else:  
      remain=Total-1.50
      print(f"Here is your change {remain}")
      return True
  elif(Total>2.50 and choice=="latte"):
    if(Total==2.50):
      return True
    else:  
      remain=Total-2.50
      print(f"Here is your change {remain}")
      return True 
  elif(Total>3.00 and choice=="cappuccino"):
    if(Total==3.00):
      return True
    else:  
      remain=Total-3.00
      print(f"Here is your change {remain}")
      return True 
  else:
    return False           
def make_operation(choice):
  if(choice=="latte"):
    print("Latte made please take it")
    resources['water']= resources['water']-MENU[choice]['ingredients']['water']
    resources['milk']= resources['milk']-MENU[choice]['ingredients']['milk']
    resources['coffee']= resources['coffee']-MENU[choice]['ingredients']['coffee']
  elif(choice=="cappuccino"):
    print("Cappuccino made please take it")
    resources['water']= resources['water']-MENU[choice]['ingredients']['water']
    resources['milk']= resources['milk']-MENU[choice]['ingredients']['milk']
    resources['coffee']= resources['coffee']-MENU[choice]['ingredients']['coffee']
  elif(choice=="espresso"):
    print("espresso made please take it")
    resources['water']= resources['water']-MENU[choice]['ingredients']['water']
    
    resources['coffee']= resources['coffee']-MENU[choice]['ingredients']['coffee']   
def Main_operation(choice):
  option=check_availability(choice)
  if option==True:
    print("please provide your money")
    money=get_money(choice)
    if money==True:
      make_operation(choice)
    else:
      print("Not Sufficient money")
  else:
    print("Not sufficient amount of resource")     
def refill():
  resources['water']=300
  resources['milk']=200
  resources['coffee']=100
  print("Refill added--------------------------------")
want_option=False

while not want_option:
  choice=input("Enter your option espresso/latte/cappuccino/report/refill:")
  if(choice=="report"):
    report()
  elif choice=="espresso":
    Main_operation(choice)
  elif choice=="latte":
    Main_operation(choice)
  elif choice=="cappuccino":
    Main_operation(choice)
  elif choice=='refill':
    refill()  
  else:
    print("Invalid option")
          


