print("Ticket price list:")
print("Below 3: Free")
print("3-12: ₹150 (Child)")
print("13-59: ₹300 (Adult)")
print("60+: ₹200 (Senior)")

print("\nDiscount details:")
print("Monday-Thursday: No discount")
print("Friday-Sunday: 20% discount")

no_tickets = int(input("\nEnter the number of tickets: "))

base_price = 0

for i in range(no_tickets):
    age = int(input(f"Enter age of person {i+1}: "))

    if age < 3:
        price = 0
    elif age <= 12:
        price = 150
    elif age <= 59:
        price = 300
    else:
        price = 200

    base_price += price

day = input("Enter the day of the week (Ex- Monday): ")

print("\nPayment Details:")
print("Base Price: ₹", base_price)

# Discount calculation
if day in ["Friday", "Saturday", "Sunday"]:
    discount = base_price * 0.20
else:
    discount = 0

final_price = base_price - discount

print("Discount: ₹", discount)
print("Price after discount: ₹", final_price)
print("Total Amount: ₹", final_price)