import json
with open("countries.json", "rt", encoding="utf8") as world:
    countries = json.load(world)

# Dictionary to store the number of countries on each continent
num_countries_in_continents = {}

# Count the number of countries on each continent
for country in countries:
    continent = country["continent"]
    
    # Update the count for the continent
    if continent not in num_countries_in_continents:
        num_countries_in_continents[continent] = 0
    num_countries_in_continents[continent] += 1

# Print the results
for continent, counts in num_countries_in_continents.items():
    print(f"{continent}: {counts}")