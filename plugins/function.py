  
import os, random , requests, json
import io 

def RANDNAME(len = 20):
    name = str()
    for i in range(len):
        name+=random.choice("abcdefghijclmnopqrstuvwxyz0987654321")
    return name

def write_bytesio_to_file(filename, bytesio):
    with open(filename, "wb") as outfile:
        outfile.write(bytesio.getbuffer())  


def LOAD_FILE(File: io.BytesIO):
    Name = r'./.temp/' + RANDNAME()
    write_bytesio_to_file(Name, File)
    FileData = open(Name, 'r').read()
    os.remove(Name)
    return FileData

def TEMP_FILE(DATA: str):
    Name = r'./.temp/' + 'R_TESTING.txt'
    with open(Name, 'w') as JSobj:
        JSobj.write(DATA)
    FILE_OBJ = open(Name, 'r').read()
    os.remove(Name)
    return FILE_OBJ


def LOAD_LIST(FileData: str):
    Load = FileData.split('\n')
    return Load, len(Load)


def Send_Document(API_KEY,chat_id, fileobj: str,caption: str = None):
    api_url = f"https://api.telegram.org/bot{API_KEY}/" 
    requests.post(api_url + 'sendDocument', data={'chat_id': chat_id,'caption':caption}, files={'document': fileobj})
            
            


def FILTER_USERNAME_LIST(USERNAME_LIS: list, DONE_USERNAME: list):
    [USERNAME_LIS.remove(i) for i in DONE_USERNAME]
    return USERNAME_LIS

def CROVET_USERDATE_TYPE_LIST(USERDATE_TYPE_LIST:dict):
    STARTIN = ''
    for i in USERDATE_TYPE_LIST:
        userlisttype = '\n'.join(USERDATE_TYPE_LIST[i])
        STARTIN += f'\n# {str(i).split(".")[1]} ( {len(USERDATE_TYPE_LIST[i])} ) :\n{userlisttype}\n' + '='*15
    return STARTIN
