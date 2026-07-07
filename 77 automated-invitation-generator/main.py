def seperating_names ():
    with open ("names/invited_names.txt","r") as data:
        new_list = data.readlines()
        return new_list
    
 

for x in seperating_names():
       with open("input/letters/starting_letters.txt","r")as new_file:
        clear_name = x.strip("\n")
        the_letter = new_file.read()
        new_letter = the_letter.replace("{name}",clear_name)
        new_letter2 = new_letter.replace("{signature}","mohamed fathy")
        with open(f"output/ready_to_send/{clear_name}_invitation.txt","w") as new_file:
            new_file.write(new_letter2)


       
    