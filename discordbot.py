from discord.ext import commands
import os
import traceback
import logging
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

global CHANNEL_ID = 786716037718474752

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if  == '/aiueo':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('メッセージ')
        
async def handle_channel(c):
    CHANNEL_ID = c

bot.run(token)
