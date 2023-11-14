import json
with (open("countries.json", "rt", encoding="utf8") as world):
    countries = json.load(world)

# Dictionary to store the richest country for each continent
richest = {}

# Iterate through each country and update the richest country for its continent
for country in countries:
    continent = country["continent"]
    gnp = country["gnp"]
    
    # Checking if gnp is None before checking if the continent is not in the dictionary or the gnp is greater than the current richest country's gnp
    if gnp is not None and (continent not in richest or gnp > richest[continent]["gnp"]):
        richest[continent] = {"name": country["name"], "gnp": gnp}


for continent, country in richest.items():
    print(f"{continent}: {country['name']} {country['gnp']}")
    
    """ Output: 
    North America: United States 8510700.0
    Asia: Japan 3787042.0
    Africa: South Africa 116729.0
    Europe: Germany 2133367.0
    South America: Brazil 776739.0
    Oceania: Australia 351182.0
    """