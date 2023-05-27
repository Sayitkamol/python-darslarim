# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:56:40 2023

@author: Sayitkamol

34-dars: JSON 
"""
import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

sonlar = (12,45,23,67)
sonlar_json = json.dumps(sonlar)


bemor = {
    "ism":"Alijon Valiyev",
    'yosh':30,
    'oila':True,
    'farzandlar':('Ahmad','Bonu'),
    'allergiya':None,
    'dorilar':[
            {"nomi":'Analgin', 'miqdori':0.5},
            {"nomi":'Panadol', 'miqdori':1.2}
        ]
    }

bemor_json = json.dumps(bemor)
# print(bemor_json)

# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)

with open('bemor_json', 'w') as f:
    json.dump(bemor,f)


bemor2 = json.loads(bemor_json)

filename = 'bemor_json.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))