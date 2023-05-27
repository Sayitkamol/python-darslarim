# -*- coding: utf-8 -*-
"""
Created on Fri May 26 21:47:17 2023

@author: Sayitkamol

33-2-dars: FILES

"""

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs':2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs':1}

with open('info.pkl','wb') as file:     # Faylga yozish
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('info.pkl','rb')as file:      # Faylni o'qish
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)



    




    