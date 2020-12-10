from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

groval CHANNEL_ID = 786716037718474752

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if  == '/aiueo':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('[' + message.channel + ']' + message.name + ':' + message.name)
        
async def handle_channel(c)
    CHANNEL_ID = c

bot.run(token)
