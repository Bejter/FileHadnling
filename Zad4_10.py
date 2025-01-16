import csv

with open('clothing.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in  reader:
        if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
            print(row)