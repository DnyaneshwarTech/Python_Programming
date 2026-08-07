def main():
    iNo = 5
    iMult = 0
    iCnt = 0

    print("Table of %d: ", iNo)

    for iCnt in range(1,11):
        iMult = iNo * iCnt
        print(iMult)

if __name__ == "__main__":
    main()