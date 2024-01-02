import os
import requests
from dotenv import load_dotenv
import discord
from discord.ext import commands
import sqlite3
import json

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


def read_data(dbase):
   data = dbase.execute("SELECT * FROM user_info ORDER BY ID;")
   for record in data:
        return(str(record[1]), str(record[2]), str(record[3]), str(record[4]))

#bot setup
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

#stablediffusion image processing
#>sandwich
def sandwich():
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
    "key": stable_diffusion_token,
    "prompt": "сендвич с"+ sandwich_ingredients,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "yes",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print("Recieved image response, parcing in progress", response.text)

#>imgen
def imgen():
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
    "key": stable_diffusion_token,
    "prompt": usermetadata,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "yes",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print("Recieved image response, parcing in progress", response.text)

#command processing
read_data(dbase)



#bot commands
@client.event
async def on_message(message):

    USERNAME = str(message.author)
    CHANNEL = message.channel.id
    USER_ID =  message.author.id

    if message.content.startswith('>sandwich'):
        insert_user_info(USERNAME,USER_ID,message.content,CHANNEL)
        await message.channel.send("<@" + str(USER_ID) + ">" " ваш запрос принят, ожидайте")

#    elif message.content.startswith('>imgen'):
#        insert_user_info(USERNAME,USER_ID,message.content,CHANNEL)
#        await message.channel.send("<@" + str(USER_ID) + ">" " ваш запрос принят, ожидайте")

    elif message.content.startswith('>hello'):
        await message.channel.send('Привет, я - бот, разработанный Singularity с целью научиться работать с api discord.py для продвижения его скиллов в Python!')

    elif message.content.startswith('>help'):
        await message.channel.send('В данный момент бот знает следующие команды: \n *>sandwich [ingredients]* - команда для генерации сендвича по заданным пользователем параметрам.\n *>imgen [prompt]* - команда для генерации изображения по заданным пользователeм параметрам.\n *>hello* - eсли хотите сказать привет боту.\n *>help* - для выведения информации о доступных коммандах.\n *>sketch [prompt]* - комманда для помощи игрокам в sketch heads, сгенерирует изображение заданное пользователем и даст его определение.')

#    elif message.content.startswith('>sketch'):
#        insert_user_info(USERNAME,USER_ID,message.content,CHANNEL)
#        await message.channel.send("<@" + str(USER_ID) + ">" " ваш запрос принят, ожидайте")

client.run(discord_token)
