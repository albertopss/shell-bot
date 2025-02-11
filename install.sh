#!/bin/bash
if (( $UID != 0 )); then
    echo "$0 needs sudo privilegies"
    exit 99
fi

# Check the bot token
echo "Checking your Telegram Bot API token........... " 

# Check if the bot token is empty
if [ ! -s "$TELEGRAM_BOT_TOKEN" ]; then
    echo "Telegram bot token found..."
    
fi

# Update and install dependencies
echo "Updating system and installing dependencies..."
#sudo apt-get update -y
#sudo apt-get upgrade -y
#sudo apt-get install -y python3 python3-pip python3-venv git cowsay

# Create a project directory
cowsay "Creating project directory..."
mkdir ~/telegram_bot
cd ~/telegram_bot

# Create a virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
#pip install --upgrade pip
#pip install telepot

# Execute Python bot on a subshell
echo "Loading python bot..."
python3 /mnt/c/Users/pepe_/OneDrive/Escritorio/shell-bot-1/telegram_bot.py &

#Check status
if [[ $? -eq 0 ]]; then
    cowsay "Running successful on the background"
else
    cowsay "Some error has occurred"
    exit 134
fi

# Make the script executable
echo "Check permissions"
#chmod +x telegram_bot.py

# Instructions for the user
echo "Installation complete."
echo "To run your Telegram bot, use the following command:"
echo "  python3 telegram_bot.py"

# Final step
echo "Bot setup completed. To run the bot, make sure to activate the virtual environment and execute the bot script."
echo "Run the following commands:"
echo "  source venv/bin/activate  # Activate the virtual environment"
echo "  python3 telegram_bot.py  # Start the Telegram bot"

# End of script
exit 0
