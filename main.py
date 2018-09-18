import random
import telebot
import os
import logging
from telebot import types

token = os.environ['TELEGRAM_TOKEN']
api_token = os.environ['SOME_API_TOKEN']
logger = telebot.logger
telebot.logger.setLevel(logging.CRITICAL)  # Outputs debug messages to console.
bot = telebot.AsyncTeleBot(token + ":" + api_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("Начать тест")
    itembtn2 = types.KeyboardButton("Не начинать тест")
    markup.add(itembtn1, itembtn2)
    # bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    task = bot.reply_to(message, "Привет, я тест на ICQ 2chby\nНачать тест?", reply_markup=markup)
    result = task.wait()
    print(result)


@bot.message_handler(func=lambda message: message.text == "Начать тест")
def getName(message):
    markup = types.ForceReply(selective=False)
    task = bot.reply_to(message, "Введите имя:", reply_markup=markup)
    result = task.wait()
    print(result)

@bot.message_handler(func=lambda message: message.text == "Не начинать тест")
def getFucked(message):
    markup = types.ForceReply(selective=False)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("Начать тест")
    itembtn2 = types.KeyboardButton("Не начинать тест")
    markup.add(itembtn1, itembtn2)
    # bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    task = bot.reply_to(message, "Че, зассцал?", reply_markup=markup)
    result = task.wait()
    print(result)

@bot.message_handler(func=lambda message: True)
def test(message):
    if message.reply_to_message.text == "Введите имя:" and message.text is not None:
        # markup = types.ForceReply(selective=False)
        a = random.randint(50, 200)
        result = None
        if a < 100:
            task = bot.reply_to(message,
                                "Ну что же, " + message.chat.username + " под псевдонимом " + message.text + "\nВаш результат: " + str(
                                    a) + "\nДобро пожаловать в /soc/!")
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton("Начать тест")
            itembtn2 = types.KeyboardButton("Не начинать тест")
            markup.add(itembtn1, itembtn2)
            task = bot.reply_to(message, "Еще разок?", reply_markup=markup)
            result = task.wait()
        elif a < 140:
            task = bot.reply_to(message,
                                "Ну что же, " + message.chat.username + " под псевдонимом " + message.text + "\nВаш результат: " + str(
                                    a) + "\nПоздравляем! Вы нормальный человек.")
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton("Начать тест")
            itembtn2 = types.KeyboardButton("Не начинать тест")
            markup.add(itembtn1, itembtn2)
            task = bot.reply_to(message, "Еще разок?", reply_markup=markup)
            result = task.wait()
        elif a < 160:
            task = bot.reply_to(message,
                                "Ну что же, " + message.chat.username + " под псевдонимом " + message.text + "\nВаш результат: " + str(
                                    a) + "\nВам можно доверить админку в конфе 2chby.")
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton("Начать тест")
            itembtn2 = types.KeyboardButton("Не начинать тест")
            markup.add(itembtn1, itembtn2)
            task = bot.reply_to(message, "Еще разок?", reply_markup=markup)
            result = task.wait()
        else:
            task = bot.reply_to(message,
                                "Ну что же, " + message.chat.username + " под псевдонимом " + message.text + "\nВаш результат: " + str(
                                    a) + "\nВышмат одним этажом выше.")
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton("Начать тест")
            itembtn2 = types.KeyboardButton("Не начинать тест")
            markup.add(itembtn1, itembtn2)
            task = bot.reply_to(message, "Еще разок?", reply_markup=markup)
            result = task.wait()


    print(result)


bot.polling(none_stop=True)
