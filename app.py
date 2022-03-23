from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from forms import GenerateActivityForm
import requests

from helpers import determine_price, get_videos
from googleapiclient.discovery import build
# from models import connect_db, db
# # from werkzeug.exceptions import Unauthorized

BORED_API_BASE_URL = "https://www.boredapi.com/api/activity/"
API_KEY = 'AIzaSyBMtqOKrUGkSTWxqeecCLN5ywVL7xkVbBE'
youtube = build('youtube', 'v3', developerKey=API_KEY)

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
    
    price = determine_price(price)

    print('****************************')
    
    response = get_videos(activity, 5)
    print(response)
    video1_title = response['items'][0]['snippet']['title']
    video2_title = response['items'][1]['snippet']['title']
    video3_title = response['items'][2]['snippet']['title']
    video4_title = response['items'][3]['snippet']['title']
    video5_title = response['items'][4]['snippet']['title']

    video1_id = response['items'][0]['id']['videoId']
    video2_id = response['items'][1]['id']['videoId']
    video3_id = response['items'][2]['id']['videoId']
    video4_id = response['items'][3]['id']['videoId']
    video5_id = response['items'][4]['id']['videoId']

    activity_info = {'activity': activity, 'price': price, 'type': type}
    return render_template('activity.html', activity_info=activity_info, video1_title=video1_title, video2_title=video2_title, video3_title=video3_title, video4_title=video4_title, video5_title=video5_title, video1_id=video1_id, video2_id=video2_id, video3_id=video3_id, video4_id=video4_id, video5_id=video5_id)

@app.route('/activity_videos', methods=["GET"])
def show_videos():
    """Shows videos based on recommended activity"""
    # request = youtube.search().list(
    #     part='snippet', 
    #     maxResults=1,
    #     q='Pickles'
    # )

    # response = request.execute()
    # videoId = response['items'][0]['snippet']['id']['videoId']
    response = get_videos('playing piano', 1)
    videoId = response['items'][0]['id']['videoId']

    return render_template('videos.html', videoId=videoId)