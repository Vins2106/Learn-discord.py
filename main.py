import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print(f"{client.user} is ready!")

@client.event
async def on_message(message):
  if message.content.startswith(".test"):
    await message.channel.send(f"Hai {message.author.nick}")

token = os.environ['token']
client.run(token)