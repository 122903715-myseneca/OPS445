#!/usr/bin/env python3

"""
I declare that this assignment is my own work in accordance with Seneca Academic Policy.
No part of this assignment has been copied manually or electronically from any other source.
(Including web sites) or distributed to other students.
Please update the following section with your information:

Student Name: Aleksander Savotchka
Student ID number: 115894214
Due Date: 2023-10-16
Submission Date:
"""
# QUESTION 1:

# Implementing a loop whilst inputting user value into firstName, lastName and id variables. If the user
# enters the letter "Q" on any of the inputs, the script will quit. NOTE: this only works with capital Q not lowercase.

while True:
    firstName = input("Please enter your first name: ")
    if firstName == 'Q':
        break

    lastName = input("Please enter your last name: ")
    if lastName == 'Q':
        break
    
    id = input("Please enter ID: ")
    if id == 'Q':
        break

# The year of birth is equal to the last 4 digits of the ID value. E.x: 11581999 = 1999
# The initials are formatted so that the first letter of the user input of the firstname, and the first letter of
# the user inputs last name is displayed.

    year_of_birth = id[-4:]
    initials = f"{firstName[0]}.{lastName[0]}."

# Finally, we put the values.

    print(f"{firstName} {lastName} ({initials}), born in {year_of_birth}")

# QUESTION 2:

# Defining the variables

dateOfBirth = "12/13/1995"
todayDate = "09/21/2022"
timeOfTheDay = "21:23:00"
sunSetsAt = "19:17:00"

# We must parse the date and time
dob_month, dob_day, dob_year = map(int, dateOfBirth.split('/'))
current_month, current_day, current_year = map(int, todayDate.split('/'))
current_hour, current_minute, current_second = map(int, timeOfTheDay.split(':'))
sunset_hour, sunset_minute, sunset_second = map(int, sunSetsAt.split(':'))

# Calculating the age in years, months, days, hours, minutes, seconds.
age_years = current_year - dob_year
age_months = (current_month - dob_month) + 12 * age_years
age_days = current_day - dob_day

if age_days < 0:
    age_months -= 1
    age_days += 30

age_hours = current_hour - sunset_hour
age_minutes = current_minute - sunset_minute
age_seconds = current_second - sunset_second

# Now we print the results
print(f"You are {age_years} years old")
print(f"or {age_months} months")
print(f"or {age_days} days")
print(f"or {age_hours} hours")
print(f"or {age_minutes} minutes")
print(f"or {age_seconds} seconds")

