# set funktion
# if we have a statement like this we are not sure that the ordre would be the same every time. That is a set funktion
utensils = {"fork", "spoon", "knif"}

#for x in utensils:
    #print(x)


exersice = {"bicep curl", "tricep extention", "leg extention", "leg curl", "hack sqaut", "pec dec", 
            "bicep curl", "ub row", "leg extention", "hack sqaut"}
exersice.add("hammer curl")
exersice.remove("hack sqaut")

#puts one list into another list and removes the old list 
utensils.update(exersice)
#for x in exersice:
    #print(x)

for x in utensils:
    print(x)

#the union funktion joins list together 
all = exersice.union(utensils)
for x in all:
    print(x)

# checks both lists to see what one list has that the other list dosent have 
print (utensils.difference(exersice))

# prints every element that both sets have  
print(utensils.intersection(exersice))