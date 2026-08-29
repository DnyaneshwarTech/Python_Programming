def main():
    iNum = int(input("Enter number : "))

    iLargest = 0

    while iNum != 0:
        iDigit = iNum % 10

        if iDigit > iLargest:
            iLargest = iDigit

        iNum = iNum // 10

    print("Largest digit = ", iLargest)

if __name__ == "__main__":
    main()