# The input funktion ask for a input. to specify what you want from use put "" around a str
name = input("What is your name")

#when we get a input it alwas a str data type so before we use it to math we need to convert it to float orh int
age = input("how old are you")

weight = float(input("What is your current weight"))

age = int(age) + 1

print(f"{age*8}")


print("Hello "+name)
print(f"you are {age} years old")

#if nesesary you can convert a data type in a string when typeing the print command

print("you weightet in at "+str(weight))