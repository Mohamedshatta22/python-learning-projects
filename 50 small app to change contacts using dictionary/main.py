
}

while True :
    
    if number_chosen==1:
        contact_id = int(input("please enter the contact id:   "))
        name = input("please enter the contact name:  ")
        phone_number = input("please enter the contact number phone:  ")
        person["id"]=contact_id
       print("welcome to contact mangment")
person = {}
while True :
    print("""1- add a contact 
2- view a contact
3- edit a contact
4- exit""")
    number_chosen = int(input("please choose a number betwen 1-4  "))
    if number_chosen==1:
        contact_id = int(input("please enter the contact id:   "))
        name = input("please enter the contact name:  ")
        phone_number = input("please enter the contact number phone:  ")
        person[contact_id]={"name":name,
                            "phone number":phone_number}
        print(f"your contact {person[contact_id]['name']} was added successfully")
    elif number_chosen==2:
        id_asked = int(input("please enter the id contact you want to watch: "))
        [print(person[id_asked])]
    elif number_chosen==3:
        id_asked = int(input("please enter the current id contact: "))
        new_name = input("please enter the new contact name:  ")
        new_phone_number = input("please enter the new contact number phone:  ")
        person[id_asked]["name"] = new_name
        person[id_asked]['phone number'] = new_phone_number
        print(f"your contact {person[id_asked]['name']} was added successfully ")
    elif number_chosen==4:
        print("Thank you for your cooperation")
        break
    else:
        print("invaild choice ")
---------------------------------------
#اخر تحديث بتاريخ 2026/6/15


import os
def clear():
    os.system("cls") if os.name =="nt" else os.system("clear")
contacts = {}
while True :
 print("contacts management")
 print("""1- add a contact
2- view a contact 
3- edit a contact
4- exit """)
 print("please choose a number from 1-4 ")
 qu = int(input())
 clear()
 if qu == 1:
   contact_id =(input("enter a contact id: "))
   contact_name = input("please type a name: ")
   contact_number_phone = (input("please type a phone number: "))
   clear()
   contacts[contact_id]={"name":contact_name,"number phone":contact_number_phone}
   print(f"{contacts[contact_id]["name"]} was added successfully..")
   input("press enter here")
   clear()
 elif qu == 2:
   question =input("wich contact do u wann see please type the id of it down below:\n")
   clear()
   while True:
    if question in contacts:
     print(contacts[question])
     input("press enter here")
     clear()
     
     break
    else:
     print("invalid input please retype again.. ")
     question =input("wich contact do u wann see please type the id of it down below:\n")
     clear()
  
 elif qu == 3:
   while True:
    question =input("wich contact do u wanna edit please type the id of it down below:\n")
    clear()
    if question in contacts:
     contact_name = input("please type a new name: ")
     clear()
     contact_number_phone = (input("please type a  new phone number: "))
     clear()
     contacts[question]={"name":contact_name,"number phone":contact_number_phone}
     print(f"{contacts[question]["name"]} was updated successfully..")
     input("press enter here")
     clear()
     break
    else:
     print("invalid id contact")
     continue
 elif qu == 4:
   print("exiting....")
   break
 else :
   print("invalid input ")
