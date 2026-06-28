# تم الحل اخيرا 
#Saturday, ‎June ‎6, ‎2026, ‏‎4:45:18 PM
name_list =[]
name_list3 = []
names = input("enter the name of the people separated by comma please \n  ").split(", ") 
num_of_people= len(names)
for x in range(0,num_of_people):
    name_list+= names[x].split(" ")
num_of_people2= len(name_list)
for x in range(0,num_of_people2,2):
    name_list2 =[]
    name_list2.append(name_list[x])
    name_list2.append(name_list[x+1])
    name_list3.append(name_list2)
num_of_people3 = len(name_list3)
for x in range(0,num_of_people3):
    print(name_list3[x])

for x in range(0,num_of_people3):
    print(f"{name_list3[x][0][0]}.{name_list3[x][1][0]}.")
