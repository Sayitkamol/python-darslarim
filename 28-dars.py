# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:45:08 2023

@author: Sayitkamol

28-dars: Object Oriented Programming

"""
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism.title()
        self.familiya = familiya.title()
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
        
    def get_lastname(self):
        return self.familiya
        
    def get_age(self,yil):
        return yil - self.tyil
        
    def tanishtir(self): 
        return f"Ismim {self.ism} {self.familiya}, tugilgan yilim {self.tyil} "


talaba1 = Talaba('olim','olimov',2000)
talaba2 = Talaba('hasan','aliyev',2004)
talaba3 = Talaba('akrom','husanov',1997)

""" Amaliyotlar """

class User():
    def __init__(self,ism,familiya,email,tel_nomer):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.tel_nomer = tel_nomer
        
    def get_fullname(self):
        return [self.ism.title(), self.familiya.title()]
        
    def get_info(self):
        return [f"Foydalanuvchi: {self.ism.title()} {self.familiya.title()}. "
                f"Elektron pochta manzili: {self.email}. Telefon raqami: {self.tel_nomer}"]
                
    
user1 = User('ali', 'valiyev','ali@email.com', +9985551998)