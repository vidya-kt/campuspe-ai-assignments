from datetime import datetime

birth_year = int(input("Enter your birth year:"))
while(birth_year<0 or birth_year>datetime.now().year):
    birth_year = int(input("Invalid year input! Please enter again:"))

#current_age = current_year - birth_year
current_year = datetime.now().year
current_age = current_year-birth_year
print("Your currenr age:", current_age)

#Age in months
age_in_months = current_age*12
print("Your age in months:",age_in_months)

#Age in days
age_in_days = current_year*365
print("Your age in days:", age_in_days)

#Age in hours
age_in_hours = age_in_days*24
print("Your age in hours:", age_in_hours)

#Age in minutes
age_in_minutes = age_in_hours*60
print("Your age in minutes:", age_in_minutes)

#Years until age 100
print("Years until age 100:", 100-current_age)

