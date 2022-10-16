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
        return '{"fulfillmentMessages": [ {"text": {"text": [" No quotes available for the given Anime name. Choose from : Hyouka , Youjo Senki , Bungou Stray Dogs 2nd Season , Fullmetal Alchemist: Brotherhood , Tokyo Ghoul √A , Mahouka Koukou no Rettousei , Boku wa Tomodachi ga Sukunai NEXT , Joker Game , Avatar: The Last Airbender , Charlotte , ReLIFE , Soul Eater , Psycho-Pass Extended Edition , Naruto , Detective Conan , Death Parade , Darker than Black - Kuro no Keiyakusha: Gaiden , Haikyuu!! Second Season , Nekomonogatari: Kuro , Gekijōban Gintama Kanketsu-hen: Yorozuya yo Eien Nare , Naruto Shippuuden , Tanaka-kun wa Itsumo Kedaruge , Little Busters! , Fairy Tail , Aoharu x Kikanjuu , Subete ga F ni Naru , Danganronpa The Animation , Ookami Shoujo To Kuro Ouji , Hotarubi no Mori e , Assassination Classroom , Hunter X Hunter , Date A Live , Bleach , Noragami , The Melancholy of Haruhi Suzumiya , Yu-Gi-Oh! Arc-V , Owarimonogatari , Monogatari Series: Second Season , Magi - The Labyrinth of Magic , Cardcaptor Sakura , xxxHOLiC , No Game No Life , Danshi Koukousei no Nichijou , Shirobako , Katanagatari , One Piece , 3-gatsu no Lion , Seishun Forget! , Yojouhan Shinwa Taikei , Tokyo Ghoul:re , Bungou Stray Dogs , Gurren Lagann , JoJo's Bizarre Adventure: Stardust Crusaders , Uchouten Kazoku , Dice: The Cube That Changes Everything , Re:Zero kara Hajimeru Isekai Seikatsu , Kimi no Na wa , Ao Haru Ride , Yahari Ore No Seishun Love Come Wa Machigatteiru , Darker than Black: Gemini of the Meteor , Days TV , Love Live! School idol project TV 2/2014 , Natsume Yuujinchou , Three Days of Happiness , Wolf Girl & Black Prince , La Corda D'Oro - primo passo , Whistle! , Berserk , Higurashi No Naku Koro Ni , Durarara!! , Tamako Market , Eureka Seven , Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e , Boku no Hero Academia , Rokudenashi Majutsu Koushi to Akashic Records , Psycho-Pass , Legend of Zelda , Koe no Katachi , Koi to Uso , Nanbaka , Spice and Wolf , Sakurasou no Pet na Kanojo , Nisekoi , Isshūkan Friends , Kono Subarashii Sekai ni Shukufuku wo! , Mayoiga , Liar Game , Shingeki no Bahamut: Genesis , Kakegurui , Ore Monogatari!! , Akame ga KILL! , Gunbuster "]} } ]}' 
    else:
        return '{"fulfillmentMessages": [ {"text": {"text": [\" Quote from given anime :' + r[0]['quote'] + ' \"]} } ]}'

@app.route('/')
def hello():
    return '{"Student Number": "200530943", "Student Name":"Romana Hussain"}'

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