import telebot

bot = telebot.TeleBot('7003201155:AAG0OJJ9oOAov8DG_UrgQEiLEawUqcJt_do') #insert here ur tg bot token

class Alert:
    @staticmethod
    def alert(mass):
        bot.send_message(5534088209, mass) #changes 5534.. to ur chat id

