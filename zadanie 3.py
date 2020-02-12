# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:52:35 2019

@author: Piotr
"""

class Ocena():
    
    def __init__(self, wartosc, waga = 1):
        self.wartosc=wartosc
        self.waga=waga
        
    def __add__(self, x):
        return Ocena((self.wartosc+x.wartosc)/2, (self.waga+x.waga)/2)
    def __str__(self):
        return (str(self.wartosc) + "(" + str(self.waga)+")")
    
    def __iadd__(self,x):
        self.wartosc+=x
        self.waga+=x
        return self
    

class Grupa():
    
    def __init__(self, ls):
        self.oceny=[]
        self.liczba_studentow=ls
        
    def wpiszocene(self, ocena):
        if len(self.oceny)<self.liczba_studentow:
            self.oceny.append(ocena)
            
    def pisz(self):
        for i in self.oceny:
            print(i)
        print(Grupa.oblicz_srednia(self))
            
    def oblicz_srednia(self):
        suma=0
        suma_wag=0
        for i in self.oceny:
            wartosc =i.wartosc*i.waga
            suma+=wartosc
            suma_wag+=i.waga
        return suma/suma_wag
    
    def zmien_ocene(self, id, ocena):
        if id>len(self.oceny):
            print("nie ma oceny o takim id")
        else:
            self.oceny[id-1].wartosc=ocena.wartosc
            self.oceny[id-1].waga=ocena.waga
        
        
    def zamkniety_semestr(self):
        for i in self.oceny:
            if i.wartosc<2 or len(self.oceny)!=self.liczba_studentow:
                return False
            else:
                return True
    
    def __add__(self, x):
        grup=Grupa()
        grup.oceny=self.oceny+self.x
        grup.liczba_studentow=self.liczba_studentow+x.liczba_studentow
        return grup

g = Grupa(2)
g.wpiszocene(Ocena(2,2))
g.wpiszocene(Ocena(22,1))
g.pisz()
g.zmien_ocene(2,Ocena(3,4))
g.pisz()

g2=Grupa(3)
g2.wpiszocene(Ocena(4,8))
g2.wpiszocene(Ocena(5,2))

print((g+g2).liczba_studentow)

        
    
