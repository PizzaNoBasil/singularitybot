import os
import requests
from dotenv import load_dotenv
import discord
import json
from discord.ext import commands

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
stable_diffusion_token = os.getenv('STABLEDIFFUSION_TOKEN')

sandwich_result = '/tmp/sandwich.png'

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

def assign_queue():
    queue_indicator = 0
    user_queue = queue_indicator += 1
    return user_queue

def get_username():
    username = {message.author}
    return username
#user_info = {
 #   "queue_position": user_queue,
  #  "username": {user}

bot_queue = [{
    "queue_position": user_queue,
    "username": user_name,
    "command": user_command
}]

@client.event
async def commands_processing(message):
    if msg.startswith('>sandwich'):
        with open("bot_queue.json", "w") as write_file:
            json.dump(data, write_file)
    elif msg.startswith('>imgen'):
        with  open("bot_queue.json", "w") as write_file:
            json.dump(data, write_file)
    elif msg.startswith('>hello'):
        with  open("bot_queue.json", "w") as write_file:
            json.dump(data, write_file)
    elif msg.startswith('>info'):
        with  open("bot_queue.json", "w") as write_file:
            json.dump(data, write_file)
    elif msg.startswith('>sketch'):
        with  open("bot_queue.json", "w") as write_file:
            json.dump(data, write_file)
client.run(discord_token)

