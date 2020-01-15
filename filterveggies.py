#by Mia and Inayat

import csv
import json
# Read vegetables.csv into a variable called vegetables.

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(veggie) for veggie in vegetables] # Convert OrderedDict to regular dict


# Loop through vegetables and filter down to only green vegtables using a whitelist.

green_vegetables = []
whitelist = ['green']
for veggie in vegetables:
    if veggie['color'] in whitelist:
        green_vegetables.append(veggie)

# Print veggies to the terminal
print(green_vegetables)

# Write the veggies to a json file called greenveggies.json
with open('green_veggies.json', 'w') as f:
    json.dump(green_vegetables, f)

#output another csv called green_vegetables.csv
with open('green_vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
    for veggie in green_vegetables:
    	writer.writerow([veggie["name"], veggie["color"]])








