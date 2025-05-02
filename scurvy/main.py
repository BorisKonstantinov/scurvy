import os
import discord
from discord.ext import commands
from utils.database import Database

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration
TOKEN = os.getenv('DISCORD_TOKEN')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Initialize the bot
bot = commands.Bot(command_prefix='!')

# Connect to the MySQL database
db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Load commands
for filename in os.listdir('./bot/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Run the bot
bot.run(TOKEN)