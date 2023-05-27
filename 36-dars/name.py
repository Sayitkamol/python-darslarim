# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:40:44 2023

@author: Sayitkamol

36-dars: FUNKSIYALARNI TEKSHIRISH
"""

def get_full_name(ism, familiya,otasi=""):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()









