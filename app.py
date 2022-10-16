import json
from flask import Flask, request
import requests
app = Flask(__name__)
app.debug = True


def apiCall(AnimeShowName):
    #Connect to the API anf get the JSON file.
    api_url='https://animechan.vercel.app/api/quotes/anime?title=' + AnimeShowName
    headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url, headers=headers) #Connect to openweather and read the JSON response.
    r=response.json() #Conver the JSON string to a dict for easier parsing.
    return '{"fulfillmentMessages": [ {"text": {"text": [\"' + r[0]['quote'] + ' \"]} } ]}'

@app.route('/')
def hello():
    return '{"Student Number": "200530943", "Student Name":"Romana Hussain"}'

@app.route('/webhook',methods=['POST'])
def index():

    body = request.json

    if(body['queryResult']['parameters']['AnimeShowName'].length!=0):
        apiCall(body['queryResult']['parameters']['AnimeShowName'])

    elif (body['queryResult']['parameters']['AnimeShowName1'].length!=0):
        apiCall(body['queryResult']['parameters']['AnimeShowName1'])

    elif (body['queryResult']['parameters']['AnimeShowName2'].length!=0):
        apiCall(body['queryResult']['parameters']['AnimeShowName2'])

    elif (body['queryResult']['parameters']['AnimeShowName3'].length!=0):
        apiCall(body['queryResult']['parameters']['AnimeShowName3'])

    elif (body['queryResult']['parameters']['AnimeShowName4'].length!=0):
        apiCall(body['queryResult']['parameters']['AnimeShowName4'])
    
    else :
        apiCall("")