def calculate_score(ml,distractions,social_media, water):
    return (ml *1) + (water * 20) - (distractions + social_media) * 0.5


def feedback(score):
    if score >= 100:
        return "Excellent work"
    elif score >= 60:
        return "Good Wrok! Keep it up"
    else:
        return "You need Improvement"
    

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in Days:
    print (f"\n---{day}---")

    ml = int(input("Enter Machine Learning Minutes: "))
    distractions = int(input("Enter Distraction Minutes: "))
    social_media = int(input("Enter Social Media Minutes: "))
    water = float(input("Enter number water in Litters: "))


    score = calculate_score(ml,distractions,social_media,water)
    print(f"Your Score is: {score:.1f} - {feedback(score)}")
