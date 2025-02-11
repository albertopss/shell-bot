import os
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# FIFO file path
FIFO_PATH = "/home/alberto/shell-bot-1/keywords.log.txt"  # Change this to the path of your FIFO file

# Telegram bot token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Function to send a message to the user
def send_fifo_data(update: Update, context: CallbackContext) -> None:
    try:
        # Open the FIFO file in read mode (blocking)
        with open(FIFO_PATH, "r") as fifo:
            # Continuously check for new data in the FIFO file
            while True:
                # Read new data from the FIFO (it will block until data is available)
                data = fifo.readline()
                if data:
                    # Send the read data to the user
                    update.message.reply_text(data.strip())
                time.sleep(1)  # Optional: Adjust the delay as needed
    except FileNotFoundError:
        update.message.reply_text("FIFO file not found. Please ensure it's created correctly.")
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I will start sending data from the FIFO file to you when available.")

def main():
    # Create the Updater and Dispatcher objects
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Add a custom command handler to start reading from FIFO
    dispatcher.add_handler(CommandHandler("read_fifo", send_fifo_data))

    # Start polling for updates
    updater.start_polling()

    # Run the bot until manually stopped
    updater.idle()

if __name__ == '__main__':
    main()

