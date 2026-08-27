def main():
    iCnt = 1
    iSum = 0

    while iCnt <= 10:
        if iCnt % 2 != 0:
            iSum = iSum + iCnt

        iCnt = iCnt + 1

    print(iSum)

if __name__ == "__main__":
    main()