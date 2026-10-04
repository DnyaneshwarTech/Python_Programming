num = int(input("Enter a number : "))

temp = num
sum = 0

while temp > 0:
    sum = sum + (temp % 10)
    temp = temp // 10

if num % sum == 0:
    print(num, "is a Harshad Number")
else:
    print(num, "is not a Harshad Number")