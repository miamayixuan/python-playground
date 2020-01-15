# by Mia and Inayat

import csv
import json
from pprint import pprint

# Read vegtables.csv into a variable called vegtables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(veggie) for veggie in vegetables] # Convert OrderedDict to regular dict

# Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for veggie in vegetables:
    color = veggie['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veggie)
    else:
        vegetables_by_color[color] = [veggie]

pprint(vegetables_by_color)

# Output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f)