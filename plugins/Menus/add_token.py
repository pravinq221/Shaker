# Require Module 
from pyrogram import Client as app, filters, types
from pyromod.exceptions import ListenerTimeout
from pyrogram.handlers import MessageHandler
import requests, json

# Require Bot Plugin .
from helpers import  keyboard as Keyboard
from config import Temp_data, datat


def CHECK_TOKEN(TOEKN :str):
    api = f"https://api.telegram.org/bot{TOEKN}/getWebhookInfo"
    response = json.loads(requests.get(api).text)
    return response['ok']


# Add Token Handler 
@app.on_callback_query(filters.regex('^ADD_TOKEN$'))
async def ADD_TOKEN(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.id, 
            text='قم بي ارسال توكن البوت : \n \n - مثل : 6778848921:AAHEfVAdH8JKR4aYkS0OrdOJTsPhvKQyeD \n\n' , reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
        )
    

    # liten token
    try: 
        data = await app.listen(chat_id=query.message.chat.id, timeout=30, filters=filters.text)
        TOKEN = data.text
    except ListenerTimeout as Err:
        return
    

    msg_data = await app.send_message(
            chat_id=query.message.chat.id,
            text='انتضر من فضلك جاري التحقق .',
        )
    # Check Token
    if not CHECK_TOKEN(TOKEN):
        await app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=msg_data.id,
            text='عذرن توكنك غير صالح قم بي ارسال توكن صالح .',
                reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
        )
        return
    Temp_data['ADD_TOKEN'] = False
    # CHeck Token exists 
    if datat.EXISTS_TOKEN(TOKEN):
        await app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=msg_data.id,
            text='عذران توكنك موجود بل فعل .',
                reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
        )
        return
    
    # Add Token 
    datat.ADD_TOKEN(TOKEN)
    await app.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=msg_data.id,
            text='تم اضافة توكنك بي نجاج , عدد توكناتك الان : {}'.format(datat.GET_TOKEN_COUNT()),
                reply_markup=Keyboard.HOME_KEYBAORD.BACK_HOME()
        )





