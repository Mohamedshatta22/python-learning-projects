names= input("please enter the name of your tasks for today sparetaed by comma ").split(", ")
ingoing_tasks=[]
outgoing_tasks=[]
for x in names:
    print( f"about {x}")
    answer=input(" have u finished doing this task ? ")
    if answer=="yes":
        print("good job")
        ingoing_tasks.append(x)
    else:
        print("try no to skip it ")
        outgoing_tasks.append(x)

que=input("do u want to see you days progress yes or no ? ")
if que =="yes":
 print(f"you done tasks\n{ingoing_tasks}")
 print(f"your undone tasks\n{outgoing_tasks}")
else:
   print("okey")
