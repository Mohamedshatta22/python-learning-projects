import os
def searching_for_file(file_name):
    drivers = ['C:\\', 'D:\\', 'E:\\', 'F:\\']
    for driver in drivers:
        if not os.path.exists(driver):
            continue
        for folder_path, folder_names_list, fileeee_name in os.walk(driver):
            if file_name in fileeee_name:
                the_file_path = os.path.join(folder_path,file_name)
                return the_file_path
    return "Unfortunately the file does not exist"
qu = input("please enter your file name ended with(.txt): ")
print("sorry this takes some time thank you for your patience")
file_path = searching_for_file(qu)
print(searching_for_file(qu))

if os.path.exists(file_path):
    os.startfile(file_path)
