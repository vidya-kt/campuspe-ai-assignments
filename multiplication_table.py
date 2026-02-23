number = int(input("Enter a number: "))
end = int(input("Enter the range (end): "))

print("Multiplication table of",number)

#multiplication table of a specific number
for i in range(end):
    print(number,"x",i+1,"=",number*(i+1))

#multiplication table from 1 to 10
print("Multiplication Table from 1 to 10\n")

# top line
print("------------------------------------------------------------")

# column numbers
print("|      ", end="")
for i in range(1, 11):
    print(i, end="   | ")
print()

print("------------------------------------------------------------")

# table
for i in range(1, 11):
    print("|", i, " ", end="| ")

    for j in range(1, 11):
        value = i * j

        # spacing adjustment for alignment
        if value < 10:
            print(value, "  ", end="| ")
        elif value < 100:
            print(value, " ", end="| ")
        else:
            print(value, end="| ")

    print()
    print("------------------------------------------------------------")

