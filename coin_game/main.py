import random
ran = random.randint(0,1)
ran2 = random.random()
print("welcome to the coin guessing game")
print("""choose a methode to toss the coin
      1-randint
      2-random random""")
user_choise = int(input())
user_choise_face =input("enter what do you choose head or tales").lower()
if user_choise ==  1 and ran ==0:
    pc_choise = "head"
elif user_choise==1 and ran ==1: 
    pc_choise = "tales"
elif user_choise ==2 and ran2>0.5:
    pc_choise= "head"
elif user_choise ==2 and ran2<0.5:
     pc_choise ="tales"
else:
    print("invalid choise")
if user_choise_face == pc_choise:
   print(f"you won the pc chosed the same face {pc_choise}")
else:
    print(F"you lost the pc chosed {pc_choise}")
    
