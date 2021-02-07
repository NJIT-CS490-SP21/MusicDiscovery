from flask import Flask, render_template
import os

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