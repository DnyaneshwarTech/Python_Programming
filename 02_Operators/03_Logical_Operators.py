def main():
    No1 = 0
    No2 = 0

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    print()
    
    print("Logical Operators Result : ")

    print()

    print("Logical AND (and) : ",(No1 > 0) and (No2 > 0))
    print("Logical OR (or) : ",(No1 > 0) or (No2 > 0))
    print("Logical NOT (not) : ",not (No1 > 0))

if __name__ == "__main__":
    main()