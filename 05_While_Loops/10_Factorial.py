def main():
    iNum = int(input("Enter number : "))

    iCnt = 1
    iFact = 1

    while iCnt <= iNum:
        iFact = iFact * iCnt
        iCnt = iCnt + 1

    print(iFact)

if __name__ == "__main__":
    main()