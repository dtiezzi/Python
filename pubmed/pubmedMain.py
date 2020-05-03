from pubmedSearch import Pubmed
from termList import Terms
import datetime

date = datetime.date.today().strftime("%Y_%m_%d")

op = 1
while op:
    termList = Terms()
    termList.createList()

    res = input('''
Searching for the following terms:
{0}
Is it correctm (y/n)?    
    '''.format(termList.terms)).lower()

    op = 0 if res == 'y' else 1

nret = int(input("Type the maximun number of results to return: "))

result = Pubmed(termList.terms, nret, 'dt@usp')

result.readNcbi()

with open("Myrecords_" +  date + '.txt', 'a+') as file:
    n = 1
    for record in result.records:
        file.write("File #" + str(n) + '\n')
        ti = record.get("TI", "?")
        ti = "title:" + ti + '\n'
        file.write(ti)
        au = record.get("AU", "?")
        au = "authors:" + str(au) + '\n'
        file.write(au)
        so = record.get("SO", "?")
        so = "source:" + so + '\n'
        file.write(so)
        ab = record.get("AB", "?")
        ab = "abstract:" + ab + '\n'
        file.write(ab)
        file.write('\n\n')
        n+=1
        
        
        
        
