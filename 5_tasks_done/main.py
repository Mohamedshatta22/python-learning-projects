inputs = input("enter your tasks separated by a comma ").lower()
tasks = inputs.split(", ")
tasks_done =[]
tasks_not_done=[]
for asks in tasks:
   print(asks)
   answer=input("have you done this tasks answer by (yes/no)").lower()
   if answer =="yes":
      print("nice jop")
      tasks_done.append(asks)
   else:
      print("try not to skip it for too long time")
      tasks_not_done.append(asks)
question = input("do you want to see you todays progress (yes/no) \n").lower()
if question == "yes":
   print(f""" tasks done
   
              {tasks_done}  
              
              ongoing tasks 
               
               {tasks_not_done}""") 
            

