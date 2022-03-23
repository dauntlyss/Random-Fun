from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from forms import GenerateActivityForm
import requests

from helpers import get_videos
# from models import connect_db, db
# # from werkzeug.exceptions import Unauthorized

BORED_API_BASE_URL = "https://www.boredapi.com/api/activity/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///random-fun'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "girlslovebeyonce"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# connect_db(app)
# db.create_all()

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/generate', methods=["GET", "POST"])
def generate():
    """Generates Activity."""

    form = GenerateActivityForm()

    if form.validate_on_submit():

        return redirect(f"/activity")

    return render_template('generate.html', form=form)

@app.route('/activity', methods=["GET"])
def show_activity():
    """Shows generated Activity."""
    form = GenerateActivityForm()
    type = form.activity.data
    res = requests.get(f"{BORED_API_BASE_URL}", params={'type': type})
    data = res.json()
    activity = data["activity"]
    price = data["price"]
    type = data["type"]
    
    if price >= .8:
        print('getting in')
        price = '$$$$'
    elif price >= .6:
        price = '$$$'
    elif price >= .4:
        price = '$$'
    else:
        price = '$' 

    print('****************************')
    
    response = get_videos('french bread', 5)
    print(response)
    activity_info = {'activity': activity, 'price': price, 'type': type}
    return render_template('activity.html', activity_info=activity_info)

@app.route('/activity_videos', methods=["GET"])
def show_videos():
    """Shows videos based on recommended activity"""
    get_videos('playing piano', 1)
    return render_template('videos.html')