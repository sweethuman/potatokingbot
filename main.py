# coding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time
import datetime
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher
shrugs = 0
lennys = 0
startTime = time.time()
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm the PotatoKing. Here to serve your wishes.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def queen(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="My Queen is @Michelle_1998")

queen_handler = CommandHandler('queen', queen)
dispatcher.add_handler(queen_handler)

def shrug(bot, update, args):
    text = ""
    args.append("1")
    if(args[0].isdigit()):
        if 0<int(args[0])<201:
            for n in range(int(args[0])):
                text = text + "¯\_(ツ)_/¯  "
            bot.sendMessage(chat_id=update.message.chat_id, text=text)
            global shrugs
            shrugs = shrugs + int(args[0])
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Out of range! Select number between 1 and 200.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Use a number! Other type of text is not accepted.")

shrug_handler = CommandHandler('shrug', shrug, pass_args=True)
dispatcher.add_handler(shrug_handler)
def lenny(bot, update, args):
    text = ""
    args.append("1")
    if(args[0].isdigit()):
        if 0<int(args[0])<201:
            for n in range(int(args[0])):
                text = text + "( ͡° ͜ʖ ͡°)  "
            bot.sendMessage(chat_id=update.message.chat_id, text=text)
            global lennys
            lennys = lennys + int(args[0])
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Out of range! Select a number between 1 and 200.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Use a number! Other type of text is not accepted.")

lenny_handler = CommandHandler('lenny', lenny, pass_args=True)
dispatcher.add_handler(lenny_handler)
def stats(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Shrugs printed: " + str(shrugs) + "\nLennys printed: " + str(lennys) + "\nTime: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "\nUptime: " + str(datetime.timedelta(seconds=int(time.time() - startTime))))
stats_handler = CommandHandler('stats', stats)
dispatcher.add_handler(stats_handler)
updater.start_polling()
