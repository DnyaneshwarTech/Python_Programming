def main():
    Age = 0

    Age = int(input("Enter your age : "))

    if Age >= 18:
        if Age >= 60:
            print("You are a Senior Citizen.")
        else:
            print("You are an Adult.")
    else:
        print("You are a Minor.")

if __name__ == "__main__":
    main()