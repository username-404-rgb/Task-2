from Item_Class import * # Imports item class
import time

#This paragraph is a list of various 'items' for the first area
lantern = Item('lantern', False)
has_been_start = Item('started', False)     # Use of item class to store value of whether or not the player has been to the 'wake_up' area

def start_area():  #The initial area, 
    print('\n')
    started_check = has_been_start.get_collected()
    if started_check == False:             
        print('You wake up in a forest clearing, unsure of how you got here, ahead you see two paths')  # (S) If the player has NOT been here before...
    else:                                   
        print('You return to the clearing, the two paths still there')                                  # (S) If the player HAS been here before...        
    lantern_check = lantern.get_collected()                                                             # (S) EITHERWAY... 
    if lantern_check == False: 
        print('The left path is brightly lit with a lantern, the right is pitch black')                 # (L) If the lantern hasn't been collected...
    else:
        print('The left path is now as silent as the right')                                            # (L) If the lantern has been collected...
    print('1 - Proceed down the left path, or\n'                                                        # (L) EITHERWAY...
            '2 - Venture down the right path')
    has_been_start.set_collected(True)                                                                        # (S) Sets the value for if the player has been here before to true
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()
    else:
        print('Enter a valid number, silly!')

def left_path():
    lantern_check = lantern.get_collected()
    if lantern_check == False:                                            # If you grabbed the lantern...
        print('You go down the bright path, stopping at the lantern')
    else:                                                                   # Otherwise...
        print('The post where the lantern was hung from sits silent and still')
    print('Just infront of you stands an insurmountable boulder, too wide to go around')    # Either way...
    if lantern_check == False:                                            # If you grabbed the lantern...
        print('1 - Return the way you came, or\n'
              '2 - Grab the lantern')
    else:                                                                   # Otherwise...
        print('1 - Return the way you came')

    choice = int(input('Enter choice: '))
    if choice == 1:
        start_area()
    elif choice == 2:
        if lantern_check == True:            # Checks if the lantern has already been collected, and if it has, has unique dialouge
            print('The post is wedged too firmly in the ground to take')
            left_path()
        else:
            print('You grab the lantern, now realising how cold you are as your fingers begin to warm')
            lantern.set_collected(True)
            left_path()
    else:
        print('Enter a valid number, silly!')


def right_path():
    print('\n'
          'You take your chances in the darkness, and find a sign')
    lantern_check = lantern.get_collected()
    if lantern_check == False:
          print('In the darkness you cannot read it, and you ignore it for now')
    else:
          print('You hold up the lantern to the sign, "They avoid the light", it warns')          
    print('Continuing, you hear a low noise, far away right now, you wonder if you should\n'
          '1 - Continue forward with apprehension, or\n'
          '2 - Turn around, and venture down the other path\n')

    choice = int(input('Enter choice: '))
    if choice == 1:
        if lantern_check == False:
            wolf_kill()
        else:
           leaving_first_areas()
    elif choice == 2:
        start_area()
    else:
        print('Enter a valid number, silly!')

def wolf_kill():
    print('\n'
          'You walk forwards, and you realise what the noise is, too late')
    time.sleep(2)
    print('You try running back to the light but are just too slow')
    time.sleep(2)
    print('You were swallowed whole in the darkness')
    time.sleep(2)
    print('1 - Try again')

    choice = int(input('Enter choice: '))
    if choice == 1:
        start_area()
    else:
        print('Enter a valid number, silly!')

def leaving_first_areas():
    print('\n'
          'You start down the path careful not to let the lantern blow out\n')
    time.sleep(2)
    print('As you look to the tree line, you see them, staring at you, waiting for your flame to die')
    time.sleep(2)
    print('And as it does, you run as fast as you can, dropping the lantern')
    time.sleep(2)
    print('As you run into a lit area, you look back to see them running back to the forest')
    time.sleep(2)
    print('You barely survived this encounter')
    time.sleep(2)