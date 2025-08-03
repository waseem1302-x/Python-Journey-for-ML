class YouTuber:
    def __init__(self , name, channel, subs,):
        self.name = name
        self.channel = channel
        self.subs = subs


    def show_info(self):
        print(f"{self.name} runs {self.channel} with {self.subs} subscribers")
    
    def upgrade_subscribers(self, new_subs):
        self.subs = new_subs


yt1 = YouTuber("Waseem Mushtaq", "StudyWithWaseem", 12000)
yt1.upgrade_subscribers(20000)
yt1.show_info()  # Should now show 20000

yt1.show_info()
yt2 = YouTuber("Nadeem Mushtaq", "StudyWithNadeem", 12000)
yt2.show_info()



# Class & Objects Attributes

class YouTuber:
    # This is a class attribute — shared by all instances of the class
    platform = "YouTube"

    def __init__(self, name, channel, subs):
        # These are instance attributes — unique for each object
        self.name = name
        self.channel = channel
        self.subs = subs

    def show_info(self):
        # Accessing both instance attributes and class attribute
        print(f"{self.name} runs {self.channel} with {self.subs} subs on {YouTuber.platform}")


# Creating first object (instance) of the class
yt1 = YouTuber("Waseem Mushtaq", "StudyWithWaseem", 12000)

# Creating second object (instance) of the class
yt2 = YouTuber("Nadeem Mushtaq", "StudyWithNadeem", 15000)

# Calling method to show info (will use instance and class attributes)
yt1.show_info()
yt2.show_info()

# Create Student Class that takes name & marks of 3 subjects as argument in Constructor.
# Then create a method to print the avg


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name} your average score is: {sum/3}")

    
s1 = Student("Waseem", [90,85,100])
s1.avg_marks()

