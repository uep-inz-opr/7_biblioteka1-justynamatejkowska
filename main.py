class Library:
    def __init__(self):
        self.ksiazki = []
        self.egzemplarze=[]
        self.tytuly=[]       

    def addKsiazka(self, ksiazka): 
        self.ksiazki.append(ksiazka)

    def addEgzemplarz(self,egzemplarz): 
        egzemplarz1 = list(egzemplarz)
        if egzemplarz1[0:2] in self.ksiazki:
            self.egzemplarze.append(egzemplarz1[0:2])
            self.tytuly.append(egzemplarz1[0])  
        else:
            library.addKsiazka(egzemplarz1[0:2])
            self.egzemplarze.append(egzemplarz1[0:2])
            self.tytuly.append(egzemplarz1[0])
                 
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

library=Library()
k = int(input())
for i in range(0, k):
    wejscie = eval(input())
    library.addEgzemplarz(wejscie)

library.liczenie()