
"""
OBJECTIVE = MAKE a simple nested menu



"""

import sys
import os
import subprocess

import celin


#bar_len = 10

def menu_alfa():
    """
    DOCSTRING HERE
    MENU ALFA CARD
    """
    celin.addline()
    celin.addline()
    print(' Alfa Menu ')
    celin.addline()

    celin.addline()
    # Draw Alfa menu
    print(' Q = MainMenu')
    print(' A = Say Alfa')
    # Deal User Input
    askuser = ' '
    askuser = input('-> ')
    askuser = askuser.lower()
    if askuser == 'q':
        main()
    if askuser == 'a':
        print(' ALFA')
    if askuser != ' ':
        menu_alfa()
def menu_beta():
    """
    MENU BETA
    """
    celin.addline()
    print(" BETA MENU")
    celin.addline()
    print(' Q = MAIN MENU')
    print(' A = PLACEHOLDER')
    print(' B = PLACEHOLDER')
    celin.addline()
    askuser = ' '
    askuser = input('->')
    askuser = askuser.lower()
    if askuser == 'q':
        mainmenu_card()
    if askuser != ' ':
        menu_beta()
    if askuser == 'a':
        print(' menu BETA ALFA PLACE holder')
    if askuser == 'b':
        print(' menu BETA BETA')
def mainmenu_card():
    """
    DOCSTRING HERE
    """
    celin.addline()
    print('MainMenu')
    celin.addline()
    #draw card
    celin.addline()
    print(' Q = Quit')
    print(' R = Restart\n')
    print(' A = Alfa Card')
    print(' B = Beta Card')
    celin.addline()
    #deal with user
    askuser = ' '
    askuser = input('-> ')
    askuser = askuser.lower() # go lowercase all input
    if askuser == 'q':
        print('Quiting...')
        sys.exit()
    if askuser == 'r':
        print('Restarting...')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    if askuser == 'a':
        menu_alfa()
    if askuser == 'b':
        menu_beta()
    if askuser != ' ':
        main()
    celin.addline()
    main()
def main():
    """
    DOCSTRING HERE
    """
    mainmenu_card()
main()
