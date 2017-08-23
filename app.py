from flask import Flask, request, Response
import json

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

    if event_type is "channel_created":
        channel_created(data)
    else if event_type is "message":
        message_posted(data)
    else:
        print(json.dumps(data, indent=4))

    print(json.dumps(data, indent=4))


def channel_created(data):
    '''creates new file for channel '''

    channel_name = data["event"]["channel"]["name_normalized"]
    channel_id = data["event"]["channel"]["id"]
    file_path = "channels/{}.json".format(channel_name)
    file = open(file_path, "w+")
    file.close()

    # add channel and id to a dict for reference
    ref_file = open("channel_ref.json", "rw+")
    ref = json.loads(ref_file.read())
    ref.update({channel_id: channel_name})
    ref_file.write(json.dumps(ref, indent=4))
    ref_file.close()


def message_posted():
    print("message was posted")
    pass

# Run the app :)
if __name__ == '__main__':
  app.run(host="0.0.0.0",
          debug=True)