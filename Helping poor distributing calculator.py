print("Welcome to helping Poor foundation")
How_Money=float(input("How many money we are giving? \n$"))
Percent_money=int(input("how many percentage we are giving? 30,40 or 50?\n"))
people=int(input("how many people are giving the money?\n"))


Money_with_Percentage= Percent_money/100*How_Money+How_Money
print(Money_with_Percentage)
Spilting_Money= Money_with_Percentage/people
Final_amount="{:.2f}".format(Spilting_Money)
print(f"Each person should pay: ${Final_amount}")
