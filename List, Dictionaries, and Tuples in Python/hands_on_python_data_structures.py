# Task 1
favorite_fruits = ["strawberry", "raspberry", "blackberry", "orange", "blueberry"]

# print original list of favorite fruits
print("Original list:", favorite_fruits)

# add 'lychee' to the list of favorite fruits and print out updated list
favorite_fruits.append("lychee")
print("After adding a fruit:", favorite_fruits)

# remove 'orange' from the list of favorite fruits and print out updated list
favorite_fruits.remove("orange")
print("After rempving a fruit", favorite_fruits)

# print out favorite_fruits in reverse
print("Reversed list", favorite_fruits[::-1])


# Task 2
print("") # print empty line as separatator between tasks

# dictionary to store information
about_me = {"name": "Angelina", "age": 20, "city": "Boston"}

# add new key-value pair to dictionary for 'favorite color'
about_me["favorite color"] = "pink"

# update 'city' to a new value
about_me["city"] = "New York City"

# use a loop to print all the keys and values
keys, values = [], []
for key, value in about_me.items():
    keys.append(key)
    values.append(str(value))

print("Keys:", ', '.join(keys))
print("Values:", ', '.join(values))


# Task 3
print("") # print empty line as separatator between tasks

# tuple to store elements
elements = ("Spider-Man", "Paradise", "Harry Potter")

# print original tuple
print("Favorite things:", elements)

# attempt to change one of the tuple elements
try:
    elements[1] = "Counting Stars"
# catch error
except TypeError:
    # print error msg
    print("Oops! Tuples cannot be changed.")

# print length of the tuple
print("Length of tuple:", len(elements))