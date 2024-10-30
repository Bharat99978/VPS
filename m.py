import time
import telegram
from datetime import datetime

# Replace these with your actual chat ID and bot token
CHAT_ID = "6972382984"
API_TOKEN = "7228147192:AAEg1GtZGTGSr_uag1BMi2V6hwytNBBYb8o"

# Initialize the bot
bot = telegram.Bot(token=API_TOKEN)

def send_vps_status():
    while True:
        # Get the current time and set the status message
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vps_status = "VPS is currently ON"  # Replace this logic if you want to dynamically check VPS status

        # Send the status message
        bot.send_message(chat_id=CHAT_ID, text=f"Status at {now}: {vps_status}")

        # Wait for 26 minutes before the next message
        time.sleep(26 * 60)

if __name__ == "__main__":
    send_vps_status()
