#Total number (2+4+6+8.......94+96+98+100)
total=0
for number in range(2, 101, 2):
    total+=number
print(total)

#Adding even number by modular
total2=0
for number in range(1, 101):
    if number%2==0:
      total2+=number
print(total2)