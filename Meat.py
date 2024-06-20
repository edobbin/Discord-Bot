import discord
import os
from typing import Final
import dotenv
import schedule
import time
import asyncio
import requests

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='~', intents=intents)

TOKEN: Final[str] = os.getenv('MEAT_TOKEN')
SERVER_ID: Final[str] = os.getenv('GUILD_ID')

server = client.get_guild(SERVER_ID)

print(server)


@bot.event
async def on_ready():
    print(f'{bot.user} is now running at')


async def send_script():
    await client.wait_until_ready()
    print("Sending scripture")


def get_Verse():
    url = ''


bot.run(TOKEN)