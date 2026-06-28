‎import time
def obtaining_info():
 user_name = input("please enter the user name: ")
 email = input("please enter you email here:  ")
 checking_email(email, user_name)
 return user_name and email 
 
def checking_email(email,user_name):
     if "@" in email and "." in email:
        print("checking user name....")
        time.sleep(3)
        print("validating email....")
        time.sleep(3)
        print(f"user {user_name} with email {email} successfully added")
     else:
        print("checking user name....")
        time.sleep(3)
        print("validating user name....")
        time.sleep(3)
        print(f"invaild email format registaration faild")
obtaining_info()
  

