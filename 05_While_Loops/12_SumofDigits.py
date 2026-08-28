def main():
    iNum = int(input("Enter the number : "))

    iSum = 0

    while iNum != 0:
        iDigit = iNum % 10
        iSum = iSum + iDigit
        iNum = iNum // 10

    print("Sum of digits : ", iSum)

if __name__ == "__main__":
    main()