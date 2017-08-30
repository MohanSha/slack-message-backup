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

@main.route("/", methods=["POST"])
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
        history(data).data_distribution()
    return(":)")


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
        history = channel.read()
        channel.close()
    return (history)