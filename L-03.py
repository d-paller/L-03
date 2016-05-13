import csv

players = {}

with open('players.csv', 'r') as playersFile:
    reader = csv.reader(playersFile)

    for row in reader:
        print(row)





