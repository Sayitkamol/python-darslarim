# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:45:08 2023

@author: Sayitkamol

29-dars: OBYEKTLAR BILAN ISHLASH

"""
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism.title()
        self.familiya = familiya.title()
        self.tyil = tyil
        self.bosqich = 1
        
    def get_name(self):
        return self.ism
        
    def get_lastname(self):
        return self.familiya
        
    def get_age(self,yil):
        return yil - self.tyil
        
    def fullname(self):
        return f"Ismim {self.ism} {self.familiya}, tugilgan yilim {self.tyil} "

    def set_bosqich(self,yangi_bosqich):
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

talaba1 = Talaba('olim','olimov',2000)
talaba2 = Talaba('hasan','aliyev',2004)
talaba3 = Talaba('akrom','husanov',1997)


class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_info() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni

def see_methods(klass):
    return [method for method in dir(klass) if method.startswth('__') is False]

matem = Fan("Oliy matematika")
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)


""" Amaliyotlar """

class Avto():
    def __init__(self,model,rang,korobka,narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0
        
    def get_info(self):
        return f"{self.rang} {self.model}, {self.korobka} korobka, narhi: {self.narh}"
    
    def update_km(self,km):
        return self.kilometr(km)
    
    
avto1 = Avto('Malibu','qizil','avtomat',30000)
avto2 = Avto('Nexia 3','qora','mexanik',10000)
    
    

class Avtosalon():
    def __init__(self,nomi,manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtolar = []
        self.avtolar_soni = 0
    
    def add_avto(self,avto):
        self.avtolar.append(avto)
        self.avtolar_soni += 1
    
    def get_info(self):
        print(f"{self.nomi} avtosalonidagi avtomobillar ro'yxati:")
        return [avto.get_info() for avto in self.avtolar]
    
salon1 = Avtosalon('Jahon','andijon')
salon1.add_avto(avto1)
salon1.add_avto(avto2)
    
    
    
    
    
    
    
    
    
    
    
    
    