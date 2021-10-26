from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
import constants as keys
import responses as R

print("Bot just started")

def start_command(update: Update, context):
    update.message.reply_text('Type something to get started!')

def help_command(update: Update, context):
    update.message.reply_text('Go googling!')

def handle_message(update: Update, context):
    text = str(update.message.text).lower()
    res = R.responses(text)
    update.message.reply_text(res)

def error_handling(update: Update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error_handling)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()