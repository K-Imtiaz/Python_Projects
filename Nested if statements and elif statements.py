print("Welcome to Roller Coaster!")
height=int(input("What is your height is in cm?\n"))

if height>=120:
    print("Enjoy the ride")
    age=int(input("What is your age?"))
    if age<12:
        print("Please pay 5$.")
    elif age<=18:
        print("Please pay 7$.")
    elif age>=60:
        print("Do not pay it's totally free for you.")
    else:
        print("please pay 12$.")
else:
    print("Sorry you have to grow taller!")