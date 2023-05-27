# -*- coding: utf-8 -*-
"""
Created on Wed May  3 23:30:56 2023

@author: Sayitkamol

18-dars: While, ro'yxat va lug'at 
"""

ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n+=1
    if takrorlash != 'ha':
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())


print("D'stlaringiz yoshni saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingizning ismni kiriting:\n>>> ")
    yosh = input(f"{ism.title()}ning yoshini kiriting.\n>>> ")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana ma'lumot qo'shasizmi?  (ha/yo'q')\n>>> ")
    if javob != 'ha':
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")



cars = ['lacetti','nexia','malibu','damas','nexia','matiz','nexia','lacetti']
car = 'nexia'
while car in cars:
    cars.remove(car)
    
print(cars)



talabalar = ['hasan','husan','olim','botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
    
# print(baholangan_talabalar)

for talaba, baho in baholangan_talabalar.items():
    print(f"{talaba.title()}ning bahosi {baholangan_talabalar[talaba]}")


""" Amaliyot """




maxsulotlar = {'olma': 15000.0, 
               'anor': 20000.0, 
               'banan': 22000.0, 
               'uzum': 10000.0, 
               'gilos': 16000.0, 
               'apelsin': 25000.0
               }

while True:
    maxsulot = input("Maxsulot nomini kiriting: ")
    narh = float(input(f"{maxsulot.title()}ning narhini kiriting: "))
    maxsulotlar[maxsulot] = narh
    javob = input("Yana maxsulot kiritasizmi?\n(ha/yo'q) >>> ")
    if javob != 'ha':
        break

print("\nSiz kiritgan maxsulotlar:")
for maxsulot, narh in maxsulotlar.items():
    print(f"{maxsulot.title()}ning narxi {maxsulotlar[maxsulot]} so'm.")


buyurtmalar = []
savol = "Maxsulot nomini kiriting: "

while True:
    maxsulot = input(savol)
    buyurtmalar.append(maxsulot)
    javob = input("Yangi maxsulot kiritasizmi?  (ha/yo'q)\n>>> ")
    if javob != 'ha':
        break
# print("\nSiz buyurtma qilgan maxsulotlar: ")
# for n in buyurtmalar:
#     print(n.title())


for maxsulot in buyurtmalar:
    if maxsulot in maxsulotlar:
        print(f"{maxsulot.title()}ning narhi {maxsulotlar[maxsulot]} so'm")
    else:
        print(f"Bizda {maxsulot} yo'q")







