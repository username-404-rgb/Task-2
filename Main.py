import time # Allows for waits
import Item_Class as IC # Import Item class
import First_Area as FA # Import First area
import Second_Area as SA# Import Second area
from Noise import *
#This paragraph is a list of various 'items' for the game
lantern = IC.Item('lantern', 'false')
has_been_start = IC.Item('started', 'false')     # Use of item class to store value of whether or not the player has been to the 'wake_up' area
first_entered = IC.Item('entered', 'false')    # Has the player entered the mansion
knife = IC.Item('knife', 'false')
noise = 0                                       # Noise mechanic in the second area

# Temporarily putting 'start_area' as a comment for easy testing of the second area

FA.start_area()   # Starts the game 
time.sleep(7)
SA.main_int() # Runs the second area, will change back to 'enter_mansion'