 # -*- coding: utf-8 -*-
"""
Created on Thu May  4 01:04:41 2023

@author: Sayitkamol

19-dars: FUNKSIYA

"""

def salom_ber():
    '''Salom beruvchi funksiya'''
    print("Assalamu Alaykum")

# salom_ber()

# docstring funksiyadan foydalanayotganda malumot beradigan matn
def salom_ber0(ism):
    """Foydalanuvchi ismini qabul qilib, 
    unga salom beruvchi funksiya"""
    print(f"Assalamu Alaykum, hurmatli {ism.title()}")

# salom_ber('hasan')


def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('olim','hakimov')


def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")

# yosh_hisobla('ali',1997)

# yosh_hisobla(tugilgan_yil = 1997, ism='vali')

def yosh_hisobla2(tugilgan_yil, joriy_yil=2023):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{joriy_yil-tugilgan_yil} yoshda")

# yosh_hisobla2(1995,2023)

""" Amaliyotlar """

''' 1 '''

def tugilgan_yilni_hisobla(ism, yosh):
    """Foydalanuvchining tugilgan yilini hisiblovchi dastur"""
    print(f"{ism.title()}ning tugilgan yili: {2023-yosh}")

# tugilgan_yilni_hisobla('ali', 20)

''' 2 '''

def kv_kub_hisobla(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini hisoblaydigan dastur"""
    print(f"{son} sonining kadrai: {son**2}, "
          f"kubi: {son**3}")

# kv_kub_hisobla(23)

''' 3 '''

def juft_or_toq_hisobla(son):
    """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son % 2 == 0:
        print(f"{son} soni juft son")
    else:
        print(f"{son} soni toq son")
        
# juft_or_toq_hisobla(23)
# juft_or_toq_hisobla(32)

''' 4 '''

def kattasini_chiqar(son1, son2):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaruvchi dastur"""
    if son1 < son2:
        print(f"{son2} soni {son1} dan katta")
    elif son1 > son2:
        print(f"{son1} soni {son2} dan katta")
    else:
        print("Sonlar teng")
        
# kattasini_chiqar(12, 23)
# kattasini_chiqar(122, 23)
# kattasini_chiqar(55, 55)


''' 5 '''

def kv_hisbla(x, y):
    """Foydalanuvchidan x va y sonlarini olib, x**y ni konsolga chiqaruvchi funksiya"""
    print(x**y)

# kv_hisbla(3, 3)

''' 6 '''

def kv_hisbla2(x, y=2):
    """Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya"""
    print(x**y)

# kv_hisbla2(3,3)
# kv_hisbla2(3)

''' 7 '''

def bolinish_alomatlari(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for n in range(2,11):
        if son%n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)
bolinish_alomatlari(70)










