#!/usr/bin/env python3

"""
I declare that this assignment is my own work in accordance with Seneca Academic Policy.
No part of this assignment has been copied manually or electronically from any other source (including web sites) or distributed to other
students.

Student name: Aleksander Savotchka
Student ID number: 115894214
Due Date: 2023-10-22
Submission Date: 2023-10-22

"""
# QUESTION 1:

from datetime import datetime

# The library "datetime," processes our system's real-time, and helps use to manipulate date
# and time.

# The Two Variables
timeOfTheDay = "21:23:00"
sunSetsAt = "19:17:00"

# The current time is equal to our system's time currently, whilst the sunset time converts the "time," string into the datetime library object.
current_time = datetime.now().time()
sunset_time = datetime.strptime(sunSetsAt, "%H:%M:%S").time()

# If the current time is before 11:59 AM we return a "Good morning," message. If the current time is after 11:59 AM but before the sunset we will return a "Good afternoon," message. And if the time is after the sunset we return a "Good evening," message.
if current_time < sunset_time:
    if current_time < datetime.strptime("11:59:00", "%H:%M:%S").time():
        message = "Good morning"
    else:
        message = "Good afternoon"
else:
    message = "Good evening"

# The value "John," is stored into the variable 'user_name'
user_name = "John"
# We print the values using the F string. The code will process our system's time, and returna message as well as a user name in accordance to our system's time.
print(f"{message} {user_name}")

# QUESTION 2:

# Value stored in text variable
text = "Guido van Rossum began working on Python in the late 1980s."

# Converts text to lowercase
text = text.lower()

max_char = ""
max_count = 0

# Looping through each character of the text
for char in text:
    if char.isalpha(): # Checking if the character is a letter or not.
        char_count = text.count(char) # Counts the amount of times the character appears in the text
        if char_count > max_count:
            max_count = char_count
            max_char = char

# Printing the output
print(f"Letter {max_char.upper()} is repeated ({max_count} times) in this text")
