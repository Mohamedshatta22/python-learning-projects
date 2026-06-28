items=[]
prices=[]
print("welcome to ishop calculator")
num_items = int(input("how many items are there in your basket today ? \n"))
print("lets go and counting them ....")
for x in range(1,num_items+1):
 item = input(f"tell me the name of the item number {x} ").lower()
 if item:
  items.append(item)
  price=float(input(f"what is the price of {item} $"))
  prices.append(price)
ask= input("would you like to see your entire basket items? ").lower()
if ask == "yes":
 print(f" your items are {items}")
else:
 print("okay")
ask2= input("would you like to see how much it will cost you? ").lower()
if ask == "yes":
 print(f"it will cost you about ${sum(prices)}")


print("wellcom to i shop calculator")
que = int(input("how many items are there in your basket for today "))
basket =[]
price_list=[]
print("lets get to counting them...." )
for c in range(1,que+1):
    que2=input(f"please tell me the name of the item number {c} ")
    basket.append(que2)
    price_que = int(input("please tell me the price of it " ))
    price_list.append(price_que)
que3=input("would u like to see your entire basket ?")
if que3 =="yes":
    print(basket)
else:
    print("okey")
que4=input("would u like to see how much it will cost you ? ")
if que4 =="yes":
    print(sum(price_list))
else:
    print("okey")
