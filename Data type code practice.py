two_digit_number=input("Type a two digit number\n")
print(type(two_digit_number))

first_digit=two_digit_number[0]
second_digit=two_digit_number[1]

print(first_digit)
print(second_digit)

result=int(first_digit)+int(second_digit)
print(result)

#another way

two_digit_number=input("Type a two digit number\n")
print(type(two_digit_number))

first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])

print(first_digit)
print(second_digit)

result=first_digit+second_digit
print(result)