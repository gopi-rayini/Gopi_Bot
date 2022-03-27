import discord
import os
import json
import requests
from replit import db
from keep_alive import keep_alive
from time import sleep
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
guild=client.guilds
prefix='$'

# # # API Methods

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_fact():
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.loads(response.text)
  fact = json_data['quote'] + " -**" + json_data['character'] + '**, *' + json_data['anime'] + '*'
  return (fact)

def get_joke():
  r = requests.get("https://v2.jokeapi.dev/joke/Any")
  j = json.loads(r.text)
  joketype = j['type']
  if(joketype=='twopart'):
      joke = j['setup'] + '  **' + j['delivery'] + '**'
  else:
      joke = j['joke']
  return joke

# Weather Methods
def get_weather(info):
  #API Call
  r = requests.get("https://www.7timer.info/bin/civil.php?lon=-74.44&lat=40.36&ac=0&unit=british&output=json&tzshift=0")
  j = json.loads(r.text)
  series = j['dataseries']

  if(info=="date"):
    date = (int)(j['init'])
    date = (int)(date/100)
    day = date%100
    month = ((int)(date/100))%100
    return ((str(month)+ "/" + (str)(day)))
  
  if(info=="temp"):
    temp = []
    for x in series:
      temp.append(x['temp2m'])
    return temp

  if(info=="weather"):
    weather = []
    for x in series:
      weather.append(x['weather'])
    return weather

  if(info=="precip"):
    prec = []
    for x in series:
      if(x['prec_type'] is not None):
        prec.append(x['prec_type'])
    return prec

  if(info=="init"):
    init = ((int)(j['init']))%100
    return (init-4)

def update_prefix(char):
  db["prefix"] = char

def add_name(name):
    namelist = db["name"]
    namelist.append(name)
    db["name"] = namelist

def checkName(msg):
  if (msg==('joe' or 'Joe')):
    return('**Joe** is a fantastic gamer. Just needs to work on communication, aim, map awareness, crosshair placement, economy management, pistol aim, awp flicks, grenade spots, smoke spots, pop flashes, positioning, bomb plant positions, retake ability, bunny hopping, spray control and getting a kill.')

  if (msg==('raven' or 'Raven')):
    return('**Raven**: I am loli maid with cat ears. Smol, cute, and very smol. Am like 3ft 4in. Anyways, give me headpats')

  if (msg==('gopi' or "Gopi")):
    return("**Gopi** : I'm the owner of this bot, bitch")

  if (msg==('xinyi' or 'Xinyi')):
    return("**Xinyi**: 我有最大的阴茎")

  if (msg==('justin' or 'Justin' or 'jj')):
    return("**JJSLAYIN**: I only play games that require 3000+ hours to get 1 item.")

  if (msg==('ariana' or 'Ariana')):
    return("**Ariana**: I am Ariana Pequeno.")

  else:
    return "NA"   


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
    update_prefix(char)
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

    if(checkName(msg)!="NA"):
      await message.channel.send(checkName(msg))

    if (msg=='dq' or msg=='daily'):
      quote = get_quote()
      await message.channel.send(quote)

    if (msg=='af' or msg=='fact'):
      fact = get_fact()
      await message.channel.send(fact)

    if (msg=='joke'):
      joke = get_joke()
      await message.channel.send(joke)
    
    if(msg=='forecast'):
      date = get_weather("date")
      temp = get_weather("temp")
      init = get_weather("init")
      hour = init + 3
      weather = get_weather("weather")
      text = '```' + "--- Start Date - " + date + " ---"
      text = text + '\n' + "{:<15} {:<15} {:<15}".format("Hour", "Temp (F)", "Condition")
      for x in range(0,(int)(len(temp)/4)):        
        text = text + '\n' + "{:<15} {:<15} {:<15}".format( (str)(hour), (str)(temp[x]), (str)(weather[x]))
        hour+=3
        if(hour>24):
          hour-=24
          text = text + '\n\n' + "<<< ----- Next Day ----- >>>"
          text = text + '\n' + "{:<15} {:<15} {:<15}".format("Hour", "Temp (F)", "Condition")
      await message.channel.send(text + "```")

    if(msg=='event'):
      split = msg.split(' ')
      await message.channel.send(split)


# Server Aliving

keep_alive()
client.run(os.getenv('TOKEN'))