def encrypted (Unencrypted_letter,encrypted_key):
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
      encrypted_letter+=letters[Unencrypted_letter_num+encrypted_key]
     elif x in letters2:
      Unencrypted_letter_num= letters2.index(x)
      encrypted_letter+=letters2[Unencrypted_letter_num+encrypted_key]
  print(encrypted_letter)
def unencrypted (Unencrypted_letter,encrypted_key):
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
      encrypted_letter+=letters[Unencrypted_letter_num-encrypted_key]
     elif x in letters2:
      Unencrypted_letter_num= letters2.index(x)
      encrypted_letter+=letters2[Unencrypted_letter_num-encrypted_key]
  print(encrypted_letter)
qu = int(input("""what do you want to do to
1-encrypte a message\n\
2-unencrypte a message\n"""))
if qu ==1:
  key =int(input("please enter the key: "))
  messages =input("please enter the sentence u wanna encrypt: ")
  encrypted (messages,key)
else:
  key =int(input("please enter the key: "))
  messages =input("please enter the sentence u wanna unencrypt: ")
  unencrypted (messages,key)
