rows = int(input("How many rows "))
colums = int(input("How many colums "))
symbol = input("What symbol should we use? ")

for i in range(rows):
    for j in range(colums):
        (print(symbol, end=""))
    print()

#Finishes one forloob before moving forward. So in this example the program will finish the innerloob before det outher loob