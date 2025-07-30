# Creating a Set

set1 = {1,2,3,4,5}
print(set1)
print(type(set1))


# Removing Duplicates Automatically

list1 = [1,2,2,3,4,5,5]
unique_set = set(list1)
print(unique_set)


# Common Set Methods
s = {1, 2, 3}
print(s)
s.add(4)           # Add one item
print(s)
s.update([5, 6])   # Add multiple items
print(s)
s.remove(2)        # Remove item (error if not found)
print(s)
s.discard(10)      # Remove item (no error if not found).............best practice
print(s)
s.clear()          # Remove all items
print(s)


# Set Operations

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))



# Set is Unordered
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
