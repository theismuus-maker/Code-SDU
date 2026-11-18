import math

pi =-3.14
x = 90
y = 170
# rounds to closet hole number 
print(round(pi))

#round a number up to the closet holde number
print(math.ceil(pi))

#round a number down to the closet holde number 
print(math.floor(pi))

#tells how long your are away from zero
print(abs(pi))

#raises a value to the power of a variable 
print(pow(pi,2))

#takes the sqarerout of a number. I have set a positiv number because our variable pi is negativ and right now we cant handle that
print(math.sqrt(x))

#either finds smalest or largest number in variables
print(max(pi, x, y))
print(min(x,y,pi))
