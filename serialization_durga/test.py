import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINTS = 'emp/'

def get_resource(id=None):
    data = {}

    if id is not None:
        data = {'id':id}
    resp = requests.get(BASE_URL+ENDPOINTS, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resource(1)


# def create_resource():
#     new_emp = {'ename':'Siri', 'eno':440, 'esal':50000}
#     resp = requests.post(BASE_URL+ENDPOINTS, data= json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# create_resource()

def update_resource():
    new_data = {'ename':'smith', 'eno':660, 'esal':25000}
    resp = requests.put(BASE_URL+ENDPOINTS, data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())

# update_resource()


def delete_resource():
    data = {'id':id}
    resp = requests.delete(BASE_URL+ENDPOINTS, data=json.dumps(data))

# delete_resource()