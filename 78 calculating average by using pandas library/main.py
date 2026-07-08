import pandas
content = pandas.read_csv("workout.csv")
list1 = content["burned_calaroies"].to_list()
sum_list = sum(list1)
len_list = len(list1)
print(sum_list/len_list)
#################################################
#sec way
print(sum(content["burned_calaroies"].to_list())/len(content["burned_calaroies"].to_list()))