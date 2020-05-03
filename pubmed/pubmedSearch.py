import os, ssl, sys
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from Bio import Entrez
from Bio import Medline

class Pubmed:

    def __init__(self, term, retmax, email):
        self.email = email
        self.term = term
        self.retmax = retmax
        self.records = []

    def readNcbi(self):
        Entrez.email = self.email
        handle = Entrez.esearch(db='pubmed',
                                sort='date', 
                                retmax=self.retmax,
                                retmode='text', 
                                term=self.term)
        results = Entrez.read(handle)
        id_list = results['IdList']
        handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline",retmode="text")
        records = Medline.parse(handle)
        self.records = list(records)
                