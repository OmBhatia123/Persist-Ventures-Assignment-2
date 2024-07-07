from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from selenium_automation import create_wallet, post_comment

TOKEN = '7286211720:AAEuS_bX1af3L6GPAZuaEjYP_hdXuaAJmW8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your crypto trading bot.')

def automate_comment(update: Update, context: CallbackContext) -> None:
    wallet_address = create_wallet()
    if wallet_address:
        post_comment(wallet_address)
        update.message.reply_text('Automated comment posted.')
    else:
        update.message.reply_text('Failed to create a wallet.')

def join_group_and_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message = "Check out this new trading bot: https://www.google.com"
    context.bot.send_message(chat_id=chat_id, text=message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('comment', automate_comment))
    dispatcher.add_handler(CommandHandler('groupmessage', join_group_and_message))

    updater.start_polling()
    updater.idle()
