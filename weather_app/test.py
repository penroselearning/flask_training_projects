import json

with open ("static/data/cities.json") as file:
    cities = json.load(file)

found = False

for i in range(len(cities)):
        if cities[i] == "Ajman":
            found = True

if found == True:
    print("found")
else:
    print("not found")