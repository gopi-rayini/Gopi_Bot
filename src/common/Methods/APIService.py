import json
import requests
from time import sleep


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

def cf():
  r = requests.get("https://catfact.ninja/fact")
  j = json.loads(r.text)
  return j["fact"]