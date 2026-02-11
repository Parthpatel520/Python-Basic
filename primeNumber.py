# A number is prime if it is divisible only by 1 and itself
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("It is NOT a Prime number")
            break
    else:
        print("It is a Prime number")
else:
    print("It is NOT a Prime number")
