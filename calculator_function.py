# functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

#Square root
def square_root(a):
    if a < 0:
        return "Invalid (negative number)"
    else:
        return a ** 0.5

#Percentage
def percentage(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return (a / b) * 100


#Main function
def calculator():

    while True:

        print("\n--- SIMPLE CALCULATOR ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "9":
            print("Exiting calculator...")
            break

        # operations with two inputs
        if choice in ["1", "2", "3", "4", "5", "6", "8"]:

            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)

            elif choice == "2":
                result = subtract(a, b)

            elif choice == "3":
                result = multiply(a, b)

            elif choice == "4":
                result = divide(a, b)

            elif choice == "5":
                result = modulus(a, b)

            elif choice == "6":
                result = power(a, b)

            elif choice == "8":
                result = percentage(a, b)

            print("Result:", result)

        # square root (only one input)
        elif choice == "7":
            a = int(input("Enter number: "))
            result = square_root(a)
            print("Result:", result)

        else:
            print("Invalid choice")


# function call
calculator()