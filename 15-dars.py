# -*- coding: utf-8 -*-
"""
Created on Tue May  2 01:07:01 2023

@author: Sayitkamol
15-dars: Lug'atlar bilan ishlash
    
"""

talaba_0 = {
        'ism': 'Alijon',
        "familiya": 'Valijonov',
        'yosh':22,
        'fakultet':'informatika',
        'kurs': 4
    }
# print(talaba_0.items())

for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")


telefonlar = {
    'ali': "iphone x",
    'vali':'samsung s9',
    'hasan':'mi 10 pro',
    'husan':'note 10'
    }

for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

mahsulotlar = {
    'olma':10000,
    'nok': 25000,
    'behi': 12000,
    "o\'rik": 20000,
    'uzum': 18000
    }

print("Do'kondagi mahsulotlar:")

for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor','uzum','non','olma']
for n in mahsulotlar:
    if n in bozorlik:
        print(f"{n.title()} {mahsulotlar[n]} so'm")

for n in bozorlik:        
    if n not in mahsulotlar:
        print(f"Iltimos do'koningizga {n}ni ham olib keling")


print("Do'kondagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar.keys()):
    print(mahsulot.title())

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in sorted(telefonlar.values()):
    print(tel)
    
# #.set() metodida mahsulotlar takrorlanmaydi
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in set(telefonlar.values()):
    print(tel)


""" Amaliyot """

''' 1 '''

lugat = {
    'boolean': 'True va False mantiqiy qiymatlar uchun',
    'int':'butun sonlar uchun',
    'float': 'haqiqiy sonlar uchun',
    'complex': 'komplex sonlar uchun',
    'str':'matnlar uchun',
    'list':"ro'yxat",
    'tuple':'kortej',
    'dictionary':'lugat',
    'set':"to'plam"
    }

for k, q in sorted(lugat.items()):
    print(f"{k.title()} - {q}")
    
''' 2 '''

poytaxtlar = {
    'uzbekistan':'tashkent',
    'turkiya':'anqara',
    'iroq':"bog'dod",
    "qirg'iziston":'bishkek',
    'tojikiston':'dushanbe',
    'indoneziya':'jakarta',
    'pokiston':'islomobod',
    'afgoniston': 'qobul',
    'aqsh': 'washington'
    }

print("Dunyo davlatlari:")
for p in sorted(poytaxtlar):
    print(p.upper())

print("\nDavlatlarning poytaxtlari:")
for p in sorted(poytaxtlar.values()):
    print(p.title())

''' 3 '''

davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz?\n>>>").lower()
d = poytaxtlar.get(davlat)

if d == None:        
    print("Kechirasiz, bizda bu haqida malumot yo'q")
else:        
    print(f"{davlat.upper()} ning poytaxti {d.title()}")

''' 4 '''

menu = {
        'osh':10000,
        'mastava':8000,
        'chuchvara':10000,
        'somsa':5000,
        'shashlik':5000,
        'non':2500,
        'shorva':9000,
        'beshtext':12000,
        'grichka':11000,
        'choy':2000
        }

print("3 ta ovqat buyurtma berishingiz mumkin!")
zakaz = []

for n in range(3):
    zakaz.append(input(f"{n+1}-ovqat:").lower())

for ovqat in zakaz:
    if ovqat in menu:
        print(f"{ovqat} narxi {menu[ovqat]} so'm")
    else:
        print(f"Kechirasiz, bizda {ovqat} yo'q")











