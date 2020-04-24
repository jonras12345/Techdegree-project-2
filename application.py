import copy
import constants
import clean_data

print(f'''\n\n\t____________________________________________
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~BASKETBALL TEAM STAT TOOL~~~~~~~~~|''')



def start_program():
    #Start up of the program.
    off_set = f'\b'* 34
    while True:
        try:
            prompt_1 = int(input(f"""\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~ OPTIONS ~~~~~~~~~~~~~~~~~~|
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |--1) Display Team Stats ------------------|
        |--2) Quit---------------------------------|
        |------------------------------------------|
        |--Please enter the number of the option---|
        |--you would like to execute.--------------|
        |------->   <------------------------------|{off_set}"""))
            if prompt_1 > 2 or prompt_1 <1:
                print(f'''\t|------------------------------------------|
        |--You failed to enter a valid number -----|
        |---Please try again ----------------------|''')
            elif prompt_1 == 1:
                clean_data.pick_team()
            elif prompt_1 == 2:
                print(f'''\t|------------------------------------------|
        |--Thank you, come again soon.-------------|
        |------------------------------------------|''')
                break
        except ValueError or NameError:
                print(f'''\t|------------------------------------------|
        |--You failed to enter a valid number -----|
        |---Please try again ----------------------|''')
                continue




















if __name__ == '__main__':
    start_program()
