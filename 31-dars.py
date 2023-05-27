# -*- coding: utf-8 -*-
"""
Created on Mon May 22 01:24:10 2023

@author: Sayitkamol

31-dars: INKAPSULYATSIYA VA KLASSGA OID XUSUSUYATLAR VA METODLAR
"""

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self._id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashina km ga km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km ni kamaytirib bo'lmaydi!")
    
avto1 = Avto("GM",'Malibu','qora',2022,40000,1000)
