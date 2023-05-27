# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:49:40 2023

@author: Sayitkamol

14-dars: LUG'AT BILAN TANISHUV

"""

# talaba_0 = {'ism':'Murod Alimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tugilgan,\
# {talaba_0['yosh']} yoshda")

# talaba_0["kurs"] = 4
# talaba_0['fakultet'] = 'informatika'

# talaba_1 = {}

# talaba_1["ism"] = 'Aziz'
# talaba_1['kurs'] = 4
# talaba_1['yosh'] = 24

# print(talaba_1)
# print(f"{talaba_1['ism'].title()} {talaba_1['kurs']}-kurs {talaba_1['yosh']} yoshda")

# del talaba_1['yosh']
# print(talaba_1)

# telefonlar = {
#     'ali':'iPhone x',
#     'vali':'Galaxy s10',
#     'nodir':'Note 10',
#     'eldor':'red mi note 10'
#     }

# # print(telefonlar)

# # phone = telefonlar['ali']
# # print(f"Alining telefoni {phone}")

# # phone = telefonlar['hasan']
# # print(f"Hasanning telefoni {phone}")
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
# print(phone)


""" Amaliyot """

''' 1 '''

# otam = {'ism':'Abdumumin','t_yil':1971,'manzil':"o'rta ko'rg'on"}
# print(f"Otam {otam['ism'].title()}, {otam['t_yil']}-da {otam['manzil']}da tug'ilgan.")

''' 2 '''

# ovqatlar = {'dadam':'osh','onam':'shorva','ukam':'somsa','akam':'manti','opam':'mastava'}
# print(f"Dadamning yoqtirgan ovqati {ovqatlar['dadam']}")

''' 3 '''

lugat = {
    "string":'matnlar',
    'intager':'butun son. U int shaklida qisqartirib yoziladi',
    'float':'haqiqiy son',
    'boolen':'rost yoki yolgonni tekshiradi'
    }

soz = input("So'z kiriting:").lower()
# print(lugat.get(soz,"Bunday so'z mavjud emas"))
tarjima = lugat.get(soz)
if tarjima == None:
    print("Bunday soz mavjud emas")
else:
    print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi")











