from Item_Class import * 

lantern = Item('lantern', 'false')

#def check_inventory(searchingitem):
#    To Be Added


def wake_up():
    print('You wake up in a forest clearing, unsure of how you got here, ahead you see two paths\n'
         'The left path is brightly lit with a lantern, the right is pitch black\n'
         '1 - Proceed down the left path, or\n'
         '2 - Venture down the unknown right path \n')
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()
    else:
        print('Enter a valid number, silly!')

def left_path():
    print('\n'
          'You go down the bright path, stopping at the lantern\n'
          'Just infront of it stands an insurmountable boulder, towide to go around\n'
          '1 - Return the way you came, or\n'
          '2 - Grab the lantern')

    choice = int(input('Enter choice: '))
    if choice == 1:
        return_wake()
    elif choice == 2:
        lantern.set_collected('True')
    else:
        print('Enter a valid number, silly!')


def right_path():
    print('\n'
          'You take your chances in the darkness, and find a sign\n'
          'In the darkness you cannot read it, and you ignore it for now\n'
          'Continuing, you hear a low noise, far away right now, you wonder if you should\n'
          '1 - Continue forward with apprehension, or\n'
          '2 - Turn around, and venture down the other path\n')

    choice = int(input('Enter choice: '))
    if choice == 1:
        wolf_kill()
    elif choice == 2:
        return_wake()
    else:
        print('Enter a valid number, silly!')

def wolf_kill():
    print('\n'
          'You walk forwards, and you realise what the noise is, too late\n'
          'You try running back to the light but are just too slow\n'
          'You were eaten by wolves\n'
          '1 - Try again')

    choice = int(input('Enter choice: '))
    if choice == 1:
        wake_up()
    else:
        print('Enter a valid number, silly!')

def return_wake():
    print('\n'
         'You return to the clearing, the two paths still there\n'
         'The left path is brightly lit with a lantern, the right is pitch black\n'
         '1 - Proceed down the left path, or\n'
         '2 - Venture down the unknown right path \n')

    choice = int(input('Enter choice: '))
    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()
    else:
        print('Enter a valid number, silly!')



wake_up()