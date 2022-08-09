from replit import db

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
