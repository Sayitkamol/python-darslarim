# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:02:10 2023

@author: User
"""

class Shaxs:
    """Shaxs haqida"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism.title()} {self.familiya.title()}. "
        info += f"Passport raqami {self.passport}, {self.tyil}-yilda tygilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshi haqida ma'lumot"""
        return yil - self.tyil
    
    def __repr__(self):
        return f"{self.ism.title()} {self.familiya.title()}"
    
odam1 = Shaxs('ali','valiyev','AB2342334',2000)
    
class Talaba(Shaxs):
    """Talaba haqida"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,bosqich):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = bosqich
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism.title()} {self.familiya.title()}. "
        info += f"ID raqami: {self.idraqam}, {self.tyil}-yilda tugilgan."
        info += f"{self.bosqich}-bosqich talabasi."
        
    def get_id(self):
        return self.idraqam
        
    def __repr__(self):
        return f"{self.ism.title()} {self.familiya.title()}"
    
    def __lt__(self,y):
        return self.bosqich < y.bosqich
    
    def __eq__(self,y):
        return self.bosqich == y.bosqich
    
    
talaba1 = Talaba('vali','aliyev','AB1234545',1992,'N0000102',bosqich=4)    
talaba2 = Talaba('hasan','husanov','AB3213132',1997,'N0000156',bosqich=2)    
talaba3 = Talaba('Qodir','Mamajanov','AB0252558',1990,'N0001212',bosqich=3)    
talaba4 = Talaba('akmal','sobirov','AB0225588',2000,'N0000321',bosqich=1)    



class Fan:
    def __init__(self,name):
        self.name = name
        self.talabalar = []
        
    def add_student(self,*talaba):
        for t in talaba:
            if isinstance(t,Talaba):
                self.talabalar.append(t)
            else:
                print("Iltimos talaba kiriting")
        
    
    
    
    
