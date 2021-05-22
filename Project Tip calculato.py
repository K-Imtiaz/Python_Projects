print("# Welcome to the tip calculator #")
Total_Bill=(float(input("What was the total bill? \n$")))
Percentage_Tip=(int(input("What percent tip would you like to give?\n 10,12 or 15?\n ")))
People=(int(input("How many people are spiliting bills?\n ")))

Bill_With_Tip= Percentage_Tip/100* Total_Bill+Total_Bill
print(Bill_With_Tip)
Spilting_Bills= Bill_With_Tip/ People
#round vs format
#Final_amount=round(Spilting_Bills,2)

#we can use float "{:.2f}".format as round with format function.
Final_amount="{:.2f}".format(Spilting_Bills)
print(f"Each person should pay: ${Final_amount}")
print("###### End #####")