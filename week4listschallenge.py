# Black-Owned Restaurant Finder: Lists exercises

####################################################################################################
# Think about different cuisines (as many as you want) and store them in a list. Using what you
# learned in the previous exercises, write code that asks the user what cuisine they are interested
# in. If the cuisine they entered is not in the list, print the string "Please choose one of these
# cuisines: [LIST OF CUISINES HERE]".
# YOUR CODE HERE
cuisines = ['American', 'Japanese', 'Vietnamese', 'Chinese', 'Korean', 'French', 'Italian', 'Mexican', 'Thai']
print(cuisines)
cuisine_choice = input("What type of cuisine are you interested in? ")
if cuisine_choice in cuisines:
    print('cool')
else:
    print("Sorry that's not in our list, please choose one that is on this list: ", cuisines)
    cuisine_choice  = input("What type of cuisine are you interested in? ")

####################################################################################################
# Find the name of at least three black-owned restaurants nearby and store their names in a list.
# Then, print out the name of each restaurant, one line at a time.

# TIP: Use Google Maps to find nearby black-owned restaurants
# https://www.google.com/maps/search/black+owned+restaurants 
# YOUR CODE HERE

bor = ["Keith's Chicken and Waffles", "Little Skillet", "Tastebuds" ]
count = 0
print("Here are some local Black Owned Restaurants")
for x in bor:
    print(str(count) + x)
    count += 1
####################################################################################################
# Take your list of restaurants from the previous challenge and print them out in a numbered list.
# Example:
# 1. <RESTAURANT 1>
# 2. <RESTAURANT 2>
# 3. <RESTAURANT 3>

# YOUR CODE HERE

####################################################################################################
# Find out how far away each restaurant is (in miles) and store those distances in another list.
# Then, print out the name of each restaurant AND how far away it is in a numbered list. Example:
# 1. <RESTAURANT 1> is 2.4 miles away
# 2. <RESTAURANT 2> is 6.8 miles away
# 3. <RESTAURANT 3> is 10.2 miles away

# YOUR CODE HERE 