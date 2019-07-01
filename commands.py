from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(bot, update):
    update.message.reply_text('Ciao sono <b>[Nome ancora da decidere]</b>, per altre informazioni sulle mie funzioni e sui miei comandi usa /help!', parse_mode='HTML')
    print(update.message.chat_id)


def regole(bot, update):
    bot.send_message(update.message.chat_id, text='https://telegra.ph/Regolamento-Google-Pixel-Italia-02-17', parse_mode='HTML')

def help(bot, update):
    bot.send_message(update.message.chat_id, text=open('help.txt', 'r').read(), parse_mode='HTML')

def source(bot, update):
    bot.send_message(update.message.chat_id, text="<b>     Google Home Mini Bot</b>\n"
                                                  "=======================\n\n"
                                                  "<b>Files</b>:\n<em>- Bot.py\n- commands.py\n- handler.py\n- config.py\n- help.txt</em>\n\n"
                                                  "<b>IDE</b>:<em> PyCharm Community edition</em>\n\n"
                                                  "<b>Programming Language</b>:<code> Python</code>\n\n"
                                                  "<b>Languages:</b> <em>Italian</em>\n\n"
                                                  "<b>Version</b>:<em> v.0.1 - beta</em>\n\n"
                                                  "<b>Source</b>:  <a href=\"https://github.com/MikeM2000/open_telegram_bot\">GitHub</a> ",
                                             parse_mode='HTML')


#COMANDI CARD
#COMANDI CARD END

#COMANDO PARSE HTML
def parse(bot,update):
    bot.send_message(update.message.chat_id, 
                 text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', 
                 parse_mode='HTML')

def button(bot, update):
    query = update.callback_query
    if query.data == '1':
        query.edit_message_text(text="L'utente non è un robot!")
        bot.restrict_chat_member(update.effective_chat.id, update.effective_user.id, can_send_messages=True,
                                 can_send_media_messages=True, can_send_other_messages=True,
                                 can_add_web_page_previews=True)

