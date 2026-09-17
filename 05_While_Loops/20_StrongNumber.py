def main():
    num = int(input("Enter a number : "))

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10

        fact = 1
        cnt = 1

        while cnt <= digit:
            fact = fact * cnt
            cnt += 1

        sum = sum + fact 
        temp = temp // 10

    if sum == num:
        print(num, "is a Strong number")
    else:
        print(num, "is not a Strong number")

if __name__ == "__main__":
    main()