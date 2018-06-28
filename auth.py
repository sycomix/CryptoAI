import time,hmac,hashlib
from config import API_ID, API_SECRET

def auth_headers(method,path):
    expires = str(round(time.time())+10)
    message = method + path+expires
    signature = hmac.new(API_SECRET.encode(),message.encode(),hashlib.sha256).hexdigest()
    return     {
        "api-expires":expires,
        "api-key":API_ID,
        "api-signature": signature}

