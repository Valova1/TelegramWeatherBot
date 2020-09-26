#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from pyowm import OWM
from tokens import *


help_message = """Python Weather Bot
/get_city - Узнать текущий город
/change_city - Сменить город
/weather - Получить полные сведения о погоде в регионе
/temp - Узнать температуру
/wind - Узнать скорость ветра
/humidity - Узнать влажность в регионе"""

owm = OWM(pyowm_token)
mgr = owm.weather_manager()
observation = mgr.weather_at_place("Moscow")
w = observation.weather

bot = telebot.TeleBot(telegram_bot_token)

city = "Moscow"


@bot.message_handler(commands=["start"])
def starting_the_bot(message):
    bot.send_message(message.chat.id, "Поздравляю, вы запустили бота. \nЧтобы получить помощь, введите /help")


@bot.message_handler(commands=["help"])
def bot_helper_message(message):
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["change_city"])
def change_city(message):
    bot.send_message(message.chat.id, "Введите название города: ")

    @bot.message_handler(content_types=["text"])
    def change_city_variable(message):

        global city

        try:
            city = message.text
            observation = mgr.weather_at_place(city)
            w = observation.weather
            bot.send_message(message.chat.id, "Успешно!")

        except:
            bot.send_message(message.chat.id, "Ошибка! Город введён неверно")


@bot.message_handler(commands=["get_city"])
def get_city(message):
    bot.send_message(message.chat.id, f"Текущий город: {city}")


if __name__ == "__main__":
    bot.polling(none_stop=True)
