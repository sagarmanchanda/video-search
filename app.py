from flask import *
from VSauthenticate import *
from VSsearch import *
from VSdatabase import *

#Create a flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Video Search Engine!"

@app.route("/search", methods=['GET', 'POST'])
def search():
    results = []
    video_playing = False
    video_playing_obj = None
    if request.method == "POST":
        search_query = request.form['search_query']
        results = find_results(search_query)
    return render_template('home.html', results=results, video_playing=video_playing, video_playing_obj=video_playing_obj)

@app.route("/play_video/<video_id>")
def play_video(video_id):
    video_playing = True
    video_playing_obj = get_video_by_id(video_id)
    #Populate this list from neo4j, define functions in VSdatabase.py only
    results=[]
    return render_template('home.html', results=results, video_playing=video_playing, video_playing_obj=video_playing_obj)


if __name__ == "__main__":
    app.run()