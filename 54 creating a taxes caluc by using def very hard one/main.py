salary = int(input("please enter yout salary: "))
bouns=int(input("please enter your bouns: "))
def taxes_calc(total_money):
    return (total_money/100)*15
   
def the_rest_of_the_money(bouns, salary):
    total_money = bouns+salary
    money_after_all = total_money -taxes_calc(total_money)
    return money_after_all
print("The remainder of your salary after deducting taxes is ")
print(the_rest_of_the_money(bouns, salary)
)   
--------------------- 
#اخر شكل بتاخري 2025 شهر 6 يوم 16 ومازال اختبار محير اوي ورخم والمرة دي لما عملته استعنت بالذكاء الاصطناعي بشكل غير مباشر انه يعرفني الحل لكن يقولي عندك مشكلة هنا ف انا اركز و احلها 

def giving_the_last_message ():
  salary = int(input("what is your tottal salary please: "))
  bouns = int(input("what is your tottal bouns: "))
  print(after_tax(bouns,salary))

def after_tax(bouns,salary):
  taxs = (bouns+salary)*0.15
  return (bouns+salary)-taxs

giving_the_last_message ()

  
