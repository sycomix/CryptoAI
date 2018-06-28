import requests, urllib.parse, json
from auth import auth_headers
from config import BASE_URL

def request(session, action,method,params=None):
    path = "/api/v1" + action
    if params:
        path+="?"+urllib.parse.urlencode(params)
    headers = auth_headers(method,path)
    session.headers.update(headers)
    if method.upper()=="GET":
        req = session.get(BASE_URL+ path)
    elif method.upper()=="POST":
        req = session.post(BASE_URL+ path)
    else: 
        raise ValueError("Method should be 'GET' or 'REQUEST'")
    try:
        response = req.json()
    except json.JSONDecodeError as err:
        response = req
    return response



