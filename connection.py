import requests, urllib.parse
from auth import auth_headers
from config import BASE_URL

def request(action,method,params=None):
    path = "/api/v1" + action
    if params:
        path+="?"+urllib.parse.urlencode(params)
    headers = auth_headers(method,path)
    req = requests.get(BASE_URL+ path,headers=headers)
    return req.json()



