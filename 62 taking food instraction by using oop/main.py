print("welcome to recipe collection ...")
class cooking ():
 def __init__(self,recipe_name,ingredients,cooking_time,cooking_instarctions):
  self.recipe_name = recipe_name
  self.ingredients = ingredients
  self.cooking_time = cooking_time
  self.cooking_instarctions = cooking_instarctions



def queistion():
 recipe_name = input("please enter a recipe name: ")
 ingredients = input("please enter the ingredients separated by comma: ")
 cooking_time = input("please enter the cooking time: ")
 cooking_instarctions = input("please enter the cooking instarctions: ")
 print("recipe added successfuly")
 return cooking (recipe_name,ingredients,cooking_time,cooking_instarctions)
recipe1 = queistion()
print("displaying recipe...")
print(f"name: {recipe1.recipe_name}")
print(f"ingredients: {recipe1.ingredients}")
print(f"cooking_time: {recipe1.cooking_time}")
print(f"cooking_instarctions: {recipe1.cooking_instarctions}")
