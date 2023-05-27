# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:11:39 2023

@author: Sayitkamol

16-dars: Nesting
"""

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'karobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'karobka':'mexanika'
        }

car2 = {
        'model':'malibu',
        'rang':'qizil',
        'yil':2019,
        'narh':20000,
        'km':20000,
        'karobka':'mexanika'
        }

cars = [car0, car1, car2]

for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']}, "
          f"{car['yil']}-yil, "
          f"{car['narh']}$ ")

print(cars[0]['model'].title()) # Ro'yhat ichidagi lug'atlarga quyidagicha murojaat qilish mumkin

print(f"{cars[0]['rang']} "
      f"{cars[0]['model'].title()}")


malibus = []

for n in range(10):
    new_car = {
        'model':'malibu',
        'rangi':None,
        'yil':2023,
        'narh':None,
        'km':0,
        'karobka':'avto'
        }
    malibus.append(new_car)

for malibu in malibus[0:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

for malibu in malibus[6:10]:
    malibu['rang'] = 'oq'
    malibu['karobka'] = 'mexanika'


for malibu in malibus:
    if malibu['karobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000
        
# print(malibus)


dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi tillarni biladi:")
    for til in tillar:
        print(til.upper())


hamkasblar = {
    'ali':{'familiya':'valiyev',
            'yoshi':20,
            'tyil':2002,
            'malumoti':'oliy',
            'tillar':['python','c++'] 
            },
    
    'vali':{'familiya':'aliyev',
            'yoshi':28,
            'tyil':1995,
            'malumoti':'orta-naxsus',
            'tillar':['html','css','js'] 
            },
    
    'hasan':{'familiya':'husanov',
            'yoshi':26,
            'tyil':1997,
            'malumoti':'maxsus',
            'tillar':['python','php'] 
            }
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tugilgan, "
          f"\nMalumoti - {info['malumoti']}."
          f"\nQuyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())


""" Amaliyotlar """

''' 1, 2 '''

adabiyot = {
    'abu abdulloh muhammad ibn ismoil':{'tyil':810,
                                        'tjoy':'buxoro',
                                        'umri':60,
                                        'asarlari':['al-jome\' as-sahih',
                                                    'al-adab al-mufrod',
                                                    'at-tarix -kabir',
                                                    'at-tarix as-sagir'] 
                                        },
    
    'abdulla qodiriy':{'tyil':1894,
                        'tjoy':'toshkent',
                        'umri':44,
                        'asarlari':['o\'tgan kunlar',
                                    'mehrobdan chayon',
                                    'obid ketmon']
                                        },
    'erkin vohidov':{'tyil':1936,
                      'tjoy':'farg\'ona',
                      'umri':80,
                      'asarlari':['tong nafasi',
                                  'qo\'shiqlarim sizga',
                                  'o\'zbegim',
                                  'qiziquvchan matmusa'] 
                                        },
    'alisher navoiy':{'tyil':1441,
                      'tjoy':'hirot',
                      'umri':60,
                      'asarlari':['hamsa',
                                  'lison it-tayr',
                                  'mahbub ul-qulub',
                                  'munojot'] 
                                        }
    }

for ism, info in adabiyot.items():
    print(f"\n{ism.title()} "
          f"{info['tyil']}-yilda {info['tjoy'].capitalize()}da tugilgan."
          f" {info['umri']} yil umr ko\'rgan."
          f"\nYozgan mashxur asarlari:")
    for asar in info['asarlari']:
        print(asar.capitalize())

''' 3 '''

kinolar = {
    'ali':['po\'lat alandar', 'ichkarida', 'tashqarida'],
    'vali':['abdullajon', 'shaytanat', 'titanic'],
    'abror':['po\'lat alandar', 'ichkarida', 'tashqarida'],
    'elbek':['abdullajon', 'shaytanat', 'titanic']
    }

for ism, kino in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kin in kino:
        print(kin.capitalize())

''' 4 , 5'''

davlatlar = {
    "o'zbekiston":{'poytaxti':'toshkent',
                   'aholisi':36001236,
                   'hududi':'448 978 kv.km',
                   'pul_birligi':"so'm"},
    
    "amerika":{'poytaxti':'washington',
               'aholisi':331000000,
               'hududi':'9 833 520 kv.km',
               'pul_birligi':"dollar"},
    
    "turkiya":{'poytaxti':'ankara',
               'aholisi':36001236,
               'hududi':'783 562 kv.km',
               'pul_birligi':"turk lirasi"},
    
    "rassiya":{'poytaxti':'maskva',
               'aholisi':145478097,
               'hududi':'17 098 246 km2',
               'pul_birligi':"rubl"}
    
    }

for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxti'].title()}."
          f"\nHududi: {info['hududi']}"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul_birligi']}")

davlat0 = input("Davlat nomini kiriting:\n>>>")

# 1-usul
davlat = davlatlar.get(davlat0)

if davlat == None:
    print("Bizda bu davlat haqida ma'lumot mavjud emas!")
else:
    print(f"\n{davlat0.title()}ning poytaxti {davlat['poytaxti'].title()}."
          f"\nHududi: {davlat['hududi']}"
          f"\nAholisi: {davlat['aholisi']}"
          f"\nPul birligi: {davlat['pul_birligi']}")
        
# 2-usul
if davlat0 in davlatlar:
    davlat = davlatlar[davlat0]
    print(f"\n{davlat0.title()}ning poytaxti {davlat['poytaxti'].title()}."
          f"\nHududi: {davlat['hududi']}"
          f"\nAholisi: {davlat['aholisi']}"
          f"\nPul birligi: {davlat['pul_birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas!")




