my_list = [1,2,3,4,5,1]
print(my_list)


fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)


# Task: Create a list of your 5 favorite YouTubers. Replace one, Add one more, Remove one.
# Then print the updated list.


my_fav_youtuber = ["Singh in USA", "Mr Beast", "iShow Speed", "Wildlenz by Abrar", "Good Life"]
print(my_fav_youtuber)  #list
my_fav_youtuber[-1] = "Harnoor"
print(my_fav_youtuber) # Replaced 
my_fav_youtuber.append("Nadeem")
print(my_fav_youtuber) #added 
del my_fav_youtuber[3]
print(my_fav_youtuber) # Removed


my_fav_youtubers = ["Ali", "Ahsan", "Ayesha", "Yahya", "Hasnat"]
print("First 3 Youtubers", my_fav_youtubers[:3])
print("Last 2 Youtubers", my_fav_youtubers[-2:])
print("Revered List" , my_fav_youtubers[::-1])



