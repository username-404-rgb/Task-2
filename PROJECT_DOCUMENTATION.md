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
    Data flow diagram / Story Boards
![Data Flow 0](images/dataflow0.png)
![Data Flow 0](images/dataflow1.png)
![Story Board 1](images/storyboard1.png)
![Story Board 2](images/storyboard2.png)
![Story Board 3](images/storyboard3.png)
![Story Board 4](images/storyboard4.png)
![Story Board 5](images/storyboard5.png)

## Build and Test
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