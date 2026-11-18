#tuple 

student = ("theis", 21, "male")

# the count funktion counts how many times a x is in a list 
print(student.count("theis"))
# the index funktion tells you where in the list x is placed
print(student.index("male"))

# this statment prints all of the itemss in a list. 
for x in student:
    print (x)

#This if statement checks if a item is in a variable and then print it if it is in the variable
if "bro" in student:
    print("Theis is here")