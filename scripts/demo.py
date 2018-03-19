# Standard library
import os
from os import path
import sys

up_one_dir = path.abspath(path.join(os.getcwd(), '..'))
if 'scripts' not in os.listdir(up_one_dir):
    raise IOError('Script must be run from the scripts/ directory.')
sys.path.insert(0, path.join(up_one_dir))

from citationpep import citation


def string_input():
    """Imports the package and returns only the citation for that package"""
    citations = citation('astroML')
    print(citations)


def module_input():
    """Returns only the citation for that package"""
    import astroML
    citations = citation(astroML)
    print(citations)


def no_input():
    """Citations for all imported packages"""
    import astroML
    citations = citation()
    print(citations)


if __name__ == '__main__':
    choice = int(sys.argv[1])

    if choice == 1:
        string_input()

    elif choice == 2:
        module_input()

    elif choice == 3:
        no_input()
