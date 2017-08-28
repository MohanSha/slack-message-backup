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
        Creates a file per channel and updating references
    '''
    url = "https://slack.com/api/channels.list?token={}".format(token)
    response = requests.get(url)
    channels_list = response.json()


    # Getting the channel_rerefence
    with open ("channels/channel_ref.json", "a+")as channel_ref:
        channel_ref.seek(0, 0)
        channel_info = channel_ref.read()
        channel_ref.close()

    try:
        ref = json.loads(channel_info)
    except:
        ref = {}

    # Creating a file per channel
    for channels in channels_list["channels"]:
        file_path = "channels/{}.json".format(channels["name"])
        file = open(file_path, "w+")
        file.close()
        ref.update({channels["id"]: channels["name"]})

    # Updating references for channels
    with open ("channels/channel_ref.json", "w")as channel_ref:
        channel_ref.write(json.dumps(ref, indent=4))
        channel_ref.close()

def getting_users(token):
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


def create_groups(token):
    '''
        Creates files for groups
    '''

    url = "https://slack.com/api/groups.list?token={}".format(token)
    response = requests.get(url)
    groups_list = response.json()

    # Getting the channel_rerefence
    with open ("channels/channel_ref.json", "a+")as channel_ref:
        channel_ref.seek(0, 0)
        channel_info = channel_ref.read()
        channel_ref.close()

    try:
        ref = json.loads(channel_info)
    except:
        ref = {}

    # Creating a file per private channel
    for group in groups_list["groups"]:
        if "mpdm" not in group["name"]:
            file_path = "channels/{}.json".format(group["name"])
        file = open(file_path, "w+")
        file.close()
        ref.update({group["id"]: group["name"]})

    # Updating references for private channels
    with open ("channels/channel_ref.json", "w")as channel_ref:
        channel_ref.write(json.dumps(ref, indent=4))
        channel_ref.close()



if __name__ == "__main__":
    token = os.getenv("token_slack")
    getting_channels(token)
    getting_users(token)
    create_groups(token)