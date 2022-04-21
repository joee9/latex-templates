
# Joe Nyhan, 18 April 2022
# Providing a path update main.tex,body.tex,.gitignore, in an already initialized repository.

from os import system as sh
from os.path import isdir
from init import write_gitignore_hw

def update_hw(path):
    print(f'Update template in this directory? [y,n]: {path}')

    while True:
        s = input('-> ')
        if s in ['Y','y']:
            print('Updating!')
            break
        elif s in ['N','n']:
            print('Choosing a new path...')
            return False
        else:
            print('Invalid input! Try again.')

    sh(f'cp body.tex {path}/hw/template/')
    sh(f'cp main.tex {path}/hw/template/')
    sh(f'cp ../../.gitignore {path}')
    sh(f'cp dist_main.py {path}/hw/')
    sh(f'cp mkhw.py {path}/hw/')

    write_gitignore_hw(path)

    print('Updated!')
    
    return True


def main():

    while True:
        path = input("Please input an (absolute) path to directory to update: ")

        if not isdir(path):
            print(f'Invalid path! {path} does not exist. Try again.')
            continue

        else:
            if update_hw(path):
                break
            else:
                continue


if __name__ == '__main__':
    main()