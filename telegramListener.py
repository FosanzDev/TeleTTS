from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram import Update
import os
from ttsConnector import TTSConnector

ttsConnector = TTSConnector(os.environ["OPENAI_API_KEY"])

async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    filepath = await ttsConnector.synth(message)
    await context.bot.send_voice(chat_id=update.message.chat_id, voice=open(filepath, "rb"))
    os.remove(filepath)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm a bot that converts text to speech. Send me a message and I'll convert it to speech for you.")


if __name__ == '__main__':
    # Create the application
    application = ApplicationBuilder().token(os.environ["TELETTS_TOKEN"]).build()

    # Register the on_message function to handle messages
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), on_message, block=False))

    application.run_polling()