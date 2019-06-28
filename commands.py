from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.message.reply_text('Ciao sono Google Assistant, per altre informazioni sulle mie funzioni usa /help!')
    print(update.message.chat_id)


def regole(bot, update):
    bot.send_message(update.message.chat_id, text='https://telegra.ph/Regolamento-Google-Pixel-Italia-02-17', parse_mode='HTML')

def help(bot, update):
    bot.send_message(update.message.chat_id, text=open('help.txt', 'r').read(), parse_mode='HTML')


#COMANDI CARD
#COMANDI CARD END

#COMANDO PARSE HTML
def parse(bot,update):
    bot.send_message(update.message.chat_id, 
                 text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', 
                 parse_mode='HTML')    
