# 1. factorial
def factorial(n):
    if n < 0:
        return "Not possible"
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


# 2. is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 3. fibonacci nth term
def fibonacci(n):
    if n <= 0:
        return "Invalid"
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b


# 4. sum of digits
def sum_of_digits(n):
    s = 0
    n = abs(n)
    while n > 0:
        d = n % 10
        s = s + d
        n = n // 10
    return s


# 5. reverse number
def reverse_number(n):
    rev = 0
    neg = False

    if n < 0:
        neg = True
        n = -n

    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    if neg == True:
        rev = -rev

    return rev


# 6. armstrong
def is_armstrong(n):
    temp = abs(n)
    digits = len(str(temp))
    s = 0
    copy = temp

    while copy > 0:
        d = copy % 10
        s = s + (d ** digits)
        copy = copy // 10

    if s == temp:
        return True
    else:
        return False


# 7. gcd
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# 8. lcm
def lcm(a, b):
    g = gcd(a, b)
    l = (a * b) // g
    return l


# 9. perfect number
def is_perfect_number(n):
    if n <= 0:
        return False

    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i

    if s == n:
        return True
    else:
        return False


# 10. menu
def math_menu():

    while True:

        print("\n=== MATH MENU ===")
        print("1. Factorial")
        print("2. Prime check")
        print("3. Fibonacci")
        print("4. Sum of digits")
        print("5. Reverse number")
        print("6. Armstrong number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect number")
        print("10. Exit")

        ch = input("Enter choice: ")

        if ch == "10":
            print("Exiting...")
            break

        elif ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif ch == "2":
            n = int(input("Enter number: "))
            if is_prime(n):
                print("Prime")
            else:
                print("Not Prime")

        elif ch == "3":
            n = int(input("Enter position: "))
            print("Fibonacci term:", fibonacci(n))

        elif ch == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif ch == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif ch == "6":
            n = int(input("Enter number: "))
            if is_armstrong(n):
                print("Armstrong number")
            else:
                print("Not Armstrong")

        elif ch == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif ch == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif ch == "9":
            n = int(input("Enter number: "))
            if is_perfect_number(n):
                print("Perfect number")
            else:
                print("Not perfect")

        else:
            print("Invalid choice")


math_menu()