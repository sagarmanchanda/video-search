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
    user = {}

    if 'username' in session:
        user['logged_in'] = True
        user['username'] = session['username']
    else:
        user['logged_in'] = False
        user['username'] = None

    if request.method == "POST":
        search_query = request.form['search_query']
        results = find_results(search_query)
    return render_template('home.html', results=results, video_playing=video_playing, video_playing_obj=video_playing_obj, user=user)

@app.route("/play_video/<video_id>")
def play_video(video_id):
    results = []
    video_playing = True
    video_playing_obj = get_video_by_id(video_id)
    user = {}

    if 'username' in session:
        user['logged_in'] = True
        user['username'] = session['username']
    else:
        user['logged_in'] = False
        user['username'] = None

    results = get_similiar_videos(video_id, 10, 0)
    return render_template('home.html', results=results, video_playing=video_playing, video_playing_obj=video_playing_obj, user=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == "POST":
        if check_user(request.form['l-username'], request.form['l-password']):
            session['username'] = request.form['l-username']
            return redirect(url_for('search'))
        else:
            error = "Incorrect username or password"
    return render_template('login-register.html', error=error)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('search'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    error = ""
    if request.method == "POST":
        if request.form['r-password'] == request.form['r-cpassword']:
            if add_user(request.form['r-username'], request.form['r-password']):
                error = "Registration Successful. Please Login."
            else:
                error = "Registration Unsuccessful. Try again."
        else:
            error = "Passwords did not match."
    return render_template('login-register.html', error=error)

@app.route("/like/<video_id>")
def like(video_id):
    return video_id

if __name__ == "__main__":
    app.secret_key = '12345678'
    app.run(debug = True)