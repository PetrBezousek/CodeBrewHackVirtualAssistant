from flask import Flask, jsonify, request
import requests
import json
from random import choice
from codeBrewAsistant import (whereIsWaldo,
                             format_response,
                             format_txt,
                             whereIs)

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
            print(resp)
            return format_response(resp)
        # WHEREIS
        elif user_input.startswith("whereis"):
            whereIs(user_input)
        # HELP
        elif user_input.startswith("help"):
            resp = {
                "text": "Brian is happy to help you./n`whereis` lorem ipsum dolo",
                "attachments": [
                {
                    "fallback": "Helping cat",
                    "text": "Cat will help!",
                    "image_url": 'https://giphy.com/gifs/cat-fire-rescue-phJ6eMRFYI6CQ',
                    "thumb_url": 'https://giphy.com/gifs/cat-fire-rescue-phJ6eMRFYI6CQ'
                }
            ]}
        return format_response("OK")

    return format_response("No form found!")
