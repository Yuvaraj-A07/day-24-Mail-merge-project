#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()
    for name in name_list:
        person = name.strip()
        with open("./input/Letters/starting_letter.txt") as letter:
            original_letter = letter.read()
            modified_letter = original_letter.replace("[name]", person)
            with open(f"./Output/ReadyToSend/{person}"+".txt", "w") as invite:
                invite.write(modified_letter)

