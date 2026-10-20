num = int(input("Give a value please integer. "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("you entered an armstrong number")
else:
    print("You have not entered an armstrong number")