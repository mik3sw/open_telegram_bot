from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


# DEFINIZIONE COMANDI ADMIN
from functools import wraps
import wikipedia

LIST_OF_ADMINS = [38201859]

# FUNZIONI
def cancellacomandi(bot, update):
    if update.message.text is not None:
        if update.message.text.startswith("/"):
            bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)


def admin(bot, update):
    if update.message.text is not None:
        if update.message.text.startswith("@admin"):
            var_messaggio = update.message.text
            var_messaggio = update.message.text[7:]
            bot.send_message('@AOSPItaliaLOG',
                             text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\n\n<b>Gruppo</b>: {}\n<b>Autore</b>: @{username}\n<b>Messaggio</b>: <code>{}</code>\n\n<b>Vai al messaggio</b>: https://t.me/{}/{}"
                             .format(update.message.chat.title, var_messaggio, update.message.chat.username, update.message.message_id, username=update.message.from_user.username, ),
                             parse_mode='HTML')
            bot.send_message(update.message.chat_id, "<code>Segnalazione effettuata!</code>", reply_to_message_id=update.message.message_id, parse_mode='HTML')

# RISPOSTE DI Gassistant
def okgoogle(bot, update):
    if update.message.text is not None:
        if str(update.message.text).lower() == "ok google":
            bot.send_message(update.message.chat_id,
                             "Ciao {name}, come posso aiutarti?".format(name=update.message.from_user.first_name))


def nexus5x(bot, update):
    if update.message.text is not None:
        if 'nexus 5x' in str(update.message.text).lower():
            bot.send_message(update.message.chat_id, 'Do you want some bootloop?', reply_to_message_id=update.message.message_id)


# Buongiorno
def buongiorno(bot, update):
    if update.message.text is not None:
        if 'buongiorno' in str(update.message.text).lower():
            bot.send_message(update.message.chat_id,
                             "Buongiorno {name}".format(name=update.message.from_user.first_name), reply_to_message_id=update.message.message_id)


# Buonanotte
def buonanotte(bot, update):
    if update.message.text is not None:
        if 'buonanotte' in str(update.message.text).lower():
            bot.send_message(update.message.chat_id,
                             "Buonanotte {username}".format(username=update.message.from_user.username, reply_to_message_id=update.message.message_id))


def say(bot, update):
    if update.message.text is not None:
        if update.message.text.startswith("/say"):
            user_id = update.effective_user.id
            if user_id in LIST_OF_ADMINS:
                var_messaggio = update.message.text
                var_messaggio = var_messaggio.replace("/say", "")
                bot.send_message(update.message.chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')

def definisci(bot, update):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith('definisci'):
            var_messaggio = str(update.message.text).lower()
            var_messaggio = var_messaggio.replace("definisci ", "")
            print("{} searced a definition from Wikipedia".format(update.message.from_user.username))
            wikipedia.set_lang("it")
            try:
                definition = wikipedia.summary(var_messaggio, sentences=3)
                bot.sendMessage(update.message.chat_id, text=definition)
            except:
                bot.sendMessage(update.message.chat_id,
                                text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(update.message.from_user.first_name, var_messaggio))


def welcome(bot, update):
    for new in update.message.new_chat_members:
        keyboard = [[InlineKeyboardButton("Non sono un Robot", callback_data='1')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Benvenuto {username} in {chat_title}!\n"
                                  "Ti preghiamo di rispettare le /regole per non ricevere sanzioni\n"
                                  "Buona permanenza!\n\n<em>- lo staff</em>".format(
            username="@" + new.username,
            chat_title=update.message.chat.title
        ), reply_markup=reply_markup, parse_mode='HTML')
        bot.send_message('@AOSPItaliaLOG',
                         text="<b>NUOVO UTENTE</b>\n\n<b>Gruppo</b>: {}\n<b>Utente</b>: @{username}\n\n<b>Vai al messaggio</b>: https://t.me/{}/{}"
                         .format(update.message.chat.title, update.message.chat.username,
                                 update.message.message_id, username=update.message.from_user.username, ),
                         parse_mode='HTML')
        bot.restrict_chat_member(update.message.chat_id, update.message.from_user.id, can_send_messages=False,
                                 can_send_media_messages=False, can_send_other_messages=False,
                                 can_add_web_page_previews=False)
	
# DICHIARAZIONE FUNZIONI
def init(bot, update):
    admin(bot, update)
    welcome(bot, update)
    okgoogle(bot, update)
    buongiorno(bot, update)
    buonanotte(bot, update)
    say(bot, update)
    nexus5x(bot, update)
    definisci(bot, update)
# cancellacomandi(bot, update)
