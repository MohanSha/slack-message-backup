from flask import Flask, request, Response
import json
import os

# Initialize the Flask application
app = Flask(__name__)

''' Getting data from post requests '''
@app.route('/', methods=["POST"])
def info():
    data = request.get_json()
    try:
        # only used for once for app verification
        return (data["challenge"])
    except:
        data_distribution(data)
    return(":)")


def data_distribution(data):
    ''' Checks if a new channel was created or if new messeges have arrived '''

    event_type = data["event"]["type"]

    if event_type == "channel_created":
        channel_created(data)
    elif event_type == "message":
        message_posted(data)
    else:
        print(json.dumps(data, indent=4))

    print(json.dumps(data, indent=4))


def channel_created(data):
    '''
        Creates new file for channel & Adds the id and the name of the channel
    '''

    channel_name = data["event"]["channel"]["name_normalized"]
    channel_id = data["event"]["channel"]["id"]
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

def message_posted(data):
    channel_id = data["event"]["channel"]

    # Getting the name of the channel based on the channel id
    with open("channels/channel_ref.json", "r") as channel_ref:
        ref = json.loads(channel_ref)
        channel_name = ref[channel_id]
        channel_ref.close()

    print(channel_name)


if __name__ == '__main__':
    # Creating necesary directories and files if they dont exist
    channel_ref = "channels/channel_ref.json"
    if not os.path.exists("channels"):
        os.makedirs("channels")
    open(channel_ref, "a").close()
    # Run the app :)
    app.run(host="0.0.0.0",
            debug=True)