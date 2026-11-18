#dictionary is a changeable, unordred colllection of unique key:value pairs 
#       Fast because they use hashing which allow us to acces a value quickly

# so in this example we set up a contry to its capital. It wery mutch look like a set but the differens is that we : to seperat what sticks togeter
capitals = {"Denmark":"Cobenhagen",
            "Sweden":"Stockholm",
            "Norway":"Oslo"}

#add a new key and a new value
capitals.update({"Koratia":"Zagreb"})
#updates a key with a new value 
capitals.update({"Denmark":"Vester Nebel"})

#removes a key from the dictionary
capitals.pop("Sweden")
#removes everything from the dictionary
capitals.clear()

# checks what value is stored to the key of norway. 
#print(capitals["Norway"])

#it is a bit more safe to uses the get funktion because instead of the system crashing it just says none when the asked key is not in the dictionary
print(capitals.get("germany"))

#prints all the keys in the dictionary 
print(capitals.keys())
#prints all the values in the dictionary
print(capitals.values())
#prints the hole dictionary
print(capitals.items())

# this forloob prints every key and every value in the hole dictionary in the dictionary
for key, value in capitals.items():
    print(key,value)