# Input birth year
birth_year = int(input("Enter your birth year: "))

# Input current year manually (instead of datetime)
current_year = int(input("Enter the current year: "))

# Validation
while birth_year < 0 or birth_year > current_year:
    birth_year = int(input("Invalid year input! Please enter again: "))

# Current age
current_age = current_year - birth_year
print("Your current age:", current_age)

# Age in months
age_in_months = current_age * 12
print("Your age in months:", age_in_months)

# Age in days (approximate)
age_in_days = current_age * 365
print("Your age in days:", age_in_days)

# Age in hours
age_in_hours = age_in_days * 24
print("Your age in hours:", age_in_hours)

# Age in minutes
age_in_minutes = age_in_hours * 60
print("Your age in minutes:", age_in_minutes)

# Years until age 100
years_to_100 = 100 - current_age

if years_to_100 > 0:
    print("Years until age 100:", years_to_100)
elif years_to_100 == 0:
    print("You are 100 years old this year!")
else:
    print("You have already crossed 100 years.")