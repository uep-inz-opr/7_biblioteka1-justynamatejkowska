class Library:
    def __init__(self):
        self.ksiazki = []
        self.egzemplarze=[]
        self.tytuly=[]       

    def addKsiazka(self, ksiazka): 
        self.ksiazki.append(ksiazka)#wrzuca książkę do listy

    def addEgzemplarz(self,egzemplarz): #dodanie egzamplarza bądz nowej ksiązki
        egzemplarz1 = list(egzemplarz)
        if egzemplarz1[1:3] in self.ksiazki:
            self.egzemplarze.append(egzemplarz1[1:3])
            self.tytuly.append(egzemplarz1[1])  
        else:
            library.addKsiazka(egzemplarz1[1:3])
            self.egzemplarze.append(egzemplarz1[1:3])
            self.tytuly.append(egzemplarz1[1])
                 
    def liczenie(self):
        listafinal=[]
        listasort=[]
        for ksiazka in self.ksiazki:
            a = self.egzemplarze.count(ksiazka)
            ksiazka = [ksiazka[0], ksiazka[1], a]
        listafinal.append(ksiazka)
        listasort = sorted(listafinal, key=lambda x: x[0])
        for element in listasort:
            element1 = (element[0], element[1], element[2])
        print(element1)