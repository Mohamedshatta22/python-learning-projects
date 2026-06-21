import time
import sys
import os
currencies = {"usd": 1.0,
              "eur": 0.86,
              "egp": 49.82,
              "rmb": 6.76,
              "myr": 4.07,
              "try":46.32}
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
def converting(user_currency,user_amount,to_be_converted):
  print(f"prepairng the deal from {user_currency} to {to_be_converted}.... please wait")
  time.sleep(3)
  clear()
  if user_currency == "usd":
    coverted_one =float(user_amount*currencies[to_be_converted])
    print(f"exchange rate 1 {user_currency} = {currencies[to_be_converted]}")
    print(coverted_one)
    time.sleep(3)
    
  else:
    price_per_one = (currencies[user_currency]/currencies[to_be_converted])
    coverted_one =float(user_amount/price_per_one)
    print(f" {user_amount} {user_currency}  is equal to {coverted_one} {to_be_converted}")
def opening_screen2():
   
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
eur: 0.86
egp: 49.82
RMB: 6.76
MYR: 4.07 """)
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
eur: 0.86
egp: 49.82
RMB: 6.76
MYR: 4.07 """)
    
    while True:
     user_currency = input("choose a currency to convert from: ").lower()
     if user_currency in currencies:
      break
     else:
      print("invalid currency please enter one of these currencies up there")
      time.sleep(2)
      clear()
      opening_screen2()
      continue

    clear() 
    time.sleep(1)
    while True:
 
 
     while True:
      user_amount = int(input("enter the amount: "))
      if type(user_amount) == int:
       clear()
       break
      else:
       print(f"invalid input {user_amount} is not a number please enter a number")
       time.sleep(3)
       continue
     ask = input(f"you entered {user_amount} {user_currency.upper()} to confirm? (y/n):  ").lower()
     time.sleep(1)
     clear()
     if ask =="y":
      while True:
       to_be_converted=input("choose a currency to convert to: ").lower()
       if to_be_converted in currencies:
        break
       else:
        print("invalid currency please enter one of these currencies up there")
        time.sleep(3)
        clear()
      
     elif ask =="n":
      continue
     
     converting(user_currency,user_amount,to_be_converted)
     qu = input("do you like to make another convert? y/n: ").lower()
     if qu == "y":
      clear()
      opening_screen()
     else:
      clear()
      print("exiting...")
      print("good bye Thank you for your cooperation see you soon  ")
      time.sleep(3)
      clear()
      sys.exit()
opening_screen()
