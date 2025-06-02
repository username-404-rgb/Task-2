from Item_Class import * # Imports item class
from Noise import *      # Imports the noise mechanic
import time # Allows for waits

# Items for this area
first_entered = Item('entered', 'false')    # Has the player entered the mansion
knife = Item('knife', 'false')


def enter_mansion():           
    print('You find yourself outside a dark mansion\n'
          'As you hear howling behind you the only thing you can think to do is\n'
            '1 - Go inside')
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        main_int()
    else:
        print('Enter a valid number, silly!')

def main_int():
    print('\n')
    entered_check = first_entered.get_collected()
    if entered_check == 'false':
        print ('As you step inside you heear the door slam behind you, and as you try to open it, you now find it locked\n'
               'You turn around, and try to get a handle on the surroundings')
    print('You only see four things of note around the dark interior\n'
          '1 - A doorway to what looks like a kitchen\n'
          '2 - A stairway to the second floor\n'
          '3 - A trapdoor in the floor\n'
          '4 - And a door leading under the stairs\n')
    first_entered.set_collected('true')   
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        kitchen()
    elif choice == 2:
        floor_two()
    elif choice == 3:
        trapdoor()
    elif choice == 4:
        stair_closet()
    else:
        print('Enter a valid number, silly!')

def kitchen():
    print ('Entering the kitchen you see rancid food strewn about the whole area, its digusting')
    knife_check = knife.get_collected()                                                                 # Checks if the knife is collected
    if knife_check == 'false':
          print('A knife is embedded in the side of a pile of cans, you consider picking it up')
    else:
          print('The cans now lay on the floor, one leaking an unidentifiable black sludge')
    print('Another hallway is now visible, though you cant tell where it leads\n'
          '1 - Go back to the main hall\n'
          '2 - Go down the next hallway')
    if knife_check == 'false':                                                                          # Hides the 'grab knife' option if it has already been picked up
          print ('3 - Grab the knife\n')
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        main_int()
    elif choice == 2:
        kitchen_hall()
    elif choice == 3:
        print('As you try to pry the knife from the can you accidentally knock down a pile of cans')
        noisy_action()                                                                                  # Adds one to 'noise'
        knife.set_collected('true')                                                                     # Sets the knife as collected
        print('\n')
        kitchen()                                                                                       # Plays the kitchen scene again
    else:
        print('Enter a valid number, silly!')

def kitchen_hall():
    print('You enter the hall, unable to see the end\n'
          'As you keep walking you see torn paintings covering the walls, you cant even tell what they were of\n'
          'After a while, you see something at the end, and you smell it too')
    time.sleep(7)
    kitchen()

def floor_two():
    pass

def trapdoor():
    print('You go up to the trapdoor, its locked\n'
           'It looks weak, you could probably lift it off even without the key')

def stair_closet():
    pass
