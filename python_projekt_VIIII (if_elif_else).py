# if statement is a block of code that will happen if a condition is true 

age = int(input("how old are you?: "))

if age >= 18:
    print("You are an adult")
elif age > 13 and age < 18:
    print("you are a teenager")
else:
    print("you are a child")


# the elif is optinal and you can have a elif step more then once but if you have a statement and your input is in to chatagories it will take the statement that is set first