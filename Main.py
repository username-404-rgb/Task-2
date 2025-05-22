def left_path():
    print('You go down the bright path')

def right_path():
    print('You take your chances in the darkness, and find a sign\n'
          'In the darkness you cannot read it, and you ignore it for now\n'
          'Continuing, you hear a low noise, far away right now, you wonder if you should\n'
          '1 - Continue forward with apprehension, or\n'
          '2 - Turn around, and venture down the other path\n')


def main():
    print('You wake up in a forest clearing, unsure of how you got here, ahead you see two paths\n'
         'The left path is brightly lit with a lantern, the right is pitch black\n'
         '1 - Proceed down the left path, or\n'
         '2 - Venture down the unknown right path \n')

    choice = int(input('Enter choice: '))
    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()
    elif choice == 9:
        print('Game Over')
    else:
        print('Enter a valid number, silly!')

main()