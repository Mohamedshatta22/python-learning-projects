def decorate_omar(func):
    def adding_more_info():
        print("this  is person from 10th of ramdan city")
        func()
        print("after reading this make sure that this was added by decoration  and also "
        "the city info")
    return adding_more_info
    
@decorate_omar
def omar():
    name = "omar"
    age = 18
    print(name)
    print(age)

omar()
