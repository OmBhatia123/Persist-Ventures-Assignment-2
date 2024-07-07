from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Application, ContextTypes
from selenium_automation import create_wallet, post_comment

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello! I am your crypto trading bot.")

async def comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wallet_address = create_wallet()
    post_comment(wallet_address)
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Automated comment posted.")

async def group_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Check out this new trading bot: https://www.google.com"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '7286211720:AAEuS_bX1af3L6GPAZuaEjYP_hdXuaAJmW8'
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("comment", comment))
    application.add_handler(CommandHandler("groupmessage", group_message))

    application.run_polling()

if __name__ == '__main__':
    main()

