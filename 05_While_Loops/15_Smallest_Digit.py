def main():
    Num = int(input("Enter a number : "))

    Smallest = 9

    while Num > 0:
        Digit = Num % 10

        if Digit < Smallest:
            Smallest = Digit

        Num = Num // 10

    print("Smallest digit = ", Smallest)

if __name__ == "__main__":
    main();