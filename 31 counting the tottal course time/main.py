sec = input("please enter the tottal sec of your course \n")
int_sec = int(sec)
tottal_hours = int_sec// 3600
rest_sec = int_sec%3600
rest_min = rest_sec//60
rest_sec_sec = rest_sec%60

print("okey then your tottal cousre hours are "+ str(tottal_hours) +" hours and the mins are " + str(rest_min) + " mins and the rest sec are " + str(rest_sec_sec))


