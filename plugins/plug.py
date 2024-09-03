from pyrogram import filters, types
from config import Temp_data, app, LIST_TEMP
from helpers import message as Messages
from helpers import keyboard as Keyboard


class My_filters:

    def is_check(data):
        def func(flt, _, message: types.Message):
            return Temp_data[flt.data[0]] == flt.data[1]
        return filters.create(func, data=data)
    
    def is_split(data):
        def func(flt, _,query: types.CallbackQuery):
            return query.data.split('|')[0] == flt.data
        return filters.create(func, data=data)



async def LANCH_TETSING(CH_INFO : list,LIST_ID: str | int,USERNAME: str,USERNAME_STAT,TOKEN_ID, message_id: int | str, chat_id: str | int ,STATS: str):
    try:
        return await app.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Messages.HOME_MESSAGE['TENSING_MESSAGE'].format(
                len(LIST_TEMP[LIST_ID]),USERNAME,USERNAME_STAT,
                CH_INFO['OK'], CH_INFO['ERR'], CH_INFO['CH'], CH_INFO['UNOT'], CH_INFO['DC'],TOKEN_ID,
                STATS), reply_markup=Keyboard.HOME_KEYBAORD.STOP_CHECKER()
        )
    except:
        pass