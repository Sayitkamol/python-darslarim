# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:14:38 2023

@author: Sayitkamol

20-dars: QIYMAT QAYTARUVCHI FUNKSIYA

"""

def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))


def oraliq2(min,max,step=1):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        if step:
            sonlar.append(min)
            min += step
        else:
            sonlar.append(min)
            min += 1
    return sonlar

print(oraliq(0,21,2)) # 0 dan 21 gacha 2 qadam bilan


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break


""" Amaliyotlar """

''' 1 , 2'''

def user_info(ism, familiya, tugilgan_yil, tugilgan_joy, email='', telefon_nomer=''):
    mijozlar = {'ism':ism,
                     'familiya':familiya,
                     'tugilgan_yil':tugilgan_yil,
                     'tugilgan_joy':tugilgan_joy,
                     'email':email,
                     'telefon_nomer':telefon_nomer}
    
    return mijozlar

foydalanuvchi1 = user_info('ali','valiyev', 1997,'bekobod','email', +812002323)
print(foydalanuvchi1)

mijozlar = []
print("Mijozlar ro'yxati:")
while True:
    ism = input("Ismini kiriting: ")
    familiya = input("Familiyani kiriting: ")
    tugilgan_yil = input("Tug'ilgan yilini kiriting: ")
    tugilgan_joy = input("Tugilgan joyini kiriting: ")
    email = input("Elektron pochta manzilini kiriting (Y'oq bo'lsa 'no' qo'ying'): ")
    telefon_nomer = input("Telefon nomerni kiriting (Y'oq bo'lsa \"bo'sh\" qoldiring): ")
    
    mijozlar.append(user_info(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon_nomer))
    
    javob=input("Yana mijoz qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break
    
#   manzilda xatolik bor
n=1
for mijoz in mijozlar:
    manzil = mijoz[tugilgan_joy]
    print(f"{n}-mijoz. {mijoz['ism'].title()} {mijoz['familiya'].title()}. "
          f"{mijoz['tugilgan_yil']}-yili {manzil.title()}da tugilgan.")
    n += 1
    if email:
        print(f"Elektron pochta manzili: {email}")
    if telefon_nomer:
        print(f"Telefon nomeri: {telefon_nomer}")


''' 3 '''

def kattasini_chiqar(son1,son2,son3):
    if son1<son2<son3:
        return son3
    elif son1<son2>son3:
        return son2
    elif son1>son2>son3:
        return son1
    else:
        return 'sonlar teng'

# print(kattasini_chiqar(12, 23, 45))

''' 4 '''

def aylana_info(radius, pi=3.14159):
    aylana= {'radius': radius,
             'diametr': 2 * radius,
             'perimetr': 2 * radius * pi,
             'yuza': pi * radius ** 2}
    return aylana


''' 5 '''

def tub_sonlar(min,max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub=True
        if n ==1:
            tub=False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n%x == 0:
                    tub = False
                    
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar


''' 6 '''

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


# print(fibonacci(10))










