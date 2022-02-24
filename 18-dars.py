# -*- coding: utf-8 -*-
"""
2022 yil, 22-fevral. 09:35:38 

Muallif: Sayitkamol

18-dars

"""

'''WHILE YORDAMIDA RO'YXATNI TO'LDIRISH'''
ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
    
print("\nDo'stlaringiz ro'yhati:")
for ism in ismlar:
    print(ism.title())
    
"""Do'stingizni yoshini saqlaymiz!"""
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

'''RO'YXAT ELEMENTLARINI O'CHIRISH'''
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)

'''RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH'''
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho


'''Amaliyot-1'''

print("Restoranimizga hush kelibsiz!")
buyurtmalar = []
ishora = True
n = 1

while ishora:
    buyurtma = input(f"{n}-buyurtmangizni berishingiz mumkin: ")
    buyurtmalar.append(buyurtma.title())
    javob = input("Yana buyurtma bermoqchimisiz? (ha\yo'q)")
    if javob == 'ha':
        n += 1
    if javob == "yo'q":
        ishora = False
    
print(f"Siz quyidagi buyurtmalarni amalga oshirdingiz:")    
for buyurtma in buyurtmalar:
    print(buyurtma)

'''Amaliyot-2'''
'''e-bozor uchun ...'''

print("E-bozorga hush kelibsiz!")
maxsulotlar = {}
n = 0
while True:
    maxsulot = input(f"{n+1}-maxsulot nomini kiriting: ")
    narhi = input(f"{maxsulot}ning narhini kiriting: ")
    
    maxsulotlar[maxsulot] = int(narhi)
    savol = input("Yana maxsulot kiritmoqchimisiz-(ha/yo'q): ")
    if savol != "ha":
        break
    
print("Siz kiritgan maxsulotlar ro'yhati:")
for maxsulot, narhi in maxsulotlar.items():
    print(f"\n{maxsulot.title()} narhi = {narhi}")

'''Amaliyot-3'''

 
















