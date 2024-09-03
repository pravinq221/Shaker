
# Requiere Module .
from pyrogram import Client, enums
import json
import os 
# Requiere Bot Plugin 
from Utils.databesas import  Datat

CONFIG = json.load(open('config.json', 'r'))

if not os.path.exists('./data'):
    os.mkdir('./data')

if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.temp'):
    os.mkdir('./.temp')

datat = Datat()
## Temps Data 
Temp_data = {
    'checker_stat':False,
    'LIST_CHECKER_ID':None,
    'ON_MESSAGE':None,
    'ADD_ACCONET':False,
    'ADD_TOKEN':False}

LIST_TEMP = {}

app = Client(
    name='./.session/rad',
    bot_token=CONFIG['API_KEY'],
    api_hash=CONFIG['API_HASH'],
    api_id=CONFIG['API_ID'], 
    parse_mode=enums.ParseMode.DEFAULT, 
    plugins=dict(root='Plugins')
)



