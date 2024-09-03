from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait, AccessTokenExpired
import asyncio 
from Utils.testing_plugin import USERDATE_TYPE_LIST, TETSING_INFO, CHACK_USERNAME, CHACK_CH
from config import CONFIG,LIST_TEMP, Temp_data
from Plugins.plug import LANCH_TETSING


async def TETSING_BOT(API_KEY: str,TOEKN_ID: int,  LIST_ID: list, message_id : str | int, chat_id: str | int):
    # Preparation Testing Vals
    USERNAME_LIST = LIST_TEMP[LIST_ID]
    DONE_USER = []
    USERDATE_TYPE = USERDATE_TYPE_LIST
    CH_INFO = TETSING_INFO
    # TETSING MESSAGE LADNSH
    await LANCH_TETSING(CH_INFO,LIST_ID, None, None, TOEKN_ID,message_id, chat_id, 'Looding ..' )
    # start Pyrogram bot Client 
    app = Client('::memory::', api_id=CONFIG['API_ID'], api_hash=CONFIG['API_HASH'], bot_token=API_KEY, in_memory=True)
    
    try:
        await app.start()
    except AccessTokenExpired as err:
            await LANCH_TETSING(CH_INFO,LIST_ID, username, None,TOEKN_ID,message_id, chat_id, f'BAND TOKEN ❲ {TOEKN_ID} ❳ ✗.' )
            return USERDATE_TYPE, CH_INFO, {'STATES':'FLOOD','SEC':seconds, 'DONE_USERNAME':DONE_USER}
        
    # START LOOPS 
    for ii, username in enumerate(USERNAME_LIST):
        if Temp_data['checker_stat'] == False:
                await LANCH_TETSING(CH_INFO,LIST_ID, username, None,TOEKN_ID,message_id, chat_id, 'STOP .' )
                return USERDATE_TYPE, CH_INFO, {'STATES':'FLOOD','SEC':seconds, 'DONE_USERNAME':DONE_USER} 
        DONE_USER.append(username)
        CH_INFO['DC']+=1
        # Check values
        if not username:
            CH_INFO['UNOT']+=1 
            continue 
        # Check user in telegram 
        if CHACK_USERNAME(username) == True:
            CH_INFO['UNOT']+=1
            continue
        
        if CHACK_CH(username) == True:
            CH_INFO['CH']+=1
            continue
        # Get FUll USername 

        try:
            userdata = await app.get_users([username])
        except FloodWait as Err:
            CH_INFO['ERR']+=1
            # DONE_USER.remove(username)
            seconds = Err.value
            if seconds > 200:
                await LANCH_TETSING(CH_INFO,LIST_ID, username, None,TOEKN_ID,message_id, chat_id, f'FLOOAD TOKEN ❲ {TOEKN_ID} ❳ ✗.' )
                return USERDATE_TYPE, CH_INFO, {'STATES':'FLOOD','SEC':seconds, 'DONE_USERNAME':DONE_USER}                 
            await asyncio.sleep(seconds)
            continue
        except Exception as Err:
            print(Err)
            CH_INFO['ERR']+=1
            continue
        # User Type Channls 
        if not userdata :
            print('CHH')
            CH_INFO['CH']+=1
            continue

        USERDATE_TYPE[userdata[0].status].append(username)
        CH_INFO['OK']+=1
        print(f'{ii}: {username} |' + str(userdata[0].status))
        await LANCH_TETSING(CH_INFO,LIST_ID, username, str(userdata[0].status),TOEKN_ID,message_id, chat_id, 'Testing ➹ .. ' )
    await LANCH_TETSING(CH_INFO,LIST_ID, username, None,TOEKN_ID,message_id, chat_id, 'DONE TETSING ✓.' )

    return USERDATE_TYPE, CH_INFO, {'STATES':'DOONE','SEC':0, 'DONE_USERNAME':DONE_USER}    

        