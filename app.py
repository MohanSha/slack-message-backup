from flask import Flask, request, Response

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

''' Checks if a new channel was created or if new messeges have arrived '''
def data_distribution(data):
    print(data)

'''creates new file for channel '''
def channel_created():
    pass


def message_posted():
    pass

# Run the app :)
if __name__ == '__main__':
  app.run(host="0.0.0.0",
          debug=True)