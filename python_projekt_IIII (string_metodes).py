name = "Theis"
full_name = "Theis Muusmann"
age = "21"

#Tells how many characters there is in a variable 
print(len(name))
print(len(full_name))

# finds out when a character first show up in a string
print(name.find("T"))
print(full_name.find("u"))

# for some reason you to put () in the end of your print statement in some cases 
# capitalizes the first character 
print(full_name.capitalize())

# upper or lower cases your full string 
print(full_name.upper())
print(full_name.lower())

# checks if the variable contants digits. But before you can write .isdigit it needs to be a string
print(name.isdigit())
print(age.isdigit())

#The same counts for letters. Rember that it needs to be only letters no space og digits
print(name.isalpha())
print(full_name.isalpha())

#counts how many of a specifik charcater there is in a string
print(full_name.count("u"))

#replace letters with otters 
print(full_name.replace("u","7"))

#print a variable multipel times 
print(name*5)