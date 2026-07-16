 try:
    input1 = int(input("please enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid integer")
  #############################################################################################
try:
    put = int(input("please enter a number: "))
    print(put*put)
except ValueError:
    print("Invalid input!")
  ####################################################################
try:
    first_number= int(input("please enter a first number: "))
    sec_number= int(input("please enter a sec number: "))
    devided_num = (first_number/sec_number)
    print(devided_num)

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")
##############################################################################
try:
    first_number= int(input("please enter a first number: "))
    sec_number= int(input("please enter a sec number: "))
    devided_num = (first_number/sec_number)
    print(devided_num)

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("program finished")
  ###########################################
try:
    first_number= int(input("please enter a first number: "))
    sec_number= int(input("please enter a sec number: "))
    devided_num = (first_number/sec_number)
    
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")

else:
   print('Everything went well.')
   print(devided_num)

finally:
    print("program finished")
