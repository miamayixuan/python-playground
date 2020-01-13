import json

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('testwrite.json', 'w') as f:
    json.dump(rows, f, indent=4)