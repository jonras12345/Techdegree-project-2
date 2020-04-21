import copy
import constants

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
# Had to make a deepcopy of PLAYERS, and TEAMS as they are constants and i
#cant/shoudldn't change them.

experienced = []
not_experienced = []
sep_teams = [[teams[0]], [teams[1]], [teams[2]]]


def clean_data():
    #converting all player data to a easier to work wit format
    #experience = True or false. Height broken down into an INT.
    #guardians split up into list
    for player_stats in players:
        if player_stats['experience'] == 'YES':
            player_stats['experience'] = True
        else:
            player_stats['experience'] = False
        player_stats['guardians'] = player_stats['guardians'].split(" and ")
        player_stats['height'] = int(player_stats['height'][:2])



def exp_vs_no_exp():
    for player in players:
        if player['experience'] == True:
            experienced.append(player)
        else:
            not_experienced.append(player)


def convert_teams():
    pass

def split_teams():
    amt_players = int(len(players) / len(teams))
    for team in sep_teams:
        while experienced:
            [team.insert(0, experienced)]
        while not_experienced:
            [team.insert(-1, not_experienced)]





clean_data()
exp_vs_no_exp()
convert_teams()
print(teams)
print(sep_teams)
split_teams()
print(experienced)
print(sep_teams)
print(sep_teams[1])
print(sep_teams[0])
print(teams)
