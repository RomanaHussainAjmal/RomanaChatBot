import json
from flask import Flask
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return '{"Student Number": "200530943", "Student Name":"Romana Hussain"}'

@app.route('/webhook',methods=['GET'])
def index():
    #Connect to the API anf get the JSON file.
    api_url='https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,explicit'
    headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url, headers=headers) #Connect to openweather and read the JSON response.
    r=response.json() #Conver the JSON string to a dict for easier parsing.

    if "joke" in r:
        return  "Joke: " + str(r['joke'])
    else:
        return "Setup: " + str(r['setup'])  + "Punch:" + str(r['delivery'])