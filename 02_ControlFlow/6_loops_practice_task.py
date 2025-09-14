#diving deep into loops
#Print numbers from 1 to 10:
for i in range(1,11):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


#task

def calculate_total(spending_list):
    return sum(spending_list)

def budget_feedback(total, budget):
    if total <= budget:
        return "Great! You're within your budget."
    else:
        return f"Oops! You exceeded your budget by {total - budget} units."

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
spending = []

for day in days:
    amount = float(input(f"Enter grocery spending for {day}: "))
    spending.append(amount)

total_spent = calculate_total(spending)
print(f"\nTotal Spending: {total_spent}")
print(budget_feedback(total_spent, budget=200))

#task 2

def calculate_score(study_min, sleep_hours, distraction_min, screen_time):
    return (study_min * 2) + (sleep_hours * 1.5) - ((distraction_min - screen_time) * 1)


def feedback(score):
    if score >= 80:
        return "Great Day! You're on fire!"
    
    elif score >= 50:
        return "Doing good, stay consistent!"
    
    else:
        return "Focus more, you can do better."

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:

    print(f"\n---{day}---")
    study_min = int(input("Enter Your Study Minutes: "))
    sleep_hours = int(input("Enter your Sleep Hours: "))
    distraction_min = int(input("Enter Your Distraction Minutes: "))
    screen_time = int(input("Enter Your Screen Time"))


    score = calculate_score(study_min, sleep_hours, distraction_min, screen_time)
    print(f"Score: {score:.1f} - {feedback(score)}")