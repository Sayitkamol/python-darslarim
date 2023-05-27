# -*- coding: utf-8 -*-
"""
Created on Wed May  3 04:51:15 2023

@author: Sayitkamol

17-dars: While() sikli

"""

# ism = input("Ismingiz nima?\n>>>")
# savol = f"Salom {ism.title()}. Yoshingiz nechida"
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz nechchi?\n>>>")
# height = float(height)


# son = 1

# while son<=5:
#     print(son, end='')
#     son += 1 

# print("Dastur tugadi!")


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur!")
# savol = "Istalgan son kiriting: "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing)\n>>>"
# qiymat = ''

# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi!")


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur!")
# savol = "Istalgan son kiriting: "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing)\n>>>"
# ishora = True

# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!")


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur!")
# savol = "Istalgan son kiriting: "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing)\n>>>"

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# sonlar = list(range(1,11))

# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2}")

# sonlar = list(range(1,11))

# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2}")

''' '''
son = 0

while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son)
        











