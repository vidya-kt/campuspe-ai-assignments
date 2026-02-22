from datetime import datetime

# taking valid day input
day = int(input("Enter birth day: "))
while day < 1 or day > 31:
    day = int(input("Invalid day! Enter again (1-31): "))

# taking valid month input
month = int(input("Enter birth month: "))
while month < 1 or month > 12:
    month = int(input("Invalid month! Enter again (1-12): "))

# taking valid year input
current_year = datetime.now().year
year = int(input("Enter birth year: "))
while year > current_year:
    year = int(input("Invalid year! Cannot be in future. Enter again: "))

# checking full date is not in future
birth_date = datetime(year, month, day)
today = datetime.now()

while birth_date > today:
    print("Birth date is in the future! Enter again.")
    
    day = int(input("Enter birth day: "))
    while day < 1 or day > 31:
        day = int(input("Invalid day! Enter again (1-31): "))

    month = int(input("Enter birth month: "))
    while month < 1 or month > 12:
        month = int(input("Invalid month! Enter again (1-12): "))

    year = int(input("Enter birth year: "))
    while year > current_year:
        year = int(input("Invalid year! Enter again: "))

    birth_date = datetime(year, month, day)

# calculating age in years
age = today.year - year

# checking if birthday has occurred this year
if today.month < month:
    age = age - 1
elif today.month == month:
    if today.day < day:
        age = age - 1

print("\nCurrent age:", age)

# approximate conversions
months = age * 12
print("Age in months:", months)

days = age * 365
print("Age in days:", days)

hours = days * 24
print("Age in hours:", hours)

minutes = hours * 60
print("Age in minutes:", minutes)

# years left to reach 100
years_left = 100 - age
if years_left < 0:
    years_left = 0

print("Years until age 100:", years_left)