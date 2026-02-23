print("Factorial Calculation: ")
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("0! = 1")

else:
    fact = 1

    print(num, "! = ", sep="", end="")

    for i in range(num, 0, -1):
        fact = fact * i

        if i != 1:
            print(i, "×", end=" ")
        else:
            print(i, end=" ")

    print("=", fact)

