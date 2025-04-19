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



# Step 1
shopping_cart = ["Milk", "Eggs", "Bread", "Oil"]
print(shopping_cart)

# Step 2
shopping_cart.append("Butter")
print(shopping_cart)

# Step 3
shopping_cart.insert(2, "Detergent")
print(shopping_cart)

# Step 4
if "Oil" in shopping_cart:
    shopping_cart.remove("Oil")
    print(shopping_cart)

# Step 5
shopping_cart.pop()
print(shopping_cart)

# Step 6
shopping_cart.sort()

# Final Output
print("Final Shopping Cart:", shopping_cart)


study_sessions = [45, 60, 30, 90, 75, 50]
print("Original: ", study_sessions)

# Sort the list
study_sessions.sort()
print("Sorted (Ascending): ", study_sessions)

# Longest and Shortest
longest = max(study_sessions)
shortest = min(study_sessions)
print("Longest Session:", longest, "minutes")
print("Shortest Session:", shortest, "minutes")

# Average calculation
average = sum(study_sessions) / len(study_sessions)
print("Average Study Time:", round(average, 1), "minutes")

# Reversed
study_sessions.reverse()
print("Descending Order: ", study_sessions)


Smart_Cart = ['apple', 'bread', 'milk', 'protein bar', 'rice', 'yogurt']
print("Orignal: ", Smart_Cart)

Smart_Cart.append("Orange")
Smart_Cart.append("Banana")
print("2 More Items added: ", Smart_Cart)

Smart_Cart[3] = "Chips"
print("Replaced: ", Smart_Cart)

if "Chips" in Smart_Cart:
    Smart_Cart.remove("Chips")
    print("Removed unhealthy item: ", Smart_Cart)

Smart_Cart.sort()
print("Sorted list: ", Smart_Cart)



