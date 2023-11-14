import json
with open("countries.json", "rt", encoding="utf8") as world:
    countries = json.load(world)

# Dictionary to store the least and most populated cities for each country
country_cities_minmax_pop = {}

# Iterate through each country and find the least and most populated cities
for country in countries:
    country_name = country["name"]
    cities = country["cities"]

    # Initialize variables to store information about the least and most populated cities
    min_population_city = {"name": "", "population": float("inf")}
    max_population_city = {"name": "", "population": 0}

    # Iterate through cities to find the least and most populated
    for city in cities:
        population = city["population"]

        # Update minimum population city if needed
        if population < min_population_city["population"]:
            min_population_city["name"] = city["name"]
            min_population_city["population"] = population

        # Update maximum population city if needed
        if population > max_population_city["population"]:
            max_population_city["name"] = city["name"]
            max_population_city["population"] = population

    # Update the dictionary with the information for the current country
    country_cities_minmax_pop[country_name] = {"min": min_population_city, "max": max_population_city}

# Print the results
for name, minmax_city in country_cities_minmax_pop.items():
    min_city = minmax_city['min']
    max_city = minmax_city['max']
    print(f"{name}: min: {min_city['name']}: {min_city['population']}")
    print(f"{name}: max: {max_city['name']}: {max_city['population']}")