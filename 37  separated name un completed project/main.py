new_library2=[]

entered_names= input("enter the first and last name of your friends separated by a comma ").split(", ") 

counting_name = int(len(entered_names))


for x in range(0,counting_name):

 new_library=[]

 new_library.append(entered_names[x])

 new_library2.append(new_library)
 
print(new_library)

print(new_library2)


# dfgdfg gfg, fg ff
names = input ("enter the names of your friends separated by comma ").split(", ")
new_list=[]
length=len(names)
for x in range(0,length):
  new_list.append(names[x])
  print(new_list)

# mohamed fathy, ahmed fathy first_name = name_parts[0]
names = input ("enter the names of your friends separated by comma ").split(", ")

for x in names:
    name_parts = x.split()
    print(name_parts)
    first_name = name_parts[0][0] 
    sec_name = name_parts[1][0]
    print(first_name+sec_name)

