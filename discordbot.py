import discord
from discord.ext import commands
import traceback
import os
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
LOG_CHANNEL_ID = 786696510439817226
BROADCASTIN_CHANNEL_ID = 786757394754568233
BROADCASTOUT_CHANNEL_ID = 786664256040730674
INTRODUCE_CHANNEL_ID = 786661109247115285
LOBBY_CHANNEL_ID = 786664600967315504
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メッセージ1
    #embed = discord.Embed(title="リンク集",description=f"メッセージのURLは [こちら]({message.jump_url}) をクリックしてください。")
    if message.channel.id == BROADCASTIN_CHANNEL_ID:
        if message.content[:3] == "YKZ":
            bchannel = bot.get_channel(BROADCASTOUT_CHANNEL_ID)
            await bchannel.send(message.content[3:])
            return 
        elif message.content[:3] == "TRI":
            ichannel = bot.get_channel(INTRODUCE_CHANNEL_ID)
            await ichannel.send(message.content[3:])
            return 
        else:
            await message.channel.send("放送に失敗しました。先頭にYKZを入れることで放送できます。")
            return 
    category = ''
    if message.channel.category_id:
        category = bot.get_channel(message.channel.category_id).name + ' '
    title = '[' + category + message.channel.name + '] ' + message.author.name
    # embed = discord.Embed(title=title,description=f"[メッセージへ]({message.jump_url})")    
    embed = discord.Embed(title=title,description= message.content + "\n" + f"[jump]({message.jump_url})")
    channel = bot.get_channel(LOG_CHANNEL_ID)
    await channel.send(embed=embed)
        
bot.run(token)
