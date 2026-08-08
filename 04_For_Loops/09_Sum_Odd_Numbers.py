def main():
    iSum = 0
    iCnt = 0

    for iCnt in range(1,101,2):
        iSum = iSum + iCnt

    print("Sum of odd numbers from 1 to 100 is : ", iSum)

if __name__ == "__main__":
    main()