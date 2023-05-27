# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:23:16 2023

@author: Sayitkamol

27-dars: TELEGRAM BOT

"""

from transiterate import to_cyrillic, to_latin
import telebot

TOKEN = "6227303472:AAEWuLOLkgeQjhhOLOaLYRTiT_UMZRSBQo0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom Alaykum, Hush kelibsiz!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(message, javob(msg))
    

bot.infinity_polling()