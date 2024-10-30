import time
import telegram
from datetime import datetime
from telegram.ext import Updater, CommandHandler

# Replace these with your actual chat ID and bot token
CHAT_ID = "6972382984"
API_TOKEN = "7228147192:AAEg1GtZGTGSr_uag1BMi2V6hwytNBBYb8o"

# Initialize the updater and dispatcher
updater = Updater(token=API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    """Sends a message when the /start command is issued."""
    update.message.reply_text("Bot is alive and running!")

def send_vps_status(context):
    """Sends a VPS status message every 26 minutes."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vps_status = "VPS is currently ON"  # Replace with logic to check real status if needed
    context.bot.send_message(chat_id=CHAT_ID, text=f"Status at {now}: {vps_status}")

def main():
    # Set up the /start command
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    # Schedule VPS status updates every 26 minutes
    updater.job_queue.run_repeating(send_vps_status, interval=26 * 60, first=0)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
