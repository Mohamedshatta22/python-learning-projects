import os
def calcu(items_quan, the_item_price):
    return items_quan*the_item_price

def clear_the_screen():

     if os.name=="nt":
          os.system("cls")
     else:
          os.system("clear")
while True:
 budget = int(input("enter your spending budget: "))
 item = input("enter the item you want to buy: " )
 items_quan = int(input(f"how many {item}s do you want to buy: "))
 the_item_price = int(input(f"enter the price per {item}: "))
 result=calcu(items_quan,the_item_price)
 if result<= budget:
   print("sucsess you can buy it ")
 else:
      print("warrning ")
 exit_que = input("do you want to continue y/n: ")
 if exit_que.lower() == "y":
     clear_the_screen()
     continue 
 elif exit_que.lower() == "n":
    clear_the_screen()
    break  
