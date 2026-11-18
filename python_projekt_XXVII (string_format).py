# str.format = optional method that gives users more cortrol when displaying out

animal = "cow"
item = "moon"


print(f'The {animal} jumped over the {item}')

print('The {} jumped over the {}'.format("cow","moon"))

print('The {} jumped over the {}'.format(animal,item))

print('The {1} jumped over the {0}'.format(animal,item))

print('The {animal} jumped over the {item}'.format(animal="pig",item="sun"))

tekst = 'The {} jumped over the {}'

print(tekst.format(animal,item))

name = "Theis"

print("Hello, my name is {}".format(name))

print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


number = 1000

print("The number pi is {:.3f}".format(number))

print("The number pi is {:,}".format(number))

print("The number pi is {:b}".format(number))

print("The number pi is {:o}".format(number))

print("The number pi is {:x}".format(number))

print("The number pi is {:e}".format(number))