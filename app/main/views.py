from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_required

from . import main
# from .forms import Nameform
from .. import db
from ..models import User

from flask import Flask, request, Response
from .. query_api.history import history
import os
import json


@main.route("/", methods=["POST", "GET"])
def slack_auth():
    '''
        On the first call with Slack's API it authenticates the server.
        After that it passes the json data to other functions
    '''
    data = request.get_json()
    try:
        # only used for once for app verification
        return (data["challenge"])
    except:
        try:
            history(data).data_distribution()
        except:
            pass
    return(redirect(url_for("main.directory"), code=302))

@main.route("/directory", methods=["GET", "POST"])
@login_required
def directory():
    '''
        Displays a list of links for all the available channels
    '''
    search = request.args.get("search", "none")
    with open("channels/channel_ref.json", "r") as chanel_ref:
        ref = json.loads(chanel_ref.read())
        chanel_ref.close()
    channels = []
    for key, value in ref.items():
        channels.append(value)

    return(render_template("directory.html",channel = sorted(channels), search=search))

@main.route("/channel/<channel_name>", methods=["GET"])
@login_required
def getting_history(channel_name=None):
    '''
        Retrives channels history based on a channel name and returns it to
        the desired route
    '''
    # Getting channel info
    file_path = "channels/{}.json".format(channel_name)
    with open(file_path, "r") as channel:
        history = json.loads(channel.read())
        channel.close()
    sorted_dates = sorted(history, key=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    sorted_date = sorted_dates.reverse()
    #return(json.dumps(history, indent=4))
    return (render_template("channel.html", history=history, dates=sorted_dates))

