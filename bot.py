#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config, commands, handler

# Questo abilita i log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    logger.warning('Update "%s" genera errore: "%s"', update, context.error)

# Questa è la funzione che inizializza il bot
def main():
    updater = Updater(config.bot_token)
    dp = updater.dispatcher

    # Qui "creo" i comandi e assegni una funzione
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help))
    dp.add_handler(CommandHandler("regole", commands.regole))
    dp.add_handler(CommandHandler("parse", commands.parse))
    dp.add_handler(CommandHandler("source", commands.source))
    # Comandi

    # Qui richiamo le funzioni senza comando, =>handler
    dp.add_handler(MessageHandler(None, handler.init))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
