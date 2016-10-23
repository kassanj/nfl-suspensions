import csv

f = open("nfl_suspensions_data.csv")
nfl_suspensions = csv.reader(f)
nfl_suspensions = list(nfl_suspensions)

nfl_suspensions = nfl_suspensions[1:]

years = {}

for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else: 
        years[row_year] = 1

print(years)