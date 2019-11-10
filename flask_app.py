from flask import Flask, jsonify, request
import requests
import json
from random import choice
from codeBrewAsistant import whereIsWaldo, format_response, format_txt

app = Flask(__name__)

# GET is allowed, so that you can test on http://bezza.pythonanywhere.com/slack (without using slack)
@app.route('/slack', methods=['POST', 'GET'])
def slack_slash_command():
    form = request.form.to_dict(flat=False)
    if form:
        print(format_txt(form.get('text', [''])[0]).startswith("where is waldo"))
        if format_txt(form.get('text', [''])[0]).startswith("where is waldo"):
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

        return format_response("OK")

    return format_response("No form found!")
