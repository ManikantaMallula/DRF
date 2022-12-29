import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINTS = 'emp/'

def get_resource(id=None):
    data = {}

    if id is not None:
        data = {'id':id}
    resp = requests.get(BASE_URL+ENDPOINTS, data = json.dumps(data))
    print(requests.status_code)
    print(resp.json())

get_resource()
