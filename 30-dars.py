# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:25:36 2023

@author: Sayitkamol

30-dars: Vorislik va Polimorfizm
"""

class Shaxs :
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}"
        info += f"Passport:{self.passport}, {self.tyil}-yilda tugilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
inson = Shaxs("Hasan","Husanov","AB122312",2001)
    
class Talaba(Shaxs):
    """Talaba classi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususuiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.bosqich}-bosqich.ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self,fan):
        """Fanga yozilgan talabalar"""
        self.fanlar.append(fan)
        
    def fanlar(self):
        
        return sorted(self.fanlar())
    

class Manzil:
    """Manzilni saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

class Fan:
    """Fanlar"""
    def __init__(self,fan):
        """Fanalar qoshish"""
        self.fan = fan
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
    
    def get_info(self):
        return [x.get_info() for x in self.talabalar]    

talaba1_manzil = Manzil(12,"Olmazor","Bog'bon","Samarqand")
# talaba2 = Talaba('hasan','aliyev',2004)
# talaba3 = Talaba('akrom','husanov',1997)

talaba1 = Talaba("Valijon",'Aliyev','FA2213322',2000,'N00000032',talaba1_manzil)
matem = Fan('Oliy matelmatika')    
talaba1.fanga_yozil(matem)

    
    
    
    
    
    
    
    
    
    
    
    
    
    