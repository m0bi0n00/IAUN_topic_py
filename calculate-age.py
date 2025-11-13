from datetime import datetime

birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year

age_years = current_year - birth_year

age_days = age_years * 365        
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60

print(f"\nYou are {age_years} years old.")
print(f"Thats about {age_hours:,} hours.")
print(f"Or about {age_minutes:,} minutes.")
print(f"And around {age_seconds:,} seconds.")
