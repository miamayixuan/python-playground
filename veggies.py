# by: Rasim, Mia, and Inayat 
import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#loops through each vegetable
# write the name of each vegetable and the color into a CSV file
with open('vegetables.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(['name', 'color'])
     
     for i in vegetables:
     	writer.writerow([i["name"], i["color"],len(i["name"])])




