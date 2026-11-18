#scope = The region that a variable is recognized 
# A variable  is only availabel from inside the it is created 
# a global and locally scope version od a varibale can be created


#local scoped
def display_name():
    name = "Theis"
    print(name)


#local varivables are only inside a created funktion 


#global scope  is available in the hole code

name = "theis"

print(name)
display_name()