def main():
    number = int(input("Enter number : "))

    original = number
    sum = 0

    while number > 0:
        digit = number % 10
        sum = sum + (digit * digit * digit)
        number = number // 10

    if original == sum:
        print(original, "is an Armstrong number")
    else:
        print(original, "is not an Armstorng number")

if __name__ == "__main__":
    main()