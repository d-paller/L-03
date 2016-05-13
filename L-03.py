import csv

# -- Test methods ----------------------------------------------------


# prints file
# *test method*
def print_file(record):
    for row in record:
        print(row)
# end print_file


# Adds the players to the dictionary
# *test method*
def print_name(record):
    for row in record:
        print (row['name'])
# End print_name


# -- Methods -------------------------------------------------------


# returns the number of players in the dictionary
def count_players(record):
    return len(record)
# end count_players


# returns the name of the youngest player
def find_youngest_player(record):

    youngest_player = 0
    youngest_player_name = ""

    for row in record:
        bd = row['birthdate'].split('-', 1)  # gets the birth date

        if(bd[0] > youngest_player):
            youngest_player_name = row['name']
            youngest_player = bd[0]

    return youngest_player_name

# end find_youngest_player


# returns a dictionary
# the values of the list to each key are in the following order:
# 0 - player_id
# 1 - country_id
# 2 - birthdate
def csv_to_dict(csv_file):
    dict = {}
    for row in csv_file:
        dict[row['name'].strip()] = [row['player_id'], row['country_id'], row['birthdate']]

    return dict

# end csv_to_dict


# -------------------------------------------------------------------

# opens the CSV file and puts it into reader
with open('players.csv', 'r', newline="") as playersFile:
    players = csv.DictReader(playersFile, delimiter=',')

    players_dict = csv_to_dict(players)

    print('There are ' + str(count_players(players_dict)) + ' players in the record.')










