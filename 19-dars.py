# -*- coding: utf-8 -*-
"""
2022-yil, 22-fevral. 17:40:40 

Muallif: Sayitkamol

19-dars = "Funksiyalar"

"""

'''FUNKSIYA YARATAMIZ'''

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalamu alaykum!")
    
    
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

'''FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH'''

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism('olim','hakimov')

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

yosh_hisobla('olim', 1997)
yosh_hisobla(tugilgan_yil=1997, ism='olim')  #KALIT SO'Z BILAN UZATISH

'''STANDART QIYMAT'''

def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1995,2020)
yosh_hisobla(1993)

"""Amaliyot-1"""

def t_yil(ism, yosh):
    '''Tug\'ilgan yilni hisoblaydigan funksiya'''
    print(f"{ism.title()} siz {2022-yosh}-yil tug'ilgansiz!")
    
t_yil('ali', 25)

"""Amaliyot-2"""

def kvadrat_kub(son):
    '''Sonnong kvadrati va kubini hisoblaydigan funksiya'''
    kvadrat = int(son)**2
    kub = int(son)**3
    print(f"Siz kiritgan sonning kavdrati {kvadrat} ga teng.\nSiz kiritgan sonning kubi {kub} ga teng")
    
kvadrat_kub(3)

"""Amaliyot-3"""

def juft_toq(son):
    '''Son toq yoki juftligini aniqlovchi dastur'''
    if son % 2:
        print(f"Siz kiritgan {son} soni toq son")
    else:
        print(f"Siz kiritgan {son} soni juft son")
        
juft_toq(4)

"""Amaliyot-4"""

def katta_son(son1, son2):
    '''Katta sonni konsolga chiqaruvchi funksiya'''
    if son1 < son2:
        print(f"{son2} soni {son1}dan katta")
    elif son1 > son2:
        print(f"{son1} soni {son2}dan katta")
    else:
        print("Siz kiritgan sonlar teng!")
        
katta_son(11,23)

"""Amaliyot-5"""

def daraja(x,y):
    '''X ning Y darajasini konsolga chiqarish'''
    print(x**y)

daraja(4, 4)


"""Amaliyot-6"""

def daraja(x,y=2):
    '''X ning Y darajasini konsolga chiqarish'''
    print(x**y)

daraja(4, )

"""Amaliyot-7"""

def bolinish_alomatlari(son):
    '''2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya'''
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")  
            
bolinish_alomatlari(21)








