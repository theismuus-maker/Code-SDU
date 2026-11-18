# index operator [] = gives acces to a sequcens element (str,list,tuples)

name = "theis Muusmann"

# so we check it the first value in the variable is spelt with small letters and if so we capitalize it and print it 
if(name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[0:5].capitalize()
print(first_name)

last_name = name[6:].capitalize()
print(last_name)