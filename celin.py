"""
USE 

import celin
in your project


Date 2022 11 26

"""

def ver():
    """
    DOCSTRING HERE
    """

    print('AUTHOR  : sirGPS')
    print('DATETIME: 2022/11/26 1630 UTC+02')
    print('LOCATION: NICOSIA 2022')


def addline(x = 1):
    """
    Adds a new line or
    multilines
    """
    for x in range(x):
        print(chr(13)) # newline
        x = x + 1
          
def addspace(x = 1):
    """
    adds space or
    multispaces
    """
    for x in range(x):
        print(chr(32),sep = '',end = '' )
        x = x + 1