#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from pyowm import OWM

from tokens import *
from bot_messages import *

help_message = """Python Weather Bot
/get_city - Узнать текущий город
/change_city - Сменить город
/weather - Получить полные сведения о погоде в регионе
/temp - Узнать температуру
/wind - Узнать скорость ветра
/humidity - Узнать влажность в регионе"""

full_weather_info = f"""Полные сведения о погоде:
"""

city = "Moscow"
standart_city = "Moscow"  # Used to rollback in case of an error in choosing a city

owm = OWM(pyowm_token)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

bot = telebot.TeleBot(telegram_bot_token)

@bot.message_handler(commands=["start"])
def starting_the_bot(message):
    """Bot launch function"""
    bot.send_message(message.chat.id, "Поздравляю, вы запустили бота. \nЧтобы получить помощь, введите /help")


@bot.message_handler(commands=["help"])
def bot_helper_message(message):
    """Function that displays a help message"""
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["change_city"])
def change_city(message):
    """A function that changes the city"""
    bot.send_message(message.chat.id, "Введите название города: ")

    @bot.message_handler(content_types=["text"])
    def change_city_variable(message):
        """A function that modifies a city variable"""
        global city
        global observation
        global w

        try:
            city = message.text
            observation = mgr.weather_at_place(city)
            w = observation.weather
            bot.send_message(message.chat.id, "Успешно!")

        except:
            bot.send_message(message.chat.id, "Ошибка! Город введён неверно")
            city = standart_city
    

@bot.message_handler(commands=["get_city"])
def get_city(message):
    """Function that displays the current city"""
    bot.send_message(message.chat.id, f"Текущий город: {city}")


@bot.message_handler(commands=["weather"])
def get_weather(message):
    """Function that displays the weather in the city"""
    print(w.temperature('celsius'))


@bot.message_handler(commands=["temp"])
def get_temperature(message):
    """ """
    pass


@bot.message_handler(commands=["wind"])
def get_wind(message):
    """ """
    pass


@bot.message_handler(commands=["humidity"])
def get_humidity(message):
    """ """
    pass


if __name__ == "__main__":
    bot.polling(none_stop=True)
