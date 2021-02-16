from flask import Flask, render_template
import os
import requests
import random


clientID = "bf8e821aeb774a3d9aaa3322b80d78ce"
clientSecret = os.getenv('clientSecret') #TODO store in heroku

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

artistIDs = ["5K4W6rqBFWDnAN6FQUkS6x", "2h93pZq0e7k5yf4dywlkpM", "1Mxqyy3pSjf8kZZL4QVxS0", "2YZyLoL8N0Wb9xBt1NhZWg", "1Xyo4u8uXC1ZmMpatF05PJ"]
randIndex = random.randrange(5)


base_url = "https://api.spotify.com/v1/artists/"+ artistIDs[randIndex]+ "/top-tracks"
market = "?market=US"
base_url = base_url + market


response = requests.get(base_url, headers=headers)
response = response.json()
response = response["tracks"]

topTracks = []
trackArtist = ""
trackImageUrls = []
trackExternalUrls = []

#getting artist
singer = response[0]["artists"][0]["name"]
trackArtist = singer

#function to get top 3 tracks info
def getTop3Tracks(response):
    
    counter = 0
    while(counter < 3):
        
        trackName = response[counter]["name"]
        topTracks.append(trackName)
        
        trackUrl = response[counter]["external_urls"]["spotify"]
        trackExternalUrls.append(trackUrl)
        
        trackImageUrl = response[counter]["album"]["images"][1]["url"]
        trackImageUrls.append(trackImageUrl)
        
        counter += 1
     



getTop3Tracks(response)

#authenticating with genuis 

base_url = 'http://api.genius.com'
lyrics_links = []

#TODO store in heroku

def getAllLyricLinks(songTitles):
    for track in songTitles:
        genuisToken=os.getenv('')

        headers = {'Authorization': 'Bearer {token}'.format(token=genuisToken)}
        search_url = base_url + "/search"
        song_title = track
        params = {'q': song_title}
        genuis_response = requests.get(search_url, params=params, headers=headers)

        genuis_data = genuis_response.json()
    
        currentSongLyricUrl = genuis_data["response"]["hits"][0]["result"]["url"]
    
        lyrics_links.append(currentSongLyricUrl)

    
    
getAllLyricLinks(topTracks)
    



app = Flask(__name__)



@app.route('/')
def hello_world():
    # return ''
    return render_template(
        "index.html",
        top3Tracks = topTracks,
        len = len(topTracks),
        topArtist = trackArtist,
        top3ImgUrls = trackImageUrls,
        top3ExtUrl = trackExternalUrls,
        lyric_urls = lyrics_links
    )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    debug = True
    )
    