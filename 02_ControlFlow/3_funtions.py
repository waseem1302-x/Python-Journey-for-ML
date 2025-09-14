# Define a simple function
def motivate_me():
    print("You got this Waseem! Time to grind for greatness!")

# Call the function
motivate_me()



# Task about functions
def study_minutes(minutes):
    if minutes >= 120:
        print("Excellent Focus !")
    elif minutes >= 60:
        print("Good! Keep it up!")
    else:
        print("Do better tomorrow!")
    
study_minutes(120)
study_minutes(60)
study_minutes(30)


#working with parameters 

def efficiency_score(ml_minutes, youtube_minutes, distractions_minutes):
    score = (ml_minutes * 2 + youtube_minutes * 1.5 - distractions_minutes * 2) / 10
    return f"Your productivity score is: {score:.2f}"

print(efficiency_score(120, 60, 30))

def is_focused_day(ml_minutes, distractions_minutes):
    
    if distractions_minutes <=30 and ml_minutes >= 90:
        return "Your Days is Focused Day!"
    else:
        return "Need More focus Tommorow"
    
print(is_focused_day(120, 30))


def daily_performance(ml_minutes, youtube_minutes, sleep_hours):

    score = 0

    if ml_minutes >= 90:
        score += 40
    elif ml_minutes >= 60:
        score += 30
    else:
        score += 10

    if youtube_minutes <= 60:
        score += 30
    else:
        score += 10

    if sleep_hours >= 6:
        score += 30
    else:
        score += 10

    return f"Your productivity score is: {score}/100"

print(daily_performance(120, 30, 7))
print(daily_performance(60, 120, 4))


# Task about functions with parameters

def daily_focus_report(ml_minutes, distractions_minutes, social_media_minutes,water_intake):
    
    score = 0
    if ml_minutes >= 90:
        score += 40
    elif ml_minutes >= 60:
        score += 30
    else:
        score += 10

    if distractions_minutes <= 30:
        score += 30
    else:
        score += 10
    
    if social_media_minutes <= 30:
        score += 30
    else:
        score += 10
    
    if water_intake >= 2:
        score += 30
    else:
        score += 10
    
    return f"Your daily focus report is: {score}/100"


print(daily_focus_report(120, 20, 15, 3))
print(daily_focus_report(60, 40, 50, 1))    
print(daily_focus_report(90, 20, 15, 2))
print(daily_focus_report(50, 40, 50, 1))


# Working with mutliple funtions 

def get_ml_score(ml_minutes):
    if ml_minutes >= 90:
        return 40  
    elif ml_minutes >= 60:
        return 30
    else:
        return 10  
    
def get_distraction_score(distractions_minutes):
    if distractions_minutes <= 30:
        return 30  
    else:
        return 10
    

def get_social_media_score(social_media_minutes):
    if social_media_minutes <= 30:
        return 30  
    else:
        return 10
    
def full_day_score(ml, distractions, social_media):
    ml_score = get_ml_score(ml)
    distraction_score = get_distraction_score(distractions)
    social_media_score = get_social_media_score(social_media)

    return ml_score + distraction_score + social_media_score

print(full_day_score(120, 20, 15))  # 100

