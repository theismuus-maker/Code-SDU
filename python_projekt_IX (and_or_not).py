temp = float(input("What is the tempetaure in the room you are standing in?: "))

if temp >= 0 and temp <= 10:
    print("It is cold but not frezzing")

elif temp >= 10 and temp<=25:
    print("The temp is nice and cosy")

elif temp > 25:
    print("It is hot remember to drink a lot of water")

else:
    print("Be careful it is freezing cold")


bmi = float(input("What is your bmi?: "))

if bmi > 25 or bmi < 20:
    print("You are unhealthy")
    print("Be aware of what you eat")
    print("A bad bmi can be dangerous")
else:
    print("sounds fine")


bmi = float(input("What is your bmi?: "))

if not( bmi > 25 or bmi < 20):
    print("You are unhealthy")
    print("Be aware of what you eat")
    print("A bad bmi can be dangerous")
else:
    print("sounds fine")

    #so beaware of the not is like chanceing the statement from true to falsh or the other way around
    # The and statement needs to have alle statements true before it will activate
    #The or funktion only needs one statement to be true 