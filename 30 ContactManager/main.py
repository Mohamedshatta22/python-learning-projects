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
        id_asked = int(input("please enter the id contact you want to see: "))
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
