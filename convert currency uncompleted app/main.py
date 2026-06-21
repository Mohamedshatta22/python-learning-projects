#‎Friday, ‎August ‎22, ‎2025, ‏‎4:56:03 PM
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
currency_chosen = input("choose a currency to convert from: ")
amount_of_money = int(input("enter the amount you want to convert: "))
converted_currency=input("choose a currency to convert to: ")
usd = 1
eur = 0.86
egp = 48.52
Rmb = 7.18
usd_to_eur = amount_of_money*eur
usd_to_egp = amount_of_money*egp
usd_to_Rmb = amount_of_money*Rmb
eur_to_usd =  (usd/eur)
eur_to_egp =  (egp/eur)
eur_to_Rmb =  (Rmb/eur)
usd_to_Rmb =  (Rmb/eur)
egp_to_usd =  (usd/egp)
egp_to_eur =  (eur/egp)
egp_to_Rmb =  (Rmb/egp)
Rmb_to_usd =  (usd/Rmb)
Rmb_to_eur =  (eur/Rmb)
Rmb_to_egp =  (egp/Rmb)
currency_library = {}
making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
def conversion():
 while True:
  if making_sure=="y":
    clear_the_screen()
    break      
  else:
    amount_of_money = int(input("enter the amount you want to convert to: "))
    making_sure = input(f"you entered {amount_of_money} {currency_chosen} confirm? y/n: ")
    clear_the_screen()
    return amount_of_money
def conversion2():
 while True:
  if making_sure=="y":
    clear_the_screen()
    print("thank you for your cooperation")
    opening_screen()
    currency_chosen = input("choose a currency to convert from: ")
    amount_of_money = int(input("enter the amount you want to convert: "))
    converted_currency=input("choose a currency to convert to: ")
    calcuating() 
    return currency_chosen and amount_of_money and converted_currency
  else: 
     print("transcation canceld")
     making_sure=input("do you want to perform another converstion ? y/n: ")
def calcuating():  
 if currency_chosen=="usd":
    if converted_currency == "eur":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {eur} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {usd_to_eur} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="egp":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {egp} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {usd_to_egp} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="Rmb":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {Rmb} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {usd_to_Rmb} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
 elif currency_chosen == "eur":
    if converted_currency == "usd":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {eur_to_usd} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {eur_to_usd*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="egp":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {eur_to_egp} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {eur_to_egp*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="Rmb":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {eur_to_Rmb} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {usd_to_Rmb*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
 elif currency_chosen == "egp":
    if converted_currency == "usd":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {egp_to_usd} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {egp_to_usd*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="eur":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {egp_to_eur} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {egp_to_eur*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="Rmb":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {egp_to_Rmb} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {egp_to_Rmb*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
 elif currency_chosen == "Rmb":
    if converted_currency == "usd":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {Rmb_to_usd} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {Rmb_to_usd*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="eur":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {Rmb_to_eur} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {Rmb_to_eur*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()
        else:
           print("thank you for your cooperation")
    elif converted_currency=="egp":
        print(f"prparing the deal from {currency_chosen} to {converted_currency} please wait ....")
        time.sleep(2)
        print(f"exchange rate 1 {currency_chosen} = {Rmb_to_egp} {converted_currency}")
        time.sleep(2)
        print(f"{amount_of_money} {currency_chosen} is equal to {Rmb_to_egp*amount_of_money} {converted_currency}")
        making_sure = input (f"do you accept this transaction confirm? y/n: ")
        if making_sure=="n":
         conversion2()

calcuating()
    
