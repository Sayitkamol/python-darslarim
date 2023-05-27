# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:45:33 2023

@author: Sayitkamol

11-dars: is-elif-else

"""

# yosh = int(input("Yoshingiz nechida:"))

# if yosh <=4:
#     narx = 0
# elif yosh <=12:
#     narx = 5000
# elif yosh <= 18:
#     narx = 8000
# else:
#     narx = 10000

# print(f"Sizga kirish {narx} so'm")


# kun = input("Bugun qaysi kun?\n>>>")

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni!")
# else:
#     print("Bugun ish kuni")


# kun = input("Bugun nima kun?\n>>>")
# harorat = float(input("Bugun havo harorati qanday?\n>>>"))

# if kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat >= 30:
#     print("Cho'milgani kettik!")
    
# elif kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat <= 30:
#     print("Uyda dam olamiz")
    

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?\n>>>')
# if ovqat in menu:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Kechirasiz, bizda bunday ovqat mavjud emas")


# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar:
#     for ovqat in buyurtmalar:
#         if ovqat in menu:
#             print(f"Menuda {ovqat} bor.")
#         else:
#             print(f"Menuda {ovqat} yo'q")
# else:
#     print("Ro'yat bo'sh!")

""" Amaliyot """

''' 1 '''

# son = float(input("Juft son kiriting:"))

# if son % 2:
#     print("Bu juft son emas!")
# else:
#     print("Rahmat")


''' 2 '''

# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh <= 4 or yosh >= 60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000  
# elif yosh >= 18:
#     narh = 20000    

# print(f"Sizga kirish {narh} so'm")

''' 3 '''

# son1 = float(input("Birinchi sonni kiriting:"))
# son2 = float(input("Ikkinchi sonni kiriting:"))

# if son1 < son2:
#     print(f"{son1} kichkina {son2}dan")
# elif son1 > son2:
#     print(f"{son1} katta {son2}dan")
# else:
#     print(f"{son1} va {son2} lar teng")


''' 4 '''

# mahsulotlar = ['anor', 'banan', 'uzum', 'anjir', 'behi', 'olma', 'nok', 'ananas', 'qulupnay', 'mandarin']
# bor_mahsulot = []
# yoq_mahsulot = []

# for n in range(5):
#     n = input(f'{n+1}-mahsulotni kiriting:')
#     if n in mahsulotlar:
#         bor_mahsulot.append(n)
#     else:
#         yoq_mahsulot.append(n)
        
# print(bor_mahsulot)
# print(yoq_mahsulot)

# # if bor_mahsulot:
# #     print("Do'konimizda siz so'ragan quyidagi mahsulotlar bor:")
# #     for n in bor_mahsulot:
# #         print(n)
# # # else :
# #     print("Do'konimizda siz so'ragan hech qaysi mahsulot yo'q")

# if yoq_mahsulot:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for n in yoq_mahsulot:
#         print(n)
# else:
#     print("Siz so'ragan barcha mahsulot do'konimizda bor")

''' 5 '''

# foydalanuvchilar = ['ali','vali','hasan','husan','olim','ravshan']
# login = input("Yangi login tanlang:")

# if login.lower() in foydalanuvchilar :
#     print(f"Kechirsiz, {login} logini band. Boshqa login tanlang")
# elif login.lower() not in foydalanuvchilar:
#     print("Xush kelibsiz")

''' 6 '''

# son = int(input("Butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



