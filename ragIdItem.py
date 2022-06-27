import requests
import json
import re
from decouple import config

def checkItemId(id, server='thRO'):
  apiKey = config('aeba153ed40c8705466f30b8783849bd')
  try:
      url = f'https://www.divine-pride.net/api/database/Item/{id}?apiKey={apiKey}'
      r = requests.get(url)
      r = json.loads(r.content)
      desc = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['description'])
      name = re.sub(r'\^([0-9A-Fa-f]{6})', '', r['name'])
      return name
  except:
    return "Could not locate the monster."
    
