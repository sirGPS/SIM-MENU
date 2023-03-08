"""
USE 

import celin
in your project


Date 2022 11 26

Date 2023 03 08
Fix Variables Name to conform code
"""

def ver():
    """
    DOCSTRING HERE
    """
    display_version = 3

    print('AUTHOR  : sirGPS')
    print('DATETIME: 2022/11/26 1630 UTC+02')
    print('LOCATION: NICOSIA 2022')
    print('VERSION: f{display_version}')


def addline(x_line = 1):
    """
    Adds a new line or
    multilines
    """
    for x_line in range(x_line):
        print(chr(13)) # newline
        x_line = x_line + 1
    # v2 whitespace conform to code
    # v2 snake_case fix
def addspace(x_space = 1):
    """
    adds space or
    multispaces
    """
    for x_space in range(x_space):
        print(chr(32),sep = '',end = '' )
        x_space = x_space + 1
    # v2 whitespace conform to code
    # v2 snake_case fix
def addbar(x_bar = 1):
    """
    Adds a bar accross terminal
    v2
    """
    for x_bar in range(x_bar):
        print('=',sep = '',end = '')
        x_bar = x_bar + 1