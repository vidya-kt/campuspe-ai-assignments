def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

while True:
    print()
    print("="*8,"Temperature Converter","="*8)
    print("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. Celsius to Kelvin \n4. Kelvin ot Celsisu \n5. Fahrenheit to Kelvin \n6. Kelvin to Fahrenheit \n7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you! Exiting.....")
        break

    if choice in ['1','2','3','4','5','6']:
        try:
            temp = float(input("Enter the temperature value: "))
        except ValueError:
            print("Invalid input! Enter a numeric value: ")
            continue

        if choice == '1':
            print("Result (Celsius to Fahrenheit):",celsius_to_fahrenheit(temp),"°F")
        elif choice == '2':
            print("Result (Fahrenheit to Celsius):",fahrenheit_to_celsius(temp),"°C")
        elif choice == '3':
            print("Result (Celsius to Kelvin:",celsius_to_kelvin(temp),"°K")
        elif choice == '4':
            if temp<0:
                print("Kelvin value cannot be negative.")
            else:
                print("Result (Kelvin to Celsius:",kelvin_to_celsius(temp),"°C")
        elif choice == '5':
            print("Result (Fahrenheit_to_kelvin):",fahrenheit_to_kelvin(temp),"°K")
        elif choice == '6':
            if temp<0:
                print("Kelvin value cannot be negative.")
            else:
                print("Result (Kelvin to Fahrenheit:",kelvin_to_fahrenheit(temp),"°F")
    else:
        print("Invalid Choice! Please select between 1 to 7.")

