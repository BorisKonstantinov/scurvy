from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

# Load environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

# Add command registration and other setup code here if needed

# This file is intentionally left blank.