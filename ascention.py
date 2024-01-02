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
dbase.execute('pragma journal_mode=wal')
print('Database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS user_info(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT NOT NULL,
    USER_ID TEXT NOT NULL,
    COMMAND TEXT NOT NULL,
    CHANNEL TEXT NOT NULL) ''')

print('Table created')

def insert_user_info(USERNAME,USER_ID,COMMAND,CHANNEL):
    dbase.execute('''INSERT INTO user_info (USERNAME,USER_ID,COMMAND,CHANNEL)
            VALUES (?,?,?,?)''',(USERNAME,USER_ID,COMMAND,CHANNEL))

    dbase.commit()
    print('New user info inserted')
    
#bot setup
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


#bot commands
@client.event
async def on_message(message):

    USERNAME = str(message.author)
    CHANNEL = message.channel.id
    USER_ID =  message.author.id

    if message.content.startswith('>sandwich'):
        insert_user_info(USERNAME,USER_ID,'>sandwich',CHANNEL)

    elif message.content.startswith('>imgen'):
        insert_user_info(USERNAME,USER_ID,'>imgen',CHANNEL)

    elif message.content.startswith('>hello'):
        await message.channel.send('Привет, я - бот, разработанный Singularity с целью научиться работать с api discord.py для продвижения его скиллов в Python!')
#    elif message.content.startswith('>help'):

    elif message.content.startswith('>sketch'):
        insert_user_info(USERNAME,USER_ID,'>sketch',CHANNEL)

client.run(discord_token)
