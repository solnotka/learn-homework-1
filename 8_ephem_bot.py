"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD
    }
}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def where_is_planet(bot, update):
    user_planet = update.message.text.split()[-1].capitalize()
    today = str(date.today())
    zodiac = {"Aries": "Овна", "Taurus": "Тельца", "Gemini": "Близнецов",
              "Cancer": "Рака", "Leo": "Льва", "Virgo": "Девы",
              "Libra": "Весов", "Scorpius": "Скорпиона", "Ophiuchus": "Змееносца",
              "Sagittarius": "Стрельца", "Capricornus": "Козерога",
              "Aquarius": "Водолея", "Pisces": "Рыб"}
    planets = {"Jupiter": "Юпитер", "Mars": "Марс", "Mercury": "Меркурий",
               "Moon": "Луна", "Neptune": "Нептун", "Pluto": "Плутон",
               "Saturn": "Сатурн", "Sun": "Солнце", "Uranus": "Уран", "Venus": "Венера"}
    print(today, user_planet)

    if user_planet in planets:
      user_constel = ephem.constellation(eval(f'ephem.{user_planet}("{today}")'))[1]
      print(user_constel)
      update.message.reply_text(f'Сегодня {planets[user_planet]} находится в созвездии {zodiac[user_constel]}')
    else:
      update.message.reply_text("Пожалуйста, введите английское название планеты")
    

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", where_is_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
