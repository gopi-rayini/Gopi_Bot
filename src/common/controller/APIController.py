import discord
import os
import json
import requests
from persistent import keep_alive
from time import sleep
from datetime import datetime
from ..Methods import APIService

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
guild=client.guilds
prefix='$'


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('gently ;)'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  # Get Message + Prefix
  prefix = db["prefix"]
  msg=message.content

  # Don't read bot's own messages
  if message.author == client.user:
    return

  # User Message Counter
  try:
    db[(str)(message.author.id)] += 1
  except:
    db[(str)(message.author.id)] = 0
    
  # Prefix Set
  if message.content.startswith(prefix+'prefix'):
    char = msg.split(prefix+'prefix ',1)[1]
    APIService.update_prefix(char)
    await message.channel.send("Prefix updated to "+char)

  if message.content.startswith(prefix):
    # Parse command only without prefix
    msg = message.content.replace(prefix, '', 1)

    # Run Commands
    if (msg=='help'):            
      await message.channel.send("**Commands are:**")
      await message.channel.send("*dq* - Daily Quotes")
      await message.channel.send("*af* - Anime Quotes/Facts")
      await message.channel.send("*joke* - Jokes")
      await message.channel.send("*joe, raven, gopi, xinyi, justin, or ariana* - Misc")

    if (msg=='msg'):
      await message.channel.send('Hey <@'+ (str)(message.author.id) + '>, you have sent ' + (str)(db[(str)(message.author.id)]) + ' messages!')

    if(APIService.checkName(msg)!="NA"):
      await message.channel.send(APIService.checkName(msg))

    if (msg=='dq' or msg=='daily'):
      quote = APIService.get_quote()
      await message.channel.send(quote)

    if (msg=='af' or msg=='fact'):
      fact = APIService.get_fact()
      await message.channel.send(fact)

    if (msg=='joke'):
      joke = APIService.get_joke()
      await message.channel.send(joke)

    if (msg=='cf' or msg=='catfact'):
      await message.channel.send(APIService.cf())
    
    if(msg=='event'):
      split = msg.split(' ')
      await message.channel.send(split)


# Server Aliving

keep_alive()
client.run(os.getenv('TOKEN'))