
# Requier Bots Plugins 
from pyrogram import Client as app ,filters ,types 

# Requier BOt PLugins 
from config import  datat, Temp_data
from helpers import message as Message, keyboard as Keybaord


# start bot handler
@app.on_message(filters.private & filters.regex('^/start$'))
async def START_BOT(app: app ,message: types.Message):
    await app.send_message(
        chat_id=message.chat.id, 
        text=Message.HOME_MESSAGE['MENU'].format(datat.GET_TOKEN_COUNT()),
        reply_markup=Keybaord.HOME_KEYBAORD.MENU_KEYBARD()
    )
    



# On Callback Data .
@app.on_callback_query(filters.regex('^BACK_MENU$'))
async def BACK_HOME(app :app, query: types.CallbackQuery):
    Temp_data['ON_MESSAGE'] = None
    Temp_data['ADD_ACCONET'] = False
    
    await app.edit_message_text(
        chat_id=query.message.chat.id, 
        message_id=query.message.id,
        text=Message.HOME_MESSAGE['MENU'].format(datat.GET_TOKEN_COUNT()),
        reply_markup=Keybaord.HOME_KEYBAORD.MENU_KEYBARD()
    )


# rando usernames menu 
@app.on_message(filters.regex('^RANDOM_USERNAME$'))
async def RANDOM_USERNAME(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.id, 
            text='Edd' , reply_markup=Keybaord.RANDOM_LIST_KEYBOARD()
        )
