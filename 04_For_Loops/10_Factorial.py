def main():
    iNo = 5 
    iFact = 1
    iCnt = 0

    for iCnt in range(1,iNo + 1):
        iFact = iFact * iCnt

    print("Factorial is : ", iFact)

if __name__ == "__main__":
    main()