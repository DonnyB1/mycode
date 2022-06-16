#!/usr/bin/env python3

"""PURPOSE OF THIS CODE | AUTHOR Contact Info"""

import crayons
def main():

    print(crayons.red('red string'))

    print(f"{crayons.red('Dirty')} white {crayons.blue('Mouth')}")  
    crayons.disable() 
    print(f"{crayons.red('Clean it up')} white {crayons.blue('With orbit gum')}")

    crayons.DISABLE_COLOR = False 

    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  
    print(crayons.red('red string', bold=True))

    print(crayons.yellow('yellow string', bold=True))

    print(crayons.magenta('magenta string', bold=True))

    print(crayons.white('white string', bold=True))

main()
