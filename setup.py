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



if __name__ == "__main__":
    token = os.getenv("token_slack")
    getting_channels(token)
    getting_users()