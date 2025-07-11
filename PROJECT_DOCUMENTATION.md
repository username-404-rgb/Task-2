# **Y11 Task 2 2025 - Card Game**

### Alexander Adams

# Sprint 1

## **Requirements Definition**
### Functional
* User can understand the menu
* Menu succesfully reads any user imput
* Game functions properly

### Non-Functional
* System runs quickly
* System always works
* System is easy to use

## **Determining Specifications**
### Functional
* User can end the program, enter any text
* System successfuly redirects from inputs
* Game functions
* System lets users know how to use it
* Minimal errors that are hard to encounter

### Non-Functional
* System is efficient
* Accessable to new users to understand
* Game is fun to play

## **Use Case**
  Actor: User (Player)

Preconditions: None

Main Flow:

* Start game - Allows user to start a game of easy, medium or hard difficulty
* Make a Card - Allows user to make a card and add it to the card pool
* View Cards - Allows user to look at a list of all cards and edit it
* Quit - System ends the program
* Other - System displays error message and allows user to input again

Postconditions: Game starts, Card is added to pool successfully, Pool is changed successfully, Program ends, Program still works

## Design
    Data flow diagram
![Data Flow 0](images/dataflow0.png)
![Data Flow 0](images/dataflow1.png)
    Story Boards
![Story Board 1](images/storyboard1.png)
![Story Board 2](images/storyboard2.png)
![Story Board 3](images/storyboard3.png)
![Story Board 4](images/storyboard4.png)
![Story Board 5](images/storyboard5.png)
    Gantt chart for the project
![Gantt Chart](images/Gantt_Chart.png)

## Build and Test
```py
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
```
## Review
    System meets all requirements set for sprint 1
    Performance is high, as it is currently a simple program and doesn't use many resources
    Code needs to be organised better for future sprints, and I need to catch up
    Should bring in function use for sprint two to make it easier to program


# Sprint 2

## Build and Test
    class Card:
        def __init__(self, name, suit, cost):
            self.name = name
            self.suit = suit
            self.cost = cost

## Review
    Need to restructure project for sake of making a functioinal one in the alloted time

# Sprint 3

## Design
![UML Class Diagram](images/UMLClassDiagram.png)

## Build and Test
```py
    #from Item_Class import * # Imports item class
    #from First_Area import * # Imports the first areas of the game
    import Item_Class as IC
    import First_Area as FA
    import Second_Area as SA

    #This paragraph is a list of various 'items' for the game
    lantern = IC.Item('lantern', 'false')
    has_been_start = IC.Item('started', 'false')     # Use of item class to store value of whether or not the player has been to the 'wake_up' area
    first_entered = IC.Item('entered', 'false')    # Has the player entered the mansion
    knife = IC.Item('knife', 'false')
    noise = 0                                       # Noise mechanic in the second area

    # Temporarily putting 'start_area' as a comment for easy testing of the second area

    #FA.start_area()   # Starts the game 
    #print('\n')
    SA.main_int() # Runs the second area, will change back to 'enter_mansion'
```

## Review

System could use optimisations in formatting, but should be sufficient in other requirements set.

Program reads inputs successfully, however I can't remove options from scenes, so I have settled for hiding the option, such that a player wouldn't know they can collect an item multiple times.

Code is difficult to read, but I am able to parse it well enough for the development of the program. Structure could use work as I don't have a direct system for organisation of code, leading to disorganised code blocks.

Improvment of code structure would be good, however I think I will just work on finishing the second area first.

# Sprint 3

## Design

### Potential Improvements
Actual locks on commands
Currently any options the player isn't meant to repeat, e.g. collecting an item, are hidden rather than actually prevented
I'll do this through checks within each command, rather than just in the scene descriptions

## Build and Test
An example of such code


    def left_path():
        lantern_check = lantern.get_collected()
        if lantern_check == 'false':                                            # If you grabbed the lantern...
            print('You go down the bright path, stopping at the lantern')
        else:                                                                   # Otherwise...
            print('The post where the lantern was hung from sits silent and still')
        print('Just infront of you stands an insurmountable boulder, too wide to go around')    # Either way...
        if lantern_check == 'false':                                            # If you grabbed the lantern...
            print('1 - Return the way you came, or\n'
                '2 - Grab the lantern')
        else:                                                                   # Otherwise...
            print('1 - Return the way you came')

    choice = int(input('Enter choice: '))
    if choice == 1:
        start_area()
    elif choice == 2:
        if lantern_check == 'true':            # Checks if the lantern has already been collected, and if it has, has unique dialouge
            print('The post is wedged too firmly in the ground to take')
            left_path()
        else:
            print('You grab the lantern, now realising how cold you are as your fingers begin to warm')
            lantern.set_collected('true')
            left_path()
    else:
        print('Enter a valid number, silly!')


## Review

The program meets the requirements I've set, excluding the reading of all inputs, as not inputing a number results in the program stopping.

It is not fair to compare my code against the use case previously described as the program has undergone a massive change in scope, making the former use case non functional

The code is relatively well organised, though some areas liikely could have been formatted better had I had a structure in mind from the begining.