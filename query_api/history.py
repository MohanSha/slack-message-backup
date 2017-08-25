import json
import os
from datetime import datetime

class history:
    def __init__(self, data):
        self.data = data

    def data_distribution(self):
        ''' Checks if a new channel was created or if new messeges have arrived '''
        event_type = self.data["event"]["type"]

        if event_type == "channel_created":
            self.channel_created()
        elif event_type == "message":
            self.message_posted()
        else:
            print(json.dumps(self.data, indent=4))

        print(json.dumps(self.data, indent=4))


    def channel_created(self):
        '''
            Creates new file for channel & Adds the id and the name of the channel
        '''

        channel_name = self.data["event"]["channel"]["name_normalized"]
        channel_id = self.data["event"]["channel"]["id"]
        file_path = "channels/{}.json".format(channel_name)
        file = open(file_path, "w+")
        file.close()

        # adding channel and id to a dict for reference
        channel_ref = "channels/channel_ref.json"
        with open(channel_ref, "r") as ref_file:
            ref = ref_file.read()
            ref_file.close()
        try:
            ref = json.loads(ref)
        except:
            ref = {}

        ref.update({channel_id: channel_name})

        with open(channel_ref, "w") as ref_file:
            ref_file.write(json.dumps(ref, indent=4))
            ref_file.close()

    def message_posted(self):
        user_id = self.data["event"]["user"]
        text = self.data["event"]["text"]
        channel_id = self.data["event"]["channel"]
        ts = self.data["event"]["ts"]
        time = datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S')

        # Getting user name using the user id
        with open("users/users.json", "r") as users:
            find_user = users.read()
            users.close()

        user_name = find_user[user_id]

        # Getting the name of the channel based on the channel id
        with open("channels/channel_ref.json", "r") as channel_ref:
            ref = json.loads(channel_ref.read())
            channel_name = ref[channel_id]
            channel_ref.close()

        file_path = "channels/{}.json".format(channel_name)
        with open(file_path, "r") as channel:
            try:
                # When the file is not empty
                content = json.loads(channel.read())
            except:
                content = {}
            channel.close()

        content.update({time:
                        [{"user": user_name}
                        , {"text":text}
                        ]})

        # Writting new messeges into the file
        with open(file_path, "w") as channel:
            channel.write(json.dumps(content, indent=4))
            channel.close()