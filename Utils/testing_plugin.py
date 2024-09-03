from pyrogram import enums
import requests
from user_agent import generate_user_agent
import asyncio

def CHACK_USERNAME(username : str):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):return True
    else:return False


def CHACK_CH(username : str):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'View in Telegram'
        )
        >= 0
    ):return True
    else:return False



USERDATE_TYPE_LIST = {
    enums.UserStatus.ONLINE:[],
    enums.UserStatus.OFFLINE:[],
    enums.UserStatus.RECENTLY:[],
    enums.UserStatus.LAST_WEEK:[],
    enums.UserStatus.LAST_MONTH:[],
    enums.UserStatus.LONG_AGO:[],
}

TETSING_INFO = {
    'DC':0,
    'OK':0,
    'CH':0,
    'UNOT':0,
    'ERR':0,
}