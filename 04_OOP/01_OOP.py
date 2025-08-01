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
