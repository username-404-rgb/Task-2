
def main():
    print('')                   # Prints a main menu for the player
    print('Start Game ~ (1)')
    print('Make Card  ~ (2)')
    print('View Cards ~ (3)')
    print('Quit       ~ (4)')
    print('')
    print('Decend The Dungeon Depths, and Return With Pride')
    print('')
    input1 = input('?')         # Lets the player input a choice
    if input1 == '1':           # If they select 'Start Game', then allows them to chose difficulty
        print('')
        print('~Start Game~')
        print('Difficulty')
        print('(E)asy')
        print('(N)ormal')
        print('(H)ard')
        print('')
        print('(X) Back')
        print('')
        input2 = input('?').lower()     # Converts their input to lowercase for easier formatting of code
        if input2 == 'e':
            print('Easy Selected') # For Sprint 2
        elif input2 == 'n':
            print('Normal Selected') # For Sprint 2
        elif input2 == 'h':
            print('Hard Selected') # For Sprint 2
        elif input2 == 'x':
            main()
        else:
            print('Try again')          # If thier input isn't valid sends them back to the main menu, and lets them know they did something wrong
            main()
    elif input1 == '2':                 # If their input is 'Make Card', runs that function
        print('Card Maker') # For Sprint 2
    elif input1 == '3':                 # If their input is 'View Cards', runs that function
        print('View Cards') # For Sprint 2
    elif input1 != '4':                 # If their input isn't 'Quit', lets them know they did something wrong and runs main again
        print ('Error, Try Again')      
        main()
    else:                               # If their input is 'Quit', ends program
        print('')
main()