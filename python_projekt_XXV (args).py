#args = is parameter that will pack all arguments into a tuple 
#useful so that a function can accept a varying amount of arguments
# the real stuff to be aware of is *

def add(*args):
    sum = 0
    args = list(args)
    for i in args:
        sum += i
    return(sum)

print(add(1,2,3,45,6,776,5,3,2,45,6))



def sub(*args):
    sum = 0
    args = list(args)
    for i in args:
        sum -= i
    return(sum)

print(sub(1,3,5,6,8,3,112,567))


print(sub(5,6),add(5,2))