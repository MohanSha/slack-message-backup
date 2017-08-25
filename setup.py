#!/bin/python3
import os
import requests
import json

'''
    Creates: Files for all the channels already created,
             References between already created user ids and user names
'''

def getting_channels(token):
    '''
        Creates a file per channel
    '''
    url = "https://slack.com/api/channels.list?token={}".format(token)
    response = requests.get(url)
    channels_list = response.json()

    chanel_ref = {}

    for channels in channels_list["channels"]:
        file_path = "channels/{}.json".format(channels["name"])
        file = open(file_path, "w+")
        file.close()

def getting_users():
    '''
        Creates references for users
    '''
    url = "https://slack.com/api/users.list?token={}".format(token)
    response = requests.get(url)
    user_list = response.json()

    with open("users/users.json", "a+") as user_file:
        user_file.seek(0,0)
        user_names = user_file.read()
        user_file.close()

    try:
        user_names = json.loads(user_names)
    except:
        user_names = {}

    for user in user_list["members"]:
        user_id = user["id"]
        user_name = user["name"]
        user_names.update({user_id: user_name})

    with open("users/users.json", "w") as user_file:
        user_file.write(json.dumps(user_names, indent=4))
        user_file.close()




if __name__ == "__main__":
    token = os.getenv("token_slack")
    getting_channels(token)
    getting_users()