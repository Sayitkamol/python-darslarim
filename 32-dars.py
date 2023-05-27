# -*- coding: utf-8 -*-
"""
Created on Mon May 22 02:56:34 2023

@author: Sayitkamol

32-dars: DUNDER METODLAR
"""

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
        
    def __str__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self,y):         # Obyektlarni tengligini ko'rsatuvchi metod
        return self.narh == y.narh
    
    def __lt__(self,y):         # Obyektlarni kichikligini ko'rsatuvchi metod  
        return self.narh < y.narh
    
    def __le__(self,y):         # Obyektlarni kichik yoki tengligini ko'rsatuvchi etod
        return self.narh <= y.narh
    

    


class AvtoSalon:
    """Avto Salon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index] = qiymat
        
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} va {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y,Avto):
            self.add_avto(y)
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")
        
        
    
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu",'Qora', 2020,40000)
avto2 = Avto("GM",'Lacetti','Qizil',2020,20000)
avto3 = Avto('KIA','sonata','oq',2022,45000)

salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto('Mazda','6','Oq',2018,35000)
avto5 = Avto('Volkswager','Polo','Qora',2015,30000)
avto6 = Avto('Honda','Accord','Qizil',2017,42000)

salon2(avto4,avto5,avto6)

















