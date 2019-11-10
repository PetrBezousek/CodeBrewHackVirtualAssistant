from flask import Flask, jsonify, request
import requests
import json
from random import choice
from codeBrewAsistant import (whereIsWaldo,
                             format_response,
                             format_txt,
                             whereIs)
from call_api import get_users

app = Flask(__name__)

# GET is allowed, so that you can test on http://bezza.pythonanywhere.com/slack (without using slack)
@app.route('/slack', methods=['POST', 'GET'])
def slack_slash_command():
    form = request.form.to_dict(flat=False)
    if form:
        user_input = format_txt(form.get('text', [''])[0])
        # WALDO
        if user_input.startswith("where is waldo"):
            resp = {
                "text": "You tell me..",
                "attachments": [
                {
                    "fallback": "Find Waldo image",
                    "text": "Snitch the Waldo",
                    "image_url": whereIsWaldo(),
                    "thumb_url": whereIsWaldo()
                }
            ]}
            return format_response(resp)
        # WHEREIS
        elif user_input.startswith("whereis"):
            seeker = form['user_name'][0]
            msg = whereIs(user_input, seeker)

            resp = {
                "text": ""
                ,
                "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": msg
                            }
                        }
                    ]
            }
            return format_response(resp)
        # HELP
        elif user_input.startswith("help"):


            resp = {
                "text": """
                        Brian helps you snith someone.
                    """
                ,
                "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "`whereis` lorem ipsum dolor sit amet"
                            }
                        }
                    ]
            }
        return format_response(resp)

    return format_response("No form found!")
