import os
import time
def clear_the_screen():

     if os.name=="nt":
          os.system("cls")
     else:
          os.system("clear")
def opening_screen():
   
    print("welcome to currency converter")
    print("")
    print("")
    print(""" ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||""")
    print("")
    print("________________________________________________________________________")
    print("""usd: 1.0
eur: 0.85
egp: 30.9
RMB: 6.5""")
opening_screen()
currency_library = {
     "usd":1,
     "eur":0.86,
     "egp":48.52,
     "Rmb":7.18
}
currency_chosen = input("choose a currency to convert from: ")
amount_of_money = int(input("enter the amount you want to convert: "))
converted_currency=input("choose a currency to convert to: ")
making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
while making_sure != "y":
    amount_of_money = int(input("enter the amount you want to convert to: "))
    making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
if currency_chosen=="usd":
    the_money_u_get =(currency_library["usd"])*amount_of_money*(currency_library[converted_currency])
else:
     the_money_u_get = (currency_library[converted_currency]/currency_library[currency_chosen])*amount_of_money

print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
time.sleep(2)
print(f"exchange rate 1 {currency_chosen} = {currency_library[converted_currency]} {converted_currency}")
time.sleep(2)
print(f"{amount_of_money} {currency_chosen} is equal to {the_money_u_get} {converted_currency}")
making_sure = input (f"do you accept this transaction confirm? y/n: ")
while making_sure != "y":
     clear_the_screen()
     print("transcation canceld")
     making_sure=input("do you want to perform another converstion ? y/n: ")
     if making_sure == "n":
          print("thank you for your cooperation")
          break
     else:
          clear_the_screen()
          opening_screen()
          currency_chosen = input("choose a currency to convert from: ")
          amount_of_money = int(input("enter the amount you want to convert: "))
          converted_currency=input("choose a currency to convert to: ")
          making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
          while making_sure != "y":
           amount_of_money = int(input("enter the amount you want to convert to: "))
           making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
          if currency_chosen=="usd":
           the_money_u_get =(currency_library["usd"])*amount_of_money*(currency_library[converted_currency])
          else:
           the_money_u_get = (currency_library[converted_currency]/currency_library[currency_chosen])*amount_of_money

          print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
          time.sleep(2)
          print(f"exchange rate 1 {currency_chosen} = {currency_library[converted_currency]} {converted_currency}")
          time.sleep(2)
          print(f"{amount_of_money} {currency_chosen} is equal to {the_money_u_get} {converted_currency}")
          making_sure = input (f"do you accept this transaction confirm? y/n: ")
          
clear_the_screen()  
print("thank you for your cooperation")    
