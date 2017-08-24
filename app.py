from flask import Flask, request, Response
from query_api.history import history
import os

# Initialize the Flask application
app = Flask(__name__)

''' Getting data from post requests '''
@app.route("/", methods=["POST"])
def info():
    data = request.get_json()
    try:
        # only used for once for app verification
        return (data["challenge"])
    except:
        history(data).data_distribution()
    return(":)")

@app.route("/channels/<channel_name>", methods=["GET"])
def getting_history(channel_name):
    # Getting channel info
    file_path = "channels/{}.json".format(channel_name)
    with open(file_path, "r") as channel:
        history = channel.read()
        channel.close()
    return (history)





if __name__ == '__main__':
    # Creating necesary directories and files if they dont exist
    channel_ref = "channels/channel_ref.json"
    if not os.path.exists("channels"):
        os.makedirs("channels")
    open(channel_ref, "a").close()
    # Run the app :)
    app.run(host="0.0.0.0",
            debug=True)