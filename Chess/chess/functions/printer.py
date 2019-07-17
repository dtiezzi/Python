import os

class Printer:

    def __init__(self):
        pass

    def printboard(p):
        os.system('clear')
        print('''
        #########################################
        ######################################### 
            ''')
        print('    ', end='')
        for i in range(8):
            print('  ', i, end=' ')
        print('\n')
        n= 0
        for l in range(65, 73):
            print('   ', chr(l), end='  ')
            for position in p.position[n]:
                print(position, end='   ')
            n+=1
            print('\n')
        print('''
        #########################################
        ######################################### 
        ''')

    def printxt(filename):
        os.system('clear')
        with open(filename, 'r') as txt:
            f = txt.read()
            print(f)