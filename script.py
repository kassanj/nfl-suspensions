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


team = [row[1] for row in nfl_suspensions]
games = [row[2] for row in nfl_suspensions]   
    
unique_teams = set(team)
unique_games = set(games)
    
print(unique_teams)
print(unique_games)


class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
   
third_suspension = Suspension(nfl_suspensions[2])   


class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]    
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0   
    def get_year(self):
        return(self.year)
    
missing_year = Suspension(nfl_suspensions[22])