num = int(input("Enter a number : "))

square = num * num
temp = num
divisor = 1

while temp > 0:
    divisor = divisor * 10
    temp = temp // 10

if square % divisor == num:
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number") 