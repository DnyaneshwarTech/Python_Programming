def main():
    num = int(input("Enter a number : "))

    cnt = 1
    sum = 0

    while cnt < num:
        if num % cnt == 0:
            sum = sum + cnt

        cnt += 1

    if sum == num:
        print(num, "is a Perfect number")
    else:
        print(num, "is not a Perfect number")

if __name__ == "__main__":
    main()