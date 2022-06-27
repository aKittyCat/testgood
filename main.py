import os
import discord
from discord.ext import commands
from decouple import config


client = commands.Bot(command_prefix="@")

@client.event
async def on_ready():
  print("Ragnarok.")


for filename in os.listdir('./commands'):
  if filename.endswith('.py'):
    client.load_extension(f'commands.{filename[:-3]}')  
  
TOKEN=config('OTkwNzQzODUwODE1NDYzNDg0.G-A-Ga.jsC5JsV-PB5yjZ9OUCjUDXfj0qz2v6Rdu9Ja0s')
client.run(OTkwNzQzODUwODE1NDYzNDg0.G-A-Ga.jsC5JsV-PB5yjZ9OUCjUDXfj0qz2v6Rdu9Ja0s)
