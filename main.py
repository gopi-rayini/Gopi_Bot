import discord
import os
import json
import requests
from replit import db
from keep_alive import keep_alive
from time import sleep

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
guild=client.guilds
prefix='$'
commands = {}

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
    msg=message.content
    prefix = db["prefix"]

    await message.channel.send(message.author) 
    if message.author == client.user:
        return

    if message.content.startswith(prefix+'prefix'):
        char = msg.split(prefix+'prefix ',1)[1]
        update_prefix(char)
        await message.channel.send("Prefix updated to "+char)

    if message.content.startswith(prefix):

        #Parse command only without prefix
        msg = message.content.replace(prefix, '', 1)

        if (msg=='help'):            
            await message.channel.send("**Commands are:**")
            await message.channel.send("*dq* - Daily Quotes")
            await message.channel.send("*af* - Anime Quotes/Facts")
            await message.channel.send("*joke* - Jokes")
            await message.channel.send("*joe, raven, gopi, xinyi, justin, or ariana* - Misc")

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
        
        if(msg=='cmdadd'):
            commands.add()

keep_alive()
client.run(os.getenv('TOKEN'))