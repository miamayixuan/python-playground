#by Mia and Rasim

#Reads superheroes.json (in this folder)

import json
import csv

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# Write a header to the CSV file
with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    headers = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active"]
    writer.writerow(headers)

# Loop over the members

    squad = superheroes['squadName']
    home = superheroes['homeTown']
    date = superheroes['formed']
    secBase = superheroes['secretBase']
    active = superheroes['active']
    members = superheroes['members']
    squad = superheroes['squadName']
    
    for member in members:
    	name = member['name']
    	age = member['age']
    	sec_ID = member['secretIdentity']
    	power = member['powers']
    	row = [name,age,sec_ID,power,squad,home,date,secBase,active]
    	writer.writerow(row)

