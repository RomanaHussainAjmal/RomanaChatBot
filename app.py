import json
from flask import Flask, request
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return '{"Student Number": "200530943", "Student Name":"Romana Hussain"}'

@app.route('/webhook',methods=['POST'])
def index():

    body = request.json
    AnimeShowName= body['queryResult']['parameters']['AnimeShowName']

    #Connect to the API anf get the JSON file.
    api_url='https://animechan.vercel.app/api/quotes/anime?title=' + AnimeShowName
    headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url, headers=headers) #Connect to openweather and read the JSON response.
    r=response.json() #Conver the JSON string to a dict for easier parsing.
    return '{"fulfillmentMessages": [ {"text": {"text": \"' + r[0]['quote'] + ' \"} } ]}'