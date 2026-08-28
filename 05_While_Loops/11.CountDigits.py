def main():
    iNum = int(input("Enter the number : "))

    iCount = 0

    while iNum != 0:
        iNum = iNum // 10
        iCount = iCount + 1

    print("Number of digits : ", iCount)

if __name__ == "__main__":
    main()