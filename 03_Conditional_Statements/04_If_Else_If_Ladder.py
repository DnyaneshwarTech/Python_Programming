def main():
    Marks = 0

    Marks = int(input("Enter your marks : "))

    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    elif Marks >= 35:
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    main()