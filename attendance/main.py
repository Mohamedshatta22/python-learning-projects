persons= ["alice", "bob", "charlie"]
for person in persons:
 
 print(person)
 attendance = input("is this persone attended (yes/no): ")
 if attendance =="yes":
   print(" attendance cofirmed")
 else:
   print("attendance not confirmed") 


_______________________________________________
#updated one

attendees = input("enter the name of the atendees seprated by comma please")
library= attendees.split(", ")
for people in library:
   print(people)
   attendance = input("is this persone attended (yes/no): ")
   if attendance =="yes":
    print(" attendance cofirmed")
   else:
    print("attendance not confirmed")
