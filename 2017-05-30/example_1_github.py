
import requests
import lxml
import json
import time

from PIL import Image
from io import BytesIO

github_root = 'https://api.github.com'


def get_api_info():
    response = requests.get(github_root)

    for k, v in response.json().items():
        print(k, v)


def get_user_data(user):
    r = requests.get('https://api.github.com/users/{user}'.format(user=user))
    return r.json()


def show_avatar(json_data):
    avatar_url = json_data['avatar_url']
    r = requests.get(avatar_url)

    i = Image.open(BytesIO(r.content))
    i.show()

# get_api_info()

# time.sleep(1)

# json_data = get_user_data('piotrkasprzyk')
# print(json_data)
# json_str = json.dumps(json_data)
# print(json_str)
# print(json.loads(json_str))
# print(json_data.keys())
# time.sleep(1)
# show_avatar(json_data)
