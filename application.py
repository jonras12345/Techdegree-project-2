import copy
import constants
import clean_data
#1.  make a "deep copy" of constants.PLAYERS
#2.  Loop through the copy.
#    a. If the player['experience'] is equal to "YES" set player['experience'] equal to True. Otherwise set it to False
#    b. Split the height string. Assign player['height'] the element at the 0 index of the resulting array and converted to an int

# Had to make a deepcopy of PLAYERS, and TEAMS as they are constants and i
#cant/shoudldn't change them.

def start_program():

    print(clean_data.players)
    print(clean_data.experienced)
    print(clean_data.not_experienced)
    print(clean_data.teams)


















if __name__ == '__main__':
    start_program()
