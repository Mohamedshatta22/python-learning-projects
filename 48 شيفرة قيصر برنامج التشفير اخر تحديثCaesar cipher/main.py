#Saturday, ‎June ‎13, ‎2026, ‏‎5:33:32 AM
import string 
letters = string.ascii_lowercase*100
encrypted_letter= ""
pun = string.punctuation
Unencrypted_letter =input("please enter the sentence u wanna encrypt: ").lower()
Unencrypted_key =int(input("please enter the key: "))
for x in Unencrypted_letter:
     if x == " " or x in pun:
         encrypted_letter+= x 
         continue
     Unencrypted_letter_num= letters.index(x)
     encrypted_letter+=letters[Unencrypted_letter_num+Unencrypted_key]
print(encrypted_letter)
#هنا مافيش فاصلة بعني اتعملت بعديها بيوم شكل جديد  ليها بستخدام الفانكشن واضافة بعض الاضافات زي الحروف الكبيرة 
def encrypted (Unencrypted_letter,Unencrypted_key):
  import string 
  letters = string.ascii_lowercase*10000
  letters2 = string.ascii_uppercase*10000
  encrypted_letter= ""
  pun = string.punctuation
  for x in Unencrypted_letter:
     if x == " " or x in pun:
         encrypted_letter+= x 
         continue
     elif x in letters:
      Unencrypted_letter_num= letters.index(x)
      encrypted_letter+=letters[Unencrypted_letter_num+Unencrypted_key]
     elif x in letters2:
      Unencrypted_letter_num= letters2.index(x)
      encrypted_letter+=letters2[Unencrypted_letter_num+Unencrypted_key]
  print(encrypted_letter)
messages =input("please enter the sentence u wanna encrypt: ")
key =int(input("please enter the key: "))
encrypted (messages,key)

