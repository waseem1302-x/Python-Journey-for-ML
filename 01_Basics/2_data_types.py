# Tutorial 2: Data Types in Python

# String
full_name = "Waseem Mushtaq"

# Integer
age = 21

# Float
daily_study_hours = 3.5

# Boolean
is_international_student = True

# List (ordered, changeable)
languages = ["Python", "HTML", "CSS"]

# Tuple (ordered, unchangeable)
coordinates = (10.5, 20.3)

# Dictionary (key-value pairs)
profile = {
    "name": "Waseem",
    "age": 21,
    "goal": "ML Engineer",
    "country": "Pakistan",
}

# Print each with its type
print("Full Name:", full_name, "| Type:", type(full_name))
print("Age:", age, "| Type:", type(age))
print("Daily Study Hours:", daily_study_hours, "| Type:", type(daily_study_hours))
print("Is International Student:", is_international_student, "| Type:", type(is_international_student))
print("Languages:", languages, "| Type:", type(languages))
print("Coordinates:", coordinates, "| Type:", type(coordinates))
print("Profile:", profile, "| Type:", type(profile))



# Task about data types
#Update the profile dictionary

Profile = {
    "name": "Waseem Mushtaq",
    "age": 21,
    "goal": "ML Engineer",
    "country": "Pakistan",
    "dream_company": "Google",    # Dream company
    "dream_job": "Machine Learning Engineer",   # Dream job
}

# Print the updated profile
print("Updated Profile:", Profile, "| Type:", type(Profile))