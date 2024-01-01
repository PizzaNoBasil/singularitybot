import os
import requests
from dotenv import load_dotenv
import discord
from discord.ext import commands
import sqlite3

#getting tokens
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
stable_diffusion_token = os.getenv('STABLEDIFFUSION_TOKEN')

#results storage path
sandwich_result = '/tmp/sandwich.png'

#sqlite db shit
dbase = sqlite3.connect('singlbot.db')
print('Database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS user_info(
    ID INT PRIMARY KEY NOT NULL,
    USERNAME TEXT NOT NULL,
    USER_ID TEXT NOT NULL,
    COMMAND NOT NULL,
    CHANNEL NOT NULL) ''')

print('Table created')

def insert_user_info(ID,USERNAME,USER_ID,COMMAND):
    db.execute(''' INSERT INTO user_info(ID,USERNAME,USER_ID,COMMAND,CHANNEL
            VALUES(?,?,?,?,?)''',(ID,USERNAME,USER_ID,COMMAND,CHANNEL))

    dbase.commit()
    print('New user info inserted')

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


#@bot.command()
#async def sandwich

ID = 0

@client.event
async def on_mesage(ctx, message):
    if message.content.startswith('>sandwich'):
        ID += 1
        USERNAME = message.author
        CHANNEL = message.channel
        USER_ID =  message.author.id
        insert_user_info(ID,USERNAME,USER_ID,'>sandwich',CHANNEL)
#    elif message.content.startswith('>imgen'):
#        client_id += 1
#        username = message.author
#        
#    elif message.content.startswith('>hello'):
#        client_id += 1
#        username = message.author
#        
#    elif message.content.startswith('>help'):
#        client_id += 1
#        username = message.author
#        
#    elif message.content.startswith('>sketch'):
#        client_id += 1
#        username = message.author
#        
    else:
        return

client.run(discord_token)
