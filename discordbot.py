from discord.ext import commands
import discord
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
       embed = discord.Embed(title="リンク集",description=f"メッセージのURLは [こちら]({message.jump_url}) をクリックしてください。")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(embed=embed)
        
bot.run(token)
