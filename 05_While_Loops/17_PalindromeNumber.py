def main():
    number = int(input("Enter number : "))

    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        print(original, "is a palindrome number")
    else:
        print(original, "is not a palindrome number")
        
if __name__ == "__main__":
    main()