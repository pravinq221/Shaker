from config import datat, LIST_TEMP
from Utils.Testing import *
from Plugins.function import FILTER_USERNAME_LIST, CROVET_USERDATE_TYPE_LIST, TEMP_FILE, Send_Document


async def TETSING_HANDLER(LIST_ID: str, message_id : str | int, chat_id: str | int):
    # Get Tokens 
    TOKENS = datat.GET_DATA()
    # Start Loop 
    for ii in TOKENS:
        if Temp_data['checker_stat'] == False:
            return
        USERSDATA, CH_INFO , STST = await TETSING_BOT(TOKENS[ii],ii, LIST_ID, message_id, chat_id)
        if int(ii) == len(TOKENS):
                await LANCH_TETSING(CH_INFO,LIST_ID, None, None,ii,message_id, chat_id, 'No Tokens ☇, DONE ✓.' ) 
                CROVET_LIST = CROVET_USERDATE_TYPE_LIST(USERSDATA)
                FILE_CROVET = TEMP_FILE(CROVET_LIST)
                Send_Document(CONFIG['API_KEY'], chat_id, FILE_CROVET)
                return
    
        if STST['STATES'] == 'FLOOD' and len(STST['DONE_USERNAME']) > 1:
            # FILTERS LIST 
            USERNAME_LIST = LIST_TEMP[LIST_ID]
            DONEUSERNAME = STST['DONE_USERNAME']
            [USERNAME_LIST.remove(uu) for uu in DONEUSERNAME]
            LIST_TEMP[LIST_ID] = USERNAME_LIST
            await LANCH_TETSING(CH_INFO,LIST_ID, None, None,ii,message_id, chat_id, 'Next Token ☇.' )
            continue

        elif STST['STATES'] == 'DOONE' : 
            CROVET_LIST = CROVET_USERDATE_TYPE_LIST(USERSDATA)
            FILE_CROVET = TEMP_FILE(CROVET_LIST)
            Send_Document(CONFIG['API_KEY'], chat_id, FILE_CROVET)
            return
        
        
