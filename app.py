import os

import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():    
    return render_template("index.html")

@app.route("/Translate", methods=(["POST"]))
def translate():
    jsonData = request.get_json()
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Translate this to standard Spanish:\n\n"+jsonData["input_text"],
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
    
    resp = str(response.choices[0].text)
    resp = resp.strip(' it\n\n')
    return resp

