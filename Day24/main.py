#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as names:
    names_list = names.readlines()

with open('./Input/Letters/starting_letter.txt') as template_letter_file:
    template_letter = template_letter_file.read()

for name in names_list:
    format_name = name.strip()
    with open(f'./Output/ReadyToSend/letter_to_{format_name}.txt', 'w') as letter_file:
        new_letter = template_letter.replace("[name]", name)
        letter_file.write(new_letter)

