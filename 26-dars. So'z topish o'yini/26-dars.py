# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:57:33 2023

@author: Sayitkamol

26-dars: SO'Z TOPISH O'YINI

"""

from uzwords import words
import random as r

def get_word():
    soz = r.choice(words)
    while "-" in soz or ' ' in soz:
        soz = r.choice(words)
    return soz.upper()


def display(harflar, word):
    display_harflar = ""
    for harf in harflar:
        if harf in word.upper():
            display_harflar+=harf
        else:
            display_harflar += "-"    
    
    return display_harflar


def play():
    word = get_word()
    word_harflar = set(word)
    harflar = []
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")
    
    while word_harflar:
        print(display(harflar, word))
        if harflar:
            print(f"Shu paytgacha kiritgan harflaringiz: {harflar}")
        
        harf = input("Harf kiriting: ").upper()
        if harf in harflar:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue
        elif harf in word:
            word_harflar.remove(harf)
            print(f"{harf} harfi to'gri")
        else:
            print("Bunday harf yo'q")
        harflar += harf
    
    print(f"Tabriklaymiz {word} so'zini {len(harflar)} ta urunishda topdinging.")





