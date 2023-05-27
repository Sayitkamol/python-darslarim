# -*- coding: utf-8 -*-
"""
Created on Fri May  5 01:30:05 2023

@author: Sayitkamol

21-dars: FUNKSIYA VA RO'YXAT

"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

""" Amaliyot """

def katta_harf(ismlar):
    ismlar = ismlar[:]
    for ism in range(len(ismlar)):
        ismlar[ism] = ismlar[ism].title()
    return ismlar

    
    # ismlar0 = []
    # for ism in ismlar:
    #     ism = f"{ism.title()}"
    #     ismlar0.append(ism)
    # return ismlar0

ismlar = ['ali', 'vali', 'hasan', 'husan']
print(ismlar)
print(katta_harf(ismlar))

def bahola2(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar
    
    

baholar = bahola(talabalar[:])
baholar = katta_harf(baholar)
print(baholar)
# print(talabalar)





