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


app = Flask(__name__)

fave_tv_shows = ["Narcos", "White Collar", "Mr. Robot", "Breaking bad", "The office"]

@app.route('/')
def hello_world():
    # return ''
    return render_template(
        "index.html",
        len = len(fave_tv_shows), 
        fave_tv_shows = fave_tv_shows
    )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    debug = True
    )