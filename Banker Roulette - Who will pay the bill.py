import random
names_string=input("Enter every body's name.")
names=names_string.split(", ")
num_items=len(names)
random_choice=random.randint(0, num_items-1)
print(random_choice)
person_who_will_pay_today=names[random_choice]
print(person_who_will_pay_today+" is going to buy the meal today")


#Shortcut way by (choice function)
person_who_will_pay_today=random.choice(names)
print(person_who_will_pay_today+" is going to buy the meal today")