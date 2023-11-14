import json
with open("countries.json", "rt", encoding="utf8") as world:
    countries = json.load(world)

# Creating a capitalPopulations dictionary
capitalPopulations = dict()

# Calculate the total population of capitals for each continent
for country in countries:
    continent = country["continent"]
    capitalPopulation = 0
    
    # Find the population of the capital city
    for city in country["cities"]:
        if city["id"] == country["capital"]:
            capitalPopulation = city["population"]
            break
    
    # Skip continents with capitalPopulation == 0
    if capitalPopulation == 0:
        continue

    # Update the total population for the continent
    if continent not in capitalPopulations:
        capitalPopulations[continent] = 0
    capitalPopulations[continent] += capitalPopulation

# Print the results in alphabetical order of continents
for continent, population in capitalPopulations.items():
    print(f"{continent}: {population}")