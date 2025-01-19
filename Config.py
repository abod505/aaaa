from pyrogram import Client, enums
import os
from Utils.database import Database

# Bot Config
class config:
    API_KEY : str = "7641107003:AAH5Uswd5AkyFptq1XAMnvHrcliu1p4q0Wk" # The API key or Bot Token
    API_HASH: str = "4n4sxxxxxxxxxxxxxxxxx" # UserBot Api Hash
    API_ID  : int = 1234500 # User Bot Api Id
    SUDO    : int = 5260517001 # Sudo Id

# Check Bot Directory
if not os.path.exists('./.session'): # Sessions File
    os.mkdir('./.session')

if not os.path.exists('./database'): # Databases File
    os.mkdir('./database')

# Get Database
database = Database()

# Temp status
temp = {'broadcast': False}

# Start Pyrogram Client (using bot_token for initial start)
app = Client(
    name="./.session/rad", 
    bot_token=config.API_KEY, 
    plugins=dict(root="Plugins"), 
    parse_mode=enums.ParseMode.DEFAULT
)

# Run the client to start the bot
app.start()

# Now you can initialize UserBot with API_ID and API_HASH if needed
userbot = Client(
    session_name="./.session/userbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

# Run the userbot client (if you're using it for extra functionalities)
userbot.start()
