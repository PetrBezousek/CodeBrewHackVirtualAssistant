from flask import Flask, jsonify, request
import requests
import json
from random import choice
from codeBrewAsistant import *

app = Flask(__name__)

# GET is allowed, so that you can test on http://bezza.pythonanywhere.com/slack (without using slack)
@app.route('/slack', methods=['POST', 'GET'])
def slack_slash_command():
    form = request.form.to_dict(flat=False)
    if form:
        if form.get('text', '')[0].lower().strip().startswith("where is waldo"):
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
            return jsonify(resp)

        resp = jsonify(text="OK")
        return resp

    return jsonify(text="No form found!")

