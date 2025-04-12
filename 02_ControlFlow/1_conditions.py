#Conditions in Python

is_hungry = False
is_bored = True

if is_hungry:
    print("Let's eat something!")
elif is_bored:
    print("Maybe scroll TikTok or read something fun.")
else:
    print("Great! Let's focus on Python!")


#task about conditions
minutes_per_day = 90

if minutes_per_day >= 90:
    print("Excellent! You're serious about ML!")

elif minutes_per_day >= 30 and minutes_per_day <= 89:
    print("Good, but push a bit more tomorrow!")

elif minutes_per_day < 30:
    print("You can do better! Don't give up!")