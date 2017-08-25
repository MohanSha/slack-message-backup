# Sypnosis

This is a proof of concept to understand better slack's API.
The goal is to successfully backup all the messages in all the channels that
belong to my school's Slack team.

I started this project for two main reasons.

+ First: I wanted to explore Slack Api and its functionalities

+ Second: I want to backup and access the history of different channels on my
school's Slack team and have access to it whenever we need it.

# Usage

+ Go to [your Slack apps](https://api.slack.com/apps)
+ Create a new app with a Creative App Name 😎
+ Select the Slack team in which you want to integrate the application.
+ Select Event Subscriptions and enable the events.

+ Now on you server, using python3 virtual environment run:

&nbsp;&nbsp;&nbsp;&nbsp;```python3 -m venv .```

&nbsp;&nbsp;&nbsp;&nbsp;```source bin/activate```

&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install -r requirements```

+ Now you should be able to run your application in a server by running

&nbsp;&nbsp;&nbsp;&nbsp;```python3 app.py```

+ Go back to your Event subscriptions and copy paste the url of your server for example:

&nbsp;&nbsp;&nbsp;&nbsp;```http://54.200.102.199:5000/```

+ Now add your desired team events you will at least need user:read, channel:history and
channel:read

+ Under settings select Install App and copy the slack token. On your server export your token

&nbsp;&nbsp;&nbsp;&nbsp;```export token_slack="[Your applicaton's token should start with xoxp-] ```

+ Now you need to set up the neccesary files for user refereces and channels
you can do this by

&nbsp;&nbsp;&nbsp;&nbsp;```python3 setup.py```

Head over to your url with the port 5000 and check if your channels load.

For example:

http://54.200.102.199:5000/channel/general

Now post a message in the general channel and go back to the url reload the page
to see if the new message has been loaded.


This project was build using [Slack Event API](https://api.slack.com/events-api)

Following their documentation to set up your app should be fairly simple. 😀

# References

[Slack API](https://api.slack.com/)

# To do
- Implement user signin and user seesions
- Backup already existing messages
- Handle files uploaded to channels
- Handle threads in messages
- Handle updated messages
- Reload pages automatically
- Add styling to pages, Right now it just returns a boring json file
