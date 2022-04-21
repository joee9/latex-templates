# Joe Nyhan, 18 April 2022
# Providing a path will initialize a repository for homework

from os import system as sh
from os.path import isdir

def write_gitignore_hw(path):
    with open(f'{path}/.gitignore', 'a') as f:
        f.write('\nmain.tex\n')
        f.write('!hw/template/main.tex\n')

def init_hw(path):
    print(f'Create HW in this directory? [y,n]: {path}')

    while True:
        s = input('-> ')
        if s in ['Y','y']:
            print('Creating template!')
            break
        elif s in ['N','n']:
            print('Choosing a new path...')
            return False
        else:
            print('Invalid input! Try again.')

    sh(f'mkdir {path}/hw/')
    sh(f'mkdir {path}/hw/template/')
    sh(f'cp body.tex {path}/hw/template/')
    sh(f'cp main.tex {path}/hw/template/')
    sh(f'cp mkhw.py {path}/hw/')
    sh(f'cp dist_main.py {path}/hw/')
    sh(f'cp ../globals.tex {path}/')
    sh(f'cp ../../.gitignore {path}')


    write_gitignore_hw(path)

    print('Created!')
    
    return True


def main():

    print('\nLaTeX Homework Template! by Joe Nyhan, 2022')

    while True:
        path = input("Please input an (absolute) path to directory to initialize: ")

        if not isdir(path):

            while True:
                print(f'Path "{path}" does not exist. Create it? [y/n]', end=' ')
                s = input(': ')
                if s in ['Y','y']:
                    sh(f'mkdir {path}')
                    init_hw(path)
                    break
                elif s in ['N','n']:
                    print('Exiting, as path is not valid.')
                    exit()
                else:
                    print('Invalid input! Try again.')
            
            break

        else:
            if init_hw(path):
                break
            else:
                continue


if __name__ == '__main__':
    main()