# A number is palindrome if it reads the same forward and backward

num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a Palindrome number")
else:
    print("It is NOT a Palindrome number")