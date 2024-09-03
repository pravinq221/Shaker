import json 
import os 


class Datat:

    def __init__(self):
        self.PAT = r'./data/tokens.json'

        if not os.path.exists(self.PAT):
            with open(self.PAT, 'w') as JS:
                json.dump({}, JS, indent=3)


    def GET_DATA(self):
        with open(self.PAT, 'r') as JSObj:
            return json.load(JSObj)
        
    def UPDATE_DATA(self, obj: dict):
        with open(self.PAT, 'w') as JSObj:
            json.dump(obj, JSObj, indent=3)
    
    def ADD_TOKEN(self, TOKEN: str):
        data = self.GET_DATA()
        data.update({len(data)+1:TOKEN})
        self.UPDATE_DATA(data)

    def EXISTS_TOKEN(self, TOKEN: str):
        data = dict(self.GET_DATA())
        return TOKEN in data.values()
    
    def GET_TOKEN_COUNT(self):
        return len(self.GET_DATA())

    def FILTESR_TOKEN(self):
        obj = {}
        data = self.GET_DATA()
        for i, ii in enumerate(data):
            obj.update({i+1:data[ii]})
        self.UPDATE_DATA(obj)

    def DELET_TOKEN(self, TOKEN_ID: str):
        data = self.GET_DATA()
        data.pop(TOKEN_ID)
        self.UPDATE_DATA(data)
        self.FILTESR_TOKEN()
        



    


