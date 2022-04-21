# Joe Nyhan, 21 April 2022
# Creates a new hw assignment in the specified path

from os import system as sh
from os.path import isdir

def main():

    while True:
        num = input('Input a number (#) for the homework assingment to create: ')

        try:
            num = int(num)
        except ValueError:
            print('Not an integer; try again!')
            continue


        if isdir(f'./hw{num}/'):
            print('This assignment already exists! Try again.')
        else:
            break
    
    path = f'./hw{num}'
    sh(f'mkdir {path}/')
    sh(f'cp ./template/body.tex {path}/')
    sh(f'cp ./template/main.tex {path}/')


if __name__ == '__main__':
    main()