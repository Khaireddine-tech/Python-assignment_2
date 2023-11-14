import json
with open("countries.json", "rt", encoding="utf8") as world:
    countries = json.load(world)

# Set to store unique continents (because a set in Python cannot have duplicate elements)
continents_set = set()

# Loop through each country and add its continent to the set
for country in countries:
    continents_set.add(country["continent"])

# Convert the set to a list
continents = list(continents_set)
# Sort the list alphabetically
continents.sort()

# Print the sorted list of continents
print(continents) 