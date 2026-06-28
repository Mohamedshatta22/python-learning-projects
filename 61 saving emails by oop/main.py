class user():
    def __init__(self,first_name,last_name,email,password,status="inactive"):
     self.first_name = first_name
     self.last_name = last_name
     self.email = email
     self.password = password
     self.status = status

def creat_user_name():
   first_name=input("please input your first name: ")
   last_name=input("please input your last name: ")
   email=input("please input your email: ")
   password=input("please input your password: ")
   if "@" in email:
      return user(first_name,last_name,email,password,status="active")
      

   return user(first_name,last_name,email,password)
user1=creat_user_name()
print(user1.first_name)
print(user1.last_name)
print(user1.email)
print(user1.password)
print(user1.status)
