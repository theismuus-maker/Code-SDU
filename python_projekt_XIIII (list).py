#list is used to store multipul items in a variable
#variable turns to a list by surrounding it with []
food = ["pizza", "dates", "milk"]

print(food)
# prints the item in that sepcifik place
print(food[1])

# adds an item to the list 
food.append("meat")

print(food[3])

#replace a item on that specifik line in the list 
food[2]="sushi"
print(food)

food.remove("sushi")

#add a item a specifik place in the list
food.insert(1,"cake")

#sorts the list in alphabetic order
food.sort()

# removes all the items in the list 
food.clear()

#print one item at a time in differnt rows 
for x in food:
    print(x)


