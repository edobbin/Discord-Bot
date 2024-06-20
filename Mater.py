import os
from typing import Final
import dotenv
import time
import discord
from discord.ext import commands
#import youtube_dl

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='%', intents=intents)

#bot = commands.Bot(command_prefix='%')


dotenv.load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
USER_ID: Final[int] = int(os.getenv('USER_ID'))
CHANNEL_ID: int = int(os.getenv('CHANNEL_ID'))
GUILD: Final[int] = int(os.getenv('GUILD_ID'))


@bot.event
async def on_ready():
    print(f'{bot.user} is now running at')
    g = bot.get_guild(GUILD)
    print(f"Opening sever {g}")

    channel = g.get_channel(CHANNEL_ID)

    print(f"Entering channel {channel}")
    await channel.send(f"{g.get_member(bot.user.id)} is now online")
    halfbreed = g.get_member(707580902900891668)
    await channel.send(f"Good afternoon <@{halfbreed.id}>")


@bot.event
async def on_message(message : discord.Message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')
    if message.content.split(' ')[0] =='Almighty' and message.content.split(' ')[1] == 'Mater':
        await message.channel.send(f'Yes, @{discord.Member.name}')

    await bot.process_commands(message)

@bot.event
async def send_message(message: discord.Message):
    if message.author == bot.user:
        return
    print('MESSAGE pending')

    if not user_message:
        print('MESSAGE WAS EMPTY')
        return
    try:
        response: str = "ALL PRAISE MATER"
        await message.author.send(response)
    except Exception as e:
        print(e)
        
async def speak():
    print()

# @bot.command()
# async def hello(ctx):
#     await ctx.send("Hello friends")
# @bot.command()
# async def bye(ctx):
#     await ctx.send("Goodbye")




# def main() -> None:
#     client.run(TOKEN)

# if __name__ == '__main__':
#     main()

# CHATGPT CODE
# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
    
#     # Get the channel by ID
#     channel = client.get_channel(CHANNEL_ID)
#     print(f'Channel: {channel}')  # Log the channel object
    
#     # Check if the channel exists
#     if channel:
#         try:
#             await channel.send("Hello, this is a test message!")
#             print("Message sent successfully!")
#         except discord.HTTPException as e:
#             print(f'Failed to send message: {e}')
#     else:
#         print("Channel not found")
        
        
bot.run(TOKEN)
