
def main():
    print('')
    print('Start Game ~ (1)')
    print('Make Card  ~ (2)')
    print('View Cards ~ (3)')
    print('Quit       ~ (4)')
    print('')
    print('Decend The Dungeon Depths, and Return With Pride')
    print('')
    input1 = input('?')
    if input1 == '1':
        print('')
        print('~Start Game~')
        print('Difficulty')
        print('(E)asy')
        print('(N)ormal')
        print('(H)ard')
        print('')
        print('(X) Back')
        print('')
        input2 = input('?').lower()
        if input2 == 'e':
            print('Easy Selected') # For Sprint 2
        elif input2 == 'n':
            print('Normal Selected') # For Sprint 2
        elif input2 == 'h':
            print('Hard Selected') # For Sprint 2
        elif input2 == 'x':
            main()
        else:
            print('Try again')
    elif input1 == '2':
        print('Card Maker')
    elif input1 == '3':
        print('View Cards')
    elif input1 != '4':
        print ('Error, Try Again')
        main()
    else:
        print('')
main()