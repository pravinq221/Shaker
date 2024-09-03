from pyrogram import types 
from config import Temp_data

    
class HOME_KEYBAORD:

    def MENU_KEYBARD():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='╰SATRT TESTING ϟ╯' if Temp_data['checker_stat'] == False else 'STOP',  callback_data='START_CHECKER'),
            ],
            [
                types.InlineKeyboardButton(text='╰ADD TOKEN╯'  , callback_data='ADD_TOKEN'),
            ],
        ])
    def BACK_HOME():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='•╰ BACK ',  callback_data='BACK_MENU')     
            ]
        ])
    def SELECT_CHECKER_TYPE():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='╰ Random',  callback_data='START_CHECK_RANDOM'),
                types.InlineKeyboardButton(text=' List ╯',  callback_data='START_CHECK_LIST')
            ],
            [
                types.InlineKeyboardButton(text='•╰ BACK ',  callback_data='BACK_MENU')
            ]
        ])
    
    def START_CH_LIST(LIST_ID: str):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='•╰START CHECKERS ϟ ╯', callback_data=f'START_CH_LIST|{LIST_ID}')
            ]
        ])
    
    def STOP_CHECKER():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='•╰ STOP', callback_data='STOP_TESTING'),
                types.InlineKeyboardButton(text='•╰ BACK ', callback_data='BACK_MENU')
            ]
        ])
    
    def RANDOM_LIST_KEYBOARD():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='XXXXX', callback_data="RANDT_1"),
                types.InlineKeyboardButton(text='XXXXXX', callback_data="RANDT_2")
            ],[
                types.InlineKeyboardButton(text='X_X_X', callback_data="RANDT_3"),
                types.InlineKeyboardButton(text='X_X_X_X', callback_data="RANDT_4")
            ],[
                types.InlineKeyboardButton(text='•╰ BACK ',  callback_data='BACK_MENU')

            ]
        ])