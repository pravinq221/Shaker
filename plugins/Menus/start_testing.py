# Require Module 
from pyrogram import filters,types
import asyncio

# Require Bot Plugin .
from helpers import message as Message, keyboard as Keyboard
from config import app ,Temp_data, LIST_TEMP, datat
from Plugins.plug import My_filters
from Plugins.function import LOAD_FILE, LOAD_LIST, RANDNAME
from Utils.START_HADNLER import TETSING_HANDLER



@app.on_callback_query(filters.regex('^START_CHECKER$'))
async def START_CHECKER(_, query: types.CallbackQuery):
    # Edit Message , SELECT_RANDOM_TYPE
    if Temp_data['checker_stat'] == True:
        ms_load = await app.edit_message_text(
                chat_id=query.message.chat.id, 
                message_id=query.message.id,
                text=Message.HOME_MESSAGE['STOP_CHECK'],
            )
        await asyncio.sleep(0.7)
        Temp_data['checker_stat'] = True if Temp_data['checker_stat'] == False else False
        Temp_data['LIST_CHECKER_ID'] = None
        await app.edit_message_text(
            chat_id=query.message.chat.id, 
            message_id=query.message.id,
            text=Message.HOME_MESSAGE['MENU'],
            reply_markup=Keyboard.HOME_KEYBAORD.MENU_KEYBARD()
        )
        return
    await app.edit_message_text(
        chat_id=query.message.chat.id, 
        message_id=query.message.id,
        text=Message.HOME_MESSAGE['SELECT_RANDOM_TYPE'],
        reply_markup=Keyboard.HOME_KEYBAORD.SELECT_CHECKER_TYPE()
    )

# Get username list 
@app.on_callback_query(filters.regex('START_CHECK_LIST'))
async def START_CHECK_LIST(_, query: types.CallbackQuery):
    if datat.GET_TOKEN_COUNT() < 1:
        await app.edit_message_text(
        chat_id=query.message.chat.id, 
        message_id=query.message.id,
        text='No Tokens in Bot Please Add Tokens .',
        reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
          )
        return
    await app.edit_message_text(
        chat_id=query.message.chat.id, 
        message_id=query.message.id,
        text='Send Username List .',
        reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
    )
    Temp_data['ON_MESSAGE'] = 'GET_RANDOM_LIST'
    # START ON DOC HANDLER
    @app.on_message(My_filters.is_check(('ON_MESSAGE', 'GET_RANDOM_LIST')))
    async def GET_USERNAME_LIST(_, message: types.Message):
        Temp_data['ON_MESSAGE'] = None
        ms_load = await app.send_message(
            chat_id=message.chat.id, 
            text=Message.HOME_MESSAGE['LODIN_LIST'])
        
        # Get File data 
        File = await app.download_media(message.document.file_id, in_memory=True)
        FileData = LOAD_FILE(File)
        usernames , len_username = LOAD_LIST(FileData)
        LIST_ID = RANDNAME(5)
        ACCONT_LEN = datat.GET_TOKEN_COUNT()
        LIST_TEMP.update({LIST_ID:usernames})
        await app.edit_message_text(
            chat_id=message.chat.id, 
            message_id=ms_load.id ,
            text=Message.HOME_MESSAGE['START_CH_LIST'].format(len_username, ACCONT_LEN),
            reply_markup=Keyboard.HOME_KEYBAORD.START_CH_LIST(LIST_ID)
        )

# start checker list       
@app.on_callback_query(My_filters.is_split('START_CH_LIST'))
async def START_CH_LIST(_, query: types.CallbackQuery):
    # Get List id
    LIST_ID = query.data.split('|')[1]

    # Edit Checker Stat
    Temp_data['checker_stat'] = True if Temp_data['checker_stat'] == False else False
    message_data = await app.edit_message_text(
            chat_id=query.message.chat.id, 
            message_id=query.message.id ,
            text='With Start Testing ..'
        )
    # START TESTING HANDLER
    await TETSING_HANDLER(LIST_ID, message_data.id , message_data.chat.id)

# STOP TESTING 
@app.on_message(filters.regex('^STOP_TESTING$'))
async def STOP_TESTING(_, query: types.CallbackQuery):
    Temp_data['checker_stat'] = False
    await app.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.id, 
        text='DONE STOP CHECKERS >.' , reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
    )



