year = int(input("Enter a year: "))

if year % 4 != 0:
    print(year, "is NOT a leap year.")
    print("Reason: It is not divisible by 4.")

elif year % 100 != 0:
    print(year, "is a leap year.")
    print("Reason: It is divisible by 4 but not divisible by 100.")

elif year % 400 == 0:
    print(year, "is a leap year.")
    print("Reason: It is divisible by 400.")

else:
    print(year, "is NOT a leap year.")
    print("Reason: It is divisible by 100 but not divisible by 400.")