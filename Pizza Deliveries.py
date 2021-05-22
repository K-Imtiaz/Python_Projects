print("Welcome to Pizza Deliveries.")
size=input("What size pizza do you want? S,M,L\n")
add_meat=input("Do you want extra meat? Y,N\n")
extra_cheese=input("Do you want extra cheese? Y,N\n")
Coke=input("Do you want coke?Y or N\n")
bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

if add_meat=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
        
if extra_cheese=="Y":
    bill+=1
if Coke=="Y":
    bill+=5
print(f"Your final bill is ${bill}")
        
