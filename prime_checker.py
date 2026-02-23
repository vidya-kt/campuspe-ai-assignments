# Part 1: Check single number

num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers are not prime")

elif num == 0 or num == 1:
    print(num, "is NOT a prime number")

elif num == 2:
    print("2 is a PRIME number")

else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")


# Part 2: Prime numbers in a range

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=", ")