# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:12:23 2023

@author: Sayitkamol

23-dars: MODULLAR

"""

'''1-usul'''
# import avto_info_mod

# avto1 = avto_info_mod.avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# avto_info_mod.avto_print(avto1)


'''2-usul'''
# import avto_info_mod as aim

# avto1 = aim.avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# aim.info_print(avto1)


'''3-usul'''
# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# info_print(avto1)


'''4-usul'''  # Funksiya nomi uzul yoki bizning dasturimizda ham shunday funksiya bolsa
# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("gm", "malibu", "qora", "avtomat", 2020, 40000)
# iprint(avto1)


'''5-usul'''  # Bu usul modul kichkina bolganda ishlatgan yaxshi
 
# from avto_info_mod import *

# avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# info_print(avto1)

'''Math moduli'''
# import math 

# x=400
# print(math.sqrt(x)) # Ildiz
# print(math.pow(5,3)) # Birinchi sonni ikkinchi sonning darajasiga kotaradi
# print(math.pi) # PI ning qiymati katta aniqlik bilan kerak bolsa. Bu o'zgaruvchi
# print(math.log2(8))
# print(math.log10(100))


'''random moduli'''
# import random as r

# # randint()
# son = r.randint(0, 100)
# print(son)

# # choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


'''shuffle moduli'''
# shuffle() aralashtirib tashlaydi
# x=list(range(11))
# print(x)
# r.shuffle(x)
# print(x)











