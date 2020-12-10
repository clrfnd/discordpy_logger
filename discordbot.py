from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

groval noticechannel

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if  == '/aiueo':
        await '[' + message.channel + ']' + message.name + ':' + message.name
        
async def handle_channel(c)
    noticechannel = c

bot.run(token)
