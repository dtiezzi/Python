import os
class Terms:

    def __init__(self):
        self.terms = ''

    def createList(self):
        done = 'y'
        os.system('clear')

        print('''

##########################################################
############----------------------------------############
############      PUBMED - SEARCH ENGINE      ############
############----------------------------------############
##########################################################   
     
''')

        while done != 'n':
            t = input("Type the term: ").lower()
            done = input("Add another term? AND, OR, NOT (a/o/n): ").lower()
            if done == 'a':
                self.terms += t + ' [AND] ' 
            elif done == 'o':
                self.terms += t + ' [OR] '
            else:
                self.terms += t
