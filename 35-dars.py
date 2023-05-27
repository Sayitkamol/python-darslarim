# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:58:16 2023

@author: Sayitkamol

35-dars: XATOLAR BILAN ISHLASH
"""

# # ValueError
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2023-yosh} yilda tugilgansiz")


# # ZeroDivisionError
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")


# #IndexError
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
        

# # KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":'admin@sasriq.dev',
#         "phone":"998971234556"}

# key = "email"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")



# # FileNotFoundError
# filename = 'data.txt'
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas")

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json']
# for filename in files:
#     try:
#         with open(filename)as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass
#         # print(f"{filename} fayl mavjud emas")
#     else:
#         print(talaba['ism'])

# # ValeuError and ZeroDivisionError
# n = input("Butun son kiriting: ")
# try: 
#     n = int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# else:
#     print(f"x={x}")


while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
print(f"Siz {2023-yosh}-ylda tugilgansiz")




