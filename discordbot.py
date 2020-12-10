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
    # メッセージ1
    await message.channel.send('メッセージ1')
    text = f'{new_channel.mention} を作成しました'
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('( #' + message.channel.name + ' ' + message.author.name + 'さん)' + message.content)
        
bot.run(token)
