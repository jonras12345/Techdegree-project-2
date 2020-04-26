import copy
import constants
import os
import sys
players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
# Had to make a deepcopy of PLAYERS, and TEAMS as they are constants and i
#cant/shoudldn't change them.

experienced = []
not_experienced = []


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
    for player in players:
        if player['experience'] == True:
            experienced.append(player)
        else:
            not_experienced.append(player)

clean_data()

team_1 = []
team_2 = []
team_3 = []
off_set = f'\b'* 34
amt_noob_players = int(len(not_experienced) / len(teams))
amt_exp_players = int(len(experienced) / len(teams))


def sort_exp_players(team):
#sorting experienced players equely amongst teams.
    exp_count = 0
    while exp_count < amt_exp_players and experienced != 0:
        exp_count += 1
        team.insert(0, experienced.pop(0))


def sort_not_exp_players(team):
#sorting not experienced players equely amongst teams.
    noob_count = 0
    while noob_count < amt_noob_players and experienced != 0:
        noob_count += 1
        team.append(not_experienced.pop(0))


def dict_team(team):
#Turning the individual teams into dictionaries with a numeric index
#inorder to make players easier to work with when calling for player_stats.
    index = 1
    team_dict = {}
    for player in team:
        team_dict[index] = player
        index += 1
    return team_dict




def avg_height(team):
    total = 0
    for key, value in team.items():
        total += value['height']
    teams_avg = total / len(team)
    return teams_avg


def players_guardians_list():
    lst_guardians = []
    lst_players = []
    for player in players:
        player_name = [player['name']]
        lst_players = lst_players + player_name
        if len(player['guardians']) == 1:
            guardians = [player['guardians'][0]]
            lst_guardians = lst_guardians + guardians
        if len(player['guardians']) > 1:
            guardian_1 = [player['guardians'][0]]
            guardian_2 = [player['guardians'][1]]
            lst_guardians = lst_guardians + guardian_1 + guardian_2
    print(f'\nThe list of Player Guardians.\n')
    print(', '.join(lst_guardians))
    print(f'\nThe list of Player names.\n')
    print(', '.join(lst_players))
    print('')

def clear():
        """Clears the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')


def display_team_stats(team):

    count = 0
    num_players = len(team)

    lst_guardians = ''
    lst_players = ''
    num = len('------------------------------------------')


    print_boxed(f'Total players: {len(team)}')
    print_boxed(f'Experienced players: {int(len(team)/2)}')
    print_boxed(f'Inexperienced players: {int(len(team)/2)}')
    print_boxed(f'Average Player Height: {round(avg_height(team))}')
    print(f'''\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~ List of players ~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|''')
    for key, value in team.items():
        #Takes the length of input name and subtracts it from the line of
        #dashes to determine the amount of dashes to fill the box.
        sub = len(value['name'])
        diffrence = num - sub
        diff = (' ' + ('-' * (diffrence - 6)))
        print(f"\t|--{key}) {value['name']}{diff}|")
    while True:


        try:
            prompt_3 = int(input(f"""\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~ OPTIONS ~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |-- To view player bio --------------------|
        |-- Enter players number (1-6) ------------|
        |--7) to view list of guardians -----------|
        |--8) to return to team selection ---------|
        |--9) to exit program ---------------------|
        |------->   <------------------------------|{off_set}"""))
            if prompt_3 == 8008:
                players_guardians_list()

            elif prompt_3 < 1 or prompt_3 > 9:
                print(f"""\t|------------------------------------------|
        |-Sorry you failed to enter a valid option-|
        |--please try again------------------------|
        |------------------------------------------|""")
            elif prompt_3 >= 7 and prompt_3 < 10:

                if prompt_3 == 7:
                    lst_guardians = []
                    for player in players:
                        if len(player['guardians']) == 1:
                            guardians = [player['guardians'][0]]
                            lst_guardians = lst_guardians + guardians
                        if len(player['guardians']) > 1:
                            guardian_1 = player['guardians'][0]
                            guardian_2 = player['guardians'][1]
                            lst_guardians = lst_guardians + [guardian_1] + [guardian_2]
                    print('''\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~ PLAYER GUARDIANS ~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|''')
                    for guardian in lst_guardians:
                        print_boxed(guardian)
                    print('\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')


                elif prompt_3 == 8:
                    break

                elif prompt_3 == 9:
                    print(f'''\t|------------------------------------------|
        |--Thank you, come again soon.-------------|
        |------------------------------------------|''')
                    sys.exit()
            else:
                player_bio(team[int(prompt_3)])
                continue

        except ValueError or NameError:
            print(f"""\t|------------------------------------------|
        |-Sorry you failed to enter a valid option-|
        |--please try again------------------------|
        |------------------------------------------|""")
            continue
def print_boxed(string):
    length = len(string)
    needed_length = len('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|') - 6
    diff = needed_length - length
    dash = '-' * diff
    output = f'\t|---' + string +' ' + dash + '|'
    print(output)




def player_bio(player):
    #creates a generic bio about the player
    #which inputs all the player data automatically
    new_old = ''
    if len(player['guardians']) == 1:
        guardians = f"{player['guardians'][0]}"
    if len(player['guardians']) > 1:
        guardians = f"{player['guardians'][0]}, {player['guardians'][1]}"
    if player['experience'] == True:
        new_old = 'n experienced player'
    else:
        new_old = ' new player'
    print('\t|------------------------------------------|')
    print_boxed(f"{player['name']}, is a{new_old}")
    print_boxed(f"Standing at a height of {player['height']}.")
    print_boxed(f"Guardians are as follows:")
    print_boxed(f"{guardians}.")
    print('\t|------------------------------------------|')

def pick_team():
#directs the user to correct teams dictionarie
#Running the all the functions to sort the teams and coerce them into dict{}
    sort_exp_players(team_1), sort_exp_players(team_2)
    sort_exp_players(team_3)
    sort_not_exp_players(team_1), sort_not_exp_players(team_2)
    sort_not_exp_players(team_3)
    panthers = dict_team(team_1)
    bandits = dict_team(team_2)
    warriors = dict_team(team_3)

    while True:
        choice = input(f'''\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~Please choose a team~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |-------1) Panthers -----------------------|
        |-------2) Bandits ------------------------|
        |-------3) Warriors -----------------------|
        |------------------------------------------|
        |------->   <------------------------------|{off_set}''')

        clear()
        if choice == '1':
            print(f"""\n\n\t____________________________________________
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~ *PANTHERS* ~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|""")
            display_team_stats(panthers)

        elif choice == '2':
            print(f"""\n\n\t____________________________________________
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~ *BANDITS* ~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|""")
            display_team_stats(bandits)

        elif choice =='3':
            print(f"""\n\n\t____________________________________________
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~ *WARRIORS* ~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|""")
            display_team_stats(warriors)

        else:
            print(f"""\t|------------------------------------------|
        |-Sorry you failed to enter a valid option-|
        |--please try again------------------------|""")
