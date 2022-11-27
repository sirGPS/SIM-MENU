
"""
OBJECTIVE = MAKE a simple nested menu



"""

import sys
import os
import subprocess

import celin


def MenuAlfa():
    """
    DOCSTRING HERE
    MENU ALFA CARD
    """
    
    celin.addline()
    print('Alfa Menu')
    celin.addline()
    # Draw Alfa menu

    print('Q =MainMenu')
    print('A =Say Alfa')

    # Deal User Input

    askuser = ' '
    askuser = input('-> ')
    askuser = askuser.lower()

    if askuser == 'q':
        main()
    if askuser == 'a':
        MenuAlfa()
    
        

def mainmenucard():
    """
    DOCSTRING HERE
    """
    celin.addline()
    print('MainMenu')
    celin.addline()
    #draw card
    
    print('Q = Quit')
    print('R = Restart\n')
    
    print('A = Alfa Card')
    print('B = Beta Card')

    #deal with user

    askuser = ' '
    askuser = input('-> ')
    askuser = askuser.lower()

    if askuser == 'q':
        print('Quiting...')
        sys.exit()
    if askuser == 'r':
        print('Restarting...')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    if askuser == 'a':
        print('Alfa placeholder')
    if askuser == 'b':
        print('Beta placeholder')
    if askuser != ' ':
        main()
        

    celin.addline()

    main()

def main():
    """
    DOCSTRING HERE
    """

    mainmenucard()

main()
