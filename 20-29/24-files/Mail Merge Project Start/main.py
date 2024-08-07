#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




with open("/home/mb/Documents/codes/PythonCourse/day24-files/Mail Merge Project Start/Input/Names/invited_names.txt" ,"r") as names_file:



    names = names_file.readlines()





print(names)

with open("/home/mb/Documents/codes/PythonCourse/day24-files/Mail Merge Project Start/Input/Letters/starting_letter.txt" ) as letter_file:
    
    letter_content = letter_file.read()
    for name in names:
        name =  name.strip("\n")
        new__letter = letter_content.replace("[name]", name)
        new_file = open(f"invitation_{name}.txt","w")
        new_file.write(new__letter)
        print(new__letter)
        new_file.close()


