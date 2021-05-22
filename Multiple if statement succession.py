print("Welcome to Roller Coaster!")
height=int(input("What is your height is in cm?\n"))
bill=0

if height>=120:
    print("Enjoy the ride")
    age=int(input("What is your age?\n"))
    if age<12:
        bill=5
        print("Children pay 5$.")
    elif age<=18:
        bill=7
        print("Adult pay 7$.")
    elif age>=60:
        bill=0
        print("For older its free.")
    else:
        bill=12
        print("please pay 12$.")
    want_Photo=input("Do want photo taken? Y or N \n")
    if want_Photo=="Y":
     bill+=3
    print(f"Your bill is ${bill}") 
else:
    print("Sorry you have to grow taller!")