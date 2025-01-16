import csv

with open('it_company.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in  reader:
        if row['Job Title'] == "Graphic Designer":
            print(f"First Name: {row['First Name']}, Last Name: {row['Last Name']}, E-mail: {row['Email']}")