def health_score(sleep_hours,exercise_minutes, junk_food,screen_time):
    return (sleep_hours * 10) + (exercise_minutes * 0.5) - (junk_food * 5 + screen_time * 2)

def feedback(score):
    if score >= 80:
        return "Great! Healthy Week!"
    elif score >= 50:
        return "Good, but can improve"
    else:
        return "Focus more on health."
    

Days = ["Monday","Tuesday"]

for day in Days:
    print(f"\n---{day}---")

    SleepHours = int(input("Enter Your Sleep Hours: "))
    ExerciseMin = int(input("Enter your Exercise Minutes: "))
    JunkFood = int(input("Enter Number of Junk Food Consuption: "))
    ScreenTime = int(input("Enter Your Screen Time: "))

    score = health_score(SleepHours,ExerciseMin,JunkFood,ScreenTime)

    print(f"Score: {score:.1f} - {feedback(score)}")
