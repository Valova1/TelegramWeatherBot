#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from pyowm import OWM
from tokens import *


owm = OWM(pyowm_token)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moscow')
w = observation.weather
print(w)
