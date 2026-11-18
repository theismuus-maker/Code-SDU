# a variable is a cotainer for a value. It can contain words, letters and more.

first_name = "Theis"
last_name = "Muusmann"
full_name = first_name + " " + last_name
age = 21
weight = 87.2
fat = False


#you can combine variables if it is the same type.
print("Hello, my name is " + first_name + " " + last_name + ".")
print(f"Hello, my name is {first_name} {last_name}.")
print(f"Hello my name is {full_name} and i am {age} years old")


#type checks what data type we are having in a variable 
print(type(first_name)) #str = string (stores a series of caractors like abcdefg...)
print(type(age)) # int = integer (stores whole number)
print(type(weight)) # float = decimal numbers
print(type(fat)) # Bool = True or false statement 


age += 1 # add 1 to age (you can do the same with all the operators)
print(age)

print("Your age is: "+str(age)) # We need to convert the age which was a int to a string so we can combine it 
print("Your weight is:"+str(weight)+"Kg") # Rember that the + is not for adding a number to the variable but is how you combine a print statment with more than one variable and text


print("Are you fat: "+str(fat)+ "!")