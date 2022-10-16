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
    if 'error' in r:
        return '{"fulfillmentMessages": [ {"text": {"text": [" No quotes available for the given/empty Anime input. Some Anime suggestions are : Hyouka , Youjo Senki , Bungou Stray Dogs 2nd Season , Fullmetal Alchemist: Brotherhood , Mahouka Koukou no Rettousei , Boku wa Tomodachi ga Sukunai NEXT , Gunbuster "]} } ]}' 
    else:
        return '{"fulfillmentMessages": [ {"text": {"text": [\" Quote from '+ AnimeShowName +' anime :' + r[0]['quote'] + ' \"]} } ]}'

@app.route('/')
def hello():
    return '<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script> <df-messenger intent="WELCOME" chat-title="RomanaHussainAssn2" agent-id="f8d18fe6-6dea-427f-ba7b-44d84e9ddee6" language-code="en" ></df-messenger>{"Student Number": "200530943", "Student Name":"Romana Hussain"}'

@app.route('/webhook',methods=['POST'])
def index():

    body = request.json

    if(len(body['queryResult']['parameters']['AnimeShowName'])!=0):
        return apiCall(body['queryResult']['parameters']['AnimeShowName'])

    elif (len(body['queryResult']['parameters']['AnimeShowName1'])!=0):
        return apiCall(body['queryResult']['parameters']['AnimeShowName1'])

    elif (len(body['queryResult']['parameters']['AnimeShowName2'])!=0):
        return apiCall(body['queryResult']['parameters']['AnimeShowName2'])

    elif (len(body['queryResult']['parameters']['AnimeShowName3'])!=0):
        return apiCall(body['queryResult']['parameters']['AnimeShowName3'])

    elif (len(body['queryResult']['parameters']['AnimeShowName4'])!=0):
        return apiCall(body['queryResult']['parameters']['AnimeShowName4'])
    
    else :
        return apiCall("")