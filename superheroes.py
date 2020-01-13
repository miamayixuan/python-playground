#Reads superheroes.json (in this folder)
import json

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

powers = []
members = superheroes['members']
for member in members:
	this_members_powers = member['powers']
	powers.append(this_members_powers)

print(powers)

