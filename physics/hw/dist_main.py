# Joe Nyhan, 21 April 2022
# Updates main files within hw directory from the template file

from os import listdir
from os import system as sh
from os.path import isfile


def main():
    dirs = [f for f in listdir('.') if not isfile(f'./{f}') and f != 'template']

    for dir in dirs:
        sh(f'cp ./template/main.tex ./{dir}/')
    
    

if __name__ == '__main__':
    main()