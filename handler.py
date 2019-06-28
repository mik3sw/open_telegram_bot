from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#DEFINIZIONE COMANDI ADMIN
from functools import wraps

LIST_OF_ADMINS = [38201859]


def restricted(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for [{}][{}].".format(user_id, update.message.from_user.username))
            return
        return func(bot, update)
    return wrapped

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
			bot.send_message(-1001323415459,
                 text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\nAutore: {username}\n<code>Messaggio:{}</code>"
					 .format(var_messaggio, username=update.message.from_user.username,),
                 parse_mode='HTML')

#RISPOSTE DI Gassistant
def okgoogle(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower() == "ok google":
			bot.send_message(update.message.chat_id, "Ciao {name}, come posso aiutarti?".format(name=update.message.from_user.first_name))

def nexus5x(bot, update):
	if update.message.text is not None:
		if 'nexus 5x' in str(update.message.text).lower():
			bot.send_message.reply_text('Do you want some bootloop?')
#Buongiorno
def buongiorno(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buongiorno"):
			bot.send_message(update.message.chat_id, "Buongiorno {username}".format(username=update.message.from_user.username))
#Buonanotte
def buonanotte(bot, update):
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("buonanotte"):
			bot.send_message(update.message.chat_id, "Buonanotte {username}".format(username=update.message.from_user.username))
			

#BENVENUTO
def welcome(bot, update):
	for new in update.message.new_chat_members:
		update.message.reply_text("Benvenuto {username} in {chat_title}!\n"
								  "Ti preghiamo di rispettare le /regole per non ricevere sanzioni\n"
								  "Buona permanenza!\n\n<em>- lo staff</em>".format(
			username = "@"+new.username,
			chat_title = update.message.chat.title
			), parse_mode='HTML')


@restricted
def say(bot, update):
	pass
	if update.message.text is not None:
		if update.message.text.startswith("/say"):
			var_messaggio = update.message.text
			var_messaggio = var_messaggio.replace("/say", "")
			bot.send_message(update.message.chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')


#DICHIARAZIONE FUNZIONI
def init(bot, update):
	admin(bot, update)
	welcome(bot, update)
	okgoogle(bot, update)
	buongiorno(bot, update)
	buonanotte(bot, update)
	say(bot, update)
	#cancellacomandi(bot, update)



	
	