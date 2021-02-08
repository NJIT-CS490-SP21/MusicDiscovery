from flask import Flask, render_template
import os
import requests


clientID = "bf8e821aeb774a3d9aaa3322b80d78ce"
clientSecret = os.getenv('clientSecret')

AUTH_URL = 'https://accounts.spotify.com/api/token'


auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': clientID,
    'client_secret': clientSecret,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

base_url = "https://api.spotify.com/v1/search"

#-------------------Requesting track info

q = "?q=i%20wonder"



typeOfContent = "&type=track"

base_url = base_url + q + typeOfContent

response = requests.get(base_url ,headers=headers)

response = response.json()

#-------------------Getting track info

#get track info
trackInfo = response["tracks"]["items"][0]

#get name of song
trackName = trackInfo["name"]

#name of artist of song
trackArtist = trackInfo["artists"][0]["name"]

trackImageUrl = trackInfo["album"]["images"][1]["url"]


app = Flask(__name__)

fave_tv_shows = ["Narcos", "White Collar", "Mr. Robot", "Breaking bad", "The office"]

@app.route('/')
def hello_world():
    # return ''
    return render_template(
        "index.html",
        trackImage = trackImageUrl,
        trackArtist = trackArtist,
        trackName = trackName
    )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    debug = True
    )