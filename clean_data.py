import copy
import constants
#1.  make a "deep copy" of constants.PLAYERS
#2.  Loop through the copy.
#    a. If the player['experience'] is equal to "YES" set player['experience'] equal to True. Otherwise set it to False
#    b. Split the height string. Assign player['height'] the element at the 0 index of the resulting array and converted to an int

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
# Had to make a deepcopy of PLAYERS, and TEAMS as they are constants and i
#cant/shoudldn't change them.
experienced = []
not_experienced = []
def clean_data():
    for player_stats in players:
        #converting 'experience' to True or False to make easier to work with
        if player_stats['experience'] == 'YES':
            player_stats['experience'] = True
        else:
            player_stats['experience'] = False



    for player_stats in players:
        #converting height to an INT
        player_stats['height'] = player_stats['height'].split()
        player_stats['height'] = int(player_stats['height'][0])


def exp_vs_no_exp():
    for player in players:
            if player['experience'] == True:
                experienced.append(player)
            else:
                not_experienced.append(player)


def split_teams():
    for team in teams:
        list(team)
    while experienced:
        for team in teams:
            list(team).append(experienced[0])
    print(teams)
    print(team)




clean_data()
exp_vs_no_exp()
#for player in experienced:
    #print(player)

#for player in not_experienced:
    #print(player)

split_teams()
