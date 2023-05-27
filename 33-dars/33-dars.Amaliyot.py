# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:39:09 2023

@author: Sayitkamol

33-dars: Amaliyot
"""

"""Amaliyot"""

with open('pi_million_digits.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')

bdate = "2111997"
# print(bdate in pi)





with open('info.txt','a') as file:
    
    while True:
        info = input("Ma'lumot kiriting: ")
        infos = file.write(info + '\n')
        
        javob = input("Yana qo'shasizmi? (yes/no)\n>>> ")
        if javob != 'yes':
            break
        
with open('info.txt') as file:
    infos = file.read()
    
print(infos)