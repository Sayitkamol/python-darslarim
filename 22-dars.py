# -*- coding: utf-8 -*-
"""
Created on Fri May  5 02:05:48 2023

@author: Sayitkamol

22-dars: *args av **kwargs

"""

def summa(*sonlar):
    """Sonlar yigindisini qaytaruvchi funksiya"""
    
    return sum(sonlar)
    
    # yigindi = 0
    # for son in sonlar:
    #     yigindi += son
    # return yigindi

def summa2(x,y,*sonlar):
    """Sonlar yigindisini qaytaruvchi funksiya"""
    
    return x+y+sum(sonlar)


# print(summa(12,23,34))
# print(summa(1,2,3))
# print(summa(1,2,3,4,5))

# print(summa2(12,23,34))
# print(summa2(1,2))
# print(summa2(1,2,3,4,5))

def avto_info(kompaniya, model,**malumotlar):
    """Avtolar haqidagi malumotni lugat ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('gm', 'malibu', rang='qora', yil=2019)
avto2 = avto_info('kia', 'k5', rang='qizil', yil=2020, narh=35000, korobka='avtomat')

# print(avto1)
# print(avto2)

""" Amaliyotlar """

''' 1 '''

def kopaytir(*sonlar):
    """Sonlarning kopaytmasini qaytaruvchi funksuya"""
    kopaytma=1
    for son in sonlar:
        kopaytma *= son
    
    return kopaytma

son1 = kopaytir(2,3,5,4,5)
# print(son1)

''' 2 '''

def talaba_info(ism,familiya,**infolar):
    """Talabalar haqidagi malumotlarni jamlovchi funksiya"""
    infolar['ism']=ism
    infolar['familiya']=familiya
    
    return infolar

talaba1 = talaba_info('ali','valiyev')
talaba2 = talaba_info('vali','aliyev',tyil=1997,tjoy='bek')
print(talaba1, talaba2)

