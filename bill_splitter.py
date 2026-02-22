total_amt = float(input("Enter the total bill amount(in INR): "))
no_people = int(input("Enetr the number of people: "))
tax_percent = float(input("Enter the tax percentage: "))
tip_percent = float(input("Enter the tip percentage: "))

print()
print("="*10 +"BILL BREAKDOWN" +"="*10)

print("  Subtotal".ljust(20), ": ₹", total_amt)

tax_amt = total_amt*tax_percent/100
print("  Tax (", tax_percent, "%)".ljust(7), ": ₹", tax_amt)

after_tax = total_amt+tax_amt
print("  After Tax".ljust(20), ": ₹", after_tax)

tip_amt = total_amt*tip_percent/100
print("  Tip (", tip_percent, "%)".ljust(8), ": ₹", tip_amt)

total_bill = total_amt+tax_amt+tip_amt
print("  Total payable".ljust(20), ": ₹", total_bill)

per_person = total_bill/no_people
print("  Amount per person".ljust(20), ": ₹", per_person)

print("="*34)
