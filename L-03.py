import csv
import datetime


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
        print (row)
# End print_name


# -- Methods -------------------------------------------------------


# returns the number of players in the dictionary
def count_players(record):
    return len(record)
# end count_players


# returns a dictionary with only names and birthdates
# def make_date_dict(record):
#     date_dict = {}
#
#     for row in record:
#         date_dict[record] = [row]
#
#     return date_dict
# end make_date_dict


# returns the name of the youngest player
# requires: there be no two players of the exact same age
def find_youngest_player(record):

    youngest_player_name = ""
    max_date = datetime.date(1900, 1, 1)

    for row in record:
        record_dob = record[row][2].split('-')
        record_dob = datetime.date(int(record_dob[0]), int(record_dob[1]), int(record_dob[2]))

        if max_date < record_dob:
            max_date = max(record_dob, max_date)
            youngest_player_name = row

    return youngest_player_name

# end find_youngest_player


# returns the name of the oldest player
# requires: there be no two players of the exact same age
def find_oldest_player(record):

    oldest_player_name = ""
    min_date = datetime.date(2016, 1, 1)

    for row in record:
        record_dob = record[row][2].split('-')
        record_dob = datetime.date(int(record_dob[0]), int(record_dob[1]), int(record_dob[2]))

        if min_date > record_dob:
            min_date = min(record_dob, min_date)
            oldest_player_name = row

    return oldest_player_name

# end find_oldest_player


# collects the countries count and compiles them into a dictionary
def get_country_count(record):
    countries = dict()

    for row in record:

        if record[row][1] in countries:
            countries[record[row][1]] += 1

        else:
            countries[record[row][1]] = 1

    return countries
# end get_country_count


# returns the name of the country with the most players
def most_players(country_record):
    highest = 0
    country_name = ''

    for row in country_record:

        if highest < country_record[row]:
            highest = country_record[row]
            country_name = row
            # print(highest)  # echo

    return country_name
# end most_players


# returns the name of the country with the least players
def least_players(country_record):
    least = 1000
    country_name = ''

    for row in country_record:

        if least > country_record[row]:
            least = country_record[row]
            country_name = row
            # print(least)  # echo

    return country_name
# end least_players


# returns a dictionary
# the values of the list to each key are in the following order:
# 0 - player_id
# 1 - country_id
# 2 - birthdate
def csv_to_dict(csv_file):
    new_dict = {}
    for row in csv_file:
        new_dict[row['name'].strip()] = [row['player_id'], row['country_id'], row['birthdate']]

    return new_dict

# end csv_to_dict


# -------------------------------------------------------------------

# opens the CSV file and puts it into reader
with open('players.csv', 'r', newline="") as playersFile:
    players = csv.DictReader(playersFile, delimiter=',')

# converts the dictReader to a dictionary
    players_dict = csv_to_dict(players)

# prints the number of players in the record
    print('\nThere are ' + str(count_players(players_dict)) + ' players in the record. \n')

    country_dict = get_country_count(players_dict)

    print(most_players(country_dict) + ' has the most players. \n')

    print(least_players(country_dict) + ' has the least players. \n')
    # during testing, I found that there are multiple countries with only one player.  Output will not be consistent

    # print country names
    print('There are the following countries in the record:')
    print('------------------------------------------------')
    for row in country_dict:
        print(row)

    print('The youngest player is ' + find_youngest_player(players_dict))

    print('The oldest player is ' + find_oldest_player(players_dict))







