def main():
    iNum = int(input("Enter the number : "))

    iReverse = 0

    while iNum != 0:
        iDigit = iNum % 10
        iReverse = iReverse * 10 + iDigit
        iNum = iNum // 10

    print("Reverse number : ", iReverse)

if __name__ == "__main__":
    main()