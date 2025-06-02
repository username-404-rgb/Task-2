import time # Allows for waits
import Second_Area as SA

noise = 0                                   # Serves as a noise mechanic, if it's too high, kills the player

def noisy_action():
    global noise
    noise = noise + 1
    if noise == 1:
        first_noise()
    if noise >= 3:
        too_loud()

def first_noise():                                                                                  # When noise is one
    time.sleep(2)                                                                                   # Wait 2 seconds, for suspense
    print('You hear a noise from elsewhere in the house, you are not alone')
    time.sleep(2)

def too_loud():                                                                                     #If noise goes above three
    print('Suddenly, you feel claws on your neck, lifting you far above the ground\n'
          'You reach for anything in your pockets, but cant reach anything right now\n'
          'As your vision darkens you hear a sickening snap\n'
          'You were killed\n'
          '1 - Try again')
    
    choice = int(input('Enter choice: '))
    if choice == 1:
        SA.main_int()
    else:
        print('Enter a valid number, silly!')