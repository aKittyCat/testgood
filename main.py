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
  
TOKEN=config('OTkwNzQzODUwODE1NDYzNDg0.GC8N6f.eofE1v7_FbfMuJ2knC0dn5GlQxivg69IklX4ps')
client.run(OTkwNzQzODUwODE1NDYzNDg0.GC8N6f.eofE1v7_FbfMuJ2knC0dn5GlQxivg69IklX4ps)
