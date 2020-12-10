from discord.ext import commands
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 786716037718474752
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    await message.channel.send('メッセージ1')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('メッセージ2')
        
bot.run(token)
