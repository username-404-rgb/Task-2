from Item_Class import * # Imports item class
from Noise import *      # Imports the noise mechanic
import time # Allows for waits

#    elif choice == 5:
#        main_int()

# Items for this area
first_entered = Item('entered', False)    # Has the player entered the mansion
knife = Item('knife', False)
base_key = Item('key', False)
trap_opened = Item('Trap Door', False)
mousetrap = Item('Mouse Trap', False)
f2 = Item('Has been to second floor', False)

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
    entered_check = first_entered.get_collected() # If the player has not been here before...
    if entered_check == False:
        print ('As you step inside you hear the door slam behind you, and as you try to open it, you now find it locked\n'
               'You turn around, and try to get a handle on the surroundings') 
    print('You only see four things of note around the dark interior\n'
          '1 - A doorway to what looks like a kitchen\n'
          '2 - A stairway to the second floor\n'
          '3 - A trapdoor in the floor\n'
          '4 - And a door leading under the stairs\n')
    first_entered.set_collected(True)   
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        kitchen()
    elif choice == 2:
        floor_check = f2.get_collected()
        if floor_check == True:
            print("You won't return")
            main_int()
        else:
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
    if knife_check == False:
          print('A knife is embedded in the side of a pile of cans, you consider picking it up')
    else:
          print('The cans now lay on the floor, one leaking an unidentifiable black sludge')
    print('Another hallway is now visible, though you cant tell where it leads\n'
          '1 - Go back to the main hall\n'
          '2 - Go down the next hallway')
    if knife_check == False:                                                                          # Hides the 'grab knife' option if it has already been picked up
          print ('3 - Grab the knife\n')
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        main_int()
    elif choice == 2:
        kitchen_hall()
    elif choice == 3:
        if knife_check == True:                                                                         # Checks if the knife is collected
             print('The cans now sit on the floor, you can see no reason to touch them')
             kitchen()
        else:
            print('As you try to pry the knife from the can you accidentally knock down a pile of cans')
            noisy_action()                                                                                  # Adds one to 'noise'
            knife.set_collected(True)                                                                     # Sets the knife as collected
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
    print('You stand at the bottom of the stairs, looking up at a closed door\n'
          'As you take the first step, a loud creak is made')
    noisy_action()
    time.sleep(3)
    print('You now look up and see the door is opened\n'
          'You decide to go back to the lobby and not risk the climb')
    time.sleep(3)
    f2.set_collected(True)
    main_int()

def trapdoor():
    print('You go up to the trapdoor, made of a dark oak')
    trap_check = trap_opened.get_collected()
    if trap_check == True:
        print('It looks weak, you could probably lift it off even without the key')
    print('1 - Return to the main room\n')
    trap_check = trap_opened.get_collected()
    if trap_check == False:
        print('2 - Tear it off its hinges')
    key_check = base_key.get_collected()
    if key_check == True:
            trap_check = trap_opened.get_collected()
            if trap_check == False:
                print('3 - Unlock the door\n')
    trap_check = trap_opened.get_collected()
    if trap_check == True:
        print('4 - Go down')

    choice = int(input('Enter choice: '))
    if choice == 1:
        main_int()
    elif choice == 2:
        if trap_check == True:
            print('The door must have been rotted through, its beed torn to pieces by your action')
            trapdoor()
        else:
            print('You place your hands on the handle, and prepare to rip it off\n'
                'As you pull you realise its much weaker than you thought and fall over as it gives out')
            noisy_action()
            print('You get back for a look at the trapdoor')
            trap_opened.set_collected(True)
            trapdoor()

    elif choice == 3:
        if trap_check == True:
            print('The door is already opened')
            trapdoor()
        else:
            print('You take the key up to the lock, and slowly turn it\n'
                  'You open the door.')
            trap_opened.set_collected(True)
            trapdoor()

    elif choice == 4:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        print('Enter a valid number, silly!')


def stair_closet():
    print('You open the door, and struggle to see for a second as you adjust to the dark')
    check_mousetrap = mousetrap.get_collected()
    if check_mousetrap == False: 
        print('You spot something, hiding on the floor of the cuboard')
    else:
        print("The mousetrap sits on the floor, you notice there wasn't even cheese in it")
    key_check = base_key.get_collected()
    if key_check == False:
        print('On the shelves you see somthing shiny, hidden behind a shorth book pile')
    else:
        print('The books are all covered in dust, too hard to read their covers')
    print('1 - Return to the main room')
    if check_mousetrap == False: 
        print('2 - Collect the item on the floor')
    if key_check == False:
        print('3 - Collect the item on the shelves')

    choice = int(input('Enter choice: '))
    if choice == 1:
        main_int()
    elif choice == 2:
        if check_mousetrap == True:
            print('Your finger still hurts, and you see no reason to keep the trap')
        else:
            print('As you lean down, you reach for the item on the floor then...')
            time.sleep(2)
            print('Your finger is caught in a mousetrap')
            noisy_action()
            mousetrap.set_collected(True) 
            stair_closet()
    elif choice == 3:
        if key_check == True:
            print('Strangely, the books are glued together')
        else:
            print('You grab and see that it is infact, a key')
            base_key.set_collected(True)
            stair_closet()

    else:
        print('Enter a valid number, silly!')

main_int()