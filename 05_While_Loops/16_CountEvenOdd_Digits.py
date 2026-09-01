def main():
    Num = int(input("Enter a number : "))

    Even = 0
    Odd = 0

    while Num > 0:
        Digit = Num % 10

        if Digit % 2 == 0:
            Even += 1
        else:
            Odd += 1

        Num = Num // 10

    print("Even digits = ", Even)
    print("Odd digits = ", Odd)

if __name__ == "__main__":
    main()