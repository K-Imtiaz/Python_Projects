height=float(input("Enter your height in m:\n"))
weight=float(input("Enter your weight in kg:\n"))
bmi=round(weight / height **2)
bmi = (bmi)
print(bmi)
if bmi <18.5:
      print(f"Your bmi is {bmi},You are Underwight")
elif bmi<25:
    print(f"Your bmi is {bmi},You are Normal weight")    
elif bmi<30:
    print(f"Your bmi is {bmi},You are Overweight")
elif bmi<35:
    print(f"Your bmi is {bmi},You are obese")    
else:
    print(f"Your bmi is {bmi},You are clinically obese")    