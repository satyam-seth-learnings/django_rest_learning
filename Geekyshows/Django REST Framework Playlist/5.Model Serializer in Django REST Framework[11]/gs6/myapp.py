import requests
import json

URL='http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# get_data(2)
# get_data()

def post_data():
    data={
        'name':'Sonal',
        'roll':108,
        'city':'Dhanbad'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# post_data()

def upadate_data():
    data={
        'id':6,
        'name':'Jack',
        'city':'Ranchi'
    }

    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# upadate_data()

def delete_data():
    data={'id':6}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

delete_data()