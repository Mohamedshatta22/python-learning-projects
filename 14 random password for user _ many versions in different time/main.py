import random
import string
pas = []
pas2=""
num =string.digits
cha=string.ascii_letters
symb = string.punctuation
print("welcome in password app generator")
total_num = int(input("enter the total number of the passwords: "))
char_num = int(input("enter the number of letters in password:" ))
num_num = int(input("enter the number of number in password:" ))
symb_num = int(input("enter the number of symbols in password:" ))
if char_num+num_num+symb_num == total_num:
  pas += random.choices(num,k=num_num)
  pas += random.choices(cha,k=char_num)
  pas += random.choices(symb,k=symb_num)
  random.shuffle(pas)
for x in pas:
  if x in num: 
     pas2+=x
  elif x in cha:
     pas2+=x
  elif x in symb:
     pas2+=x
print(f"here is your password {pas2}")
______________________________________________________________________________________________
import random
import string
pas = []
pas2=""
num =[1,2,3,4,5,6,7,8,9]
cha=["a", "b", "c", "d", "e", "f", "g", "l", "w", "u"]
symb = ["!", "@", "#", "$", "%", "^", "&", "*"]
print("welcome in password app generator")
total_num = int(input("enter the total number of the passwords: "))
char_num = int(input("enter the number of letters in password:" ))
num_num = int(input("enter the number of number in password:" ))
symb_num = int(input("enter the number of symbols in password:" ))
if char_num+num_num+symb_num == total_num:
  pas += random.choices(num,k=num_num)
  pas += random.choices(cha,k=char_num)
  pas += random.choices(symb,k=symb_num)
  random.shuffle(pas)
  for x in pas:
   if x in num: 
     pas2+=str(x)
   elif x in cha:
     pas2+=x
   elif x in symb:
     pas2+=x
  print(f"here is your password {pas2}")
  name =input("press enter to close the app")
else:
  print("there is something wrong you might have added less or more than you asked")
  name2 =input("press enter to close and run the program again")

_____________________________________________
import random
import string
print("wellcom to the password app generator")
password=[]
meme = ""
num =string.digits
cha=string.ascii_letters
symb = string.punctuation
the_total_number=int(input("enter the total number of characters in the password " \
""))
char_num = int(input("enter the number of letters in password :" ))
num_num = int(input("enter the number of number in password :" ))
symb_num = int(input("enter the number of symbols in password :" ))
if char_num+num_num+symb_num==the_total_number:
   password+=(random.choices(num,k=char_num))
   password+=(random.choices(cha,k=num_num))
   password+=(random.choices(symb,k=symb_num))
   random.shuffle(password)
   print("your generated password is ")
   print("".join(password))
else:
   print("how can this ba posssible the number of the password is not even correct according to what u asked for please rework it again")


