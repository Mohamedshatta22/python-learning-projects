def make_numbers_generator():
    for i in range(1,4):
        yield i               

for x in make_numbers_generator():
 print(x)
####################################################
def make_numbers_generator():
    yield "hello"  
    yield "wolrd"
    yield "python"
for x in make_numbers_generator():
 print(x)
  #################################
def make_numbers_generator(num):
 for i in range(1,6):
  yield i ** num
try:
 num  = int(input("please enter a number here: "))
 for x in make_numbers_generator(num):
  print(x)
except ValueError:
 print("invalid input")
finally:
 print("program is finished")

