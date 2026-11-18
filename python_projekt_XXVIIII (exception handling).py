# exceptioin events detected during a execution that interrubt the flow od af program
result = 0

while result==0:
    try: 
        numerator = int(input("Enter a number to divide: "))
        denominator = int(input("Enter a number to divide by: "))
        result = numerator / denominator
        
    except ZeroDivisionError as e:
        print(e) # prints what the specifik problem was
        print("You cant divide by zero!")
    except ValueError as e:
        print(e)
        print("Enter only numbers")
    except Exception as e:
        print(e)
        print("something went wrong")
    else:
        print(result)
    



