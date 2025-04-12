

def calculate_score(ml, distraction, social_media, water):
    return (ml * 1) + (water * 20) - (distraction + social_media)*0.5


def feedback(score):
    if score >= 90:
        return "Excellent"
    elif score >= 60:
        return "Good, Keep it up!"
    else:
        return "Needs improvement"
    

days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday"]

for day in days:
    print(f"--{day}--")

    ml = int(input("ML minutes:"))
    distraction = int(input("Distraction minutes:"))
    social_media = int(input("Social Media minutes:"))
    water = float(input("Water in Litters:"))

    score = calculate_score(ml, distraction, social_media, water)
    print(f"Score: {score} - {feedback(score)}")


    

