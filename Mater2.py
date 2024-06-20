import discord
from discord.ext import commands
from typing import Final
import os

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN: Final[str] = os.getenv('TOKEN_ID')

# Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to send the message to
CHANNEL_ID: Final[str] = os.getenv('CHANNEL_ID')  # Example channel ID, replace with your actual channel ID

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('Hello, World!')
    else:
        print(f'Could not find channel with ID {CHANNEL_ID}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)  # Process commands after handling the message

@bot.command()
async def greet(ctx):
    await ctx.send('Hello!')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

# Start the bot
bot.run(TOKEN)
