#  Creating a Dictionary

student_record = {
    "Name" : "Waseee",
    "Age"  : 20,
    "Is_internatioal" : True
}
print(student_record)


# Accessing Items

print(student_record["Name"])       # Waseem
print(student_record.get("Age"))    # 20
print(student_record.get("grade", "Not Available"))  


# Modifying Items
student_record["Major"] = "Computer Science"
student_record["Age"] = 21
print(student_record)



# Removing Items
student_record.pop("Age")
print(student_record)

del student_record["Is_internatioal"]
print(student_record)


# Looping through Dictionary

for key in student_record:
    print(key, ":", student_record[key])

for key, value in student_record.items():
    print(f"{key}: {value}")





# Practice Task

youtuber = {
    "name": "TechNova",
    "subscribers": 874000,
    "niche": "Tech Reviews & Tutorials",
    "verified": True
}
youtuber["platform"] = "YouTube"
youtuber["subscribers"] = 904000
print(youtuber)
print(youtuber.get("country", "Not Available"))


for key,value in youtuber.items():
    print(f"{key} : {value}")