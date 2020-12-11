import discord
from discord.ext import commands
import traceback
import os
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 786716037718474752
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メッセージ1
    await message.channel.send('メッセージ1_')
    #embed = discord.Embed(title="リンク集",description=f"メッセージのURLは [こちら]({message.jump_url}) をクリックしてください。")
    
    category = ''
    if message.channel.category_id:
        await message.channel.send('メッセージ1.25')
        category = bot.get_channel(message.channel.category_id).name
    title = category + ' ' + message.channel.name + ' ' + message.author.name
    # embed = discord.Embed(title=title,description=f"[メッセージへ]({message.jump_url})")    
    embed = discord.Embed(title=title,description= message.content + f"[jump]({message.jump_url})")    
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(embed=embed)
        
bot.run(token)
