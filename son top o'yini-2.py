# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:21:17 2023

@author: User
"""

import random as r

print("Keling o'ylagan sonni topish o'ynaymiz!")

def sontop(x=10):
    tasodifiy_son = r.randint(1,x)
    print(f"1 dan {10} gacha son o'yladim topa olasizmi?\n>>> ")
    taxminlar = 0
    while True:
        taxminlar+=1
        taxmin = int(input(">>>"))
        
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
        
    return taxminlar
    print(f"tabriklaymiz.{taxminlar} taxmin bilan topdingiz")        
    
    
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugamani bosing. men topaman.")
    taxminlar = 0
    quyi = 1
    yuqori = x
    
    while True:
        taxminlar +=1
        if quyi != yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            taxmin = yuqori - 1
        elif javob == "+":
            taxmin = quyi + 1
        else:
            break
        
    return taxminlar
    print("{taxminlar} ta taxmin bilan topdim")
    
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
            
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    