from flask import Flask, render_template, redirect,request,url_for
from flask_debugtoolbar import DebugToolbarExtension

from forms import GenerateActivityForm

from helpers import determine_price, get_videos, get_activity_by_type
from models import connect_db, db
# # from werkzeug.exceptions import Unauthorized

BORED_API_BASE_URL = "https://www.boredapi.com/api/activity/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///random-fun'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "girlslovebeyonce"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
#db.drop_all()
db.create_all()

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/generate', methods=["GET", "POST"])
def generate():
    """Generates Activity."""

    form = GenerateActivityForm()

    if form.validate_on_submit():
        # for later here is where you save in the dB, before redirecting towards a get request that renders a page
        # here though, you don't need to save anything, as we agreed that saving is done once a person interacts with the activity
        # either by saving the activity to their list
        return redirect(url_for('show_activity', activity=form.activity.data,price=form.minprice.data,accessible=form.accessible.data))

    return render_template('generate.html', form=form)

@app.route('/activity', methods=["GET"])
def show_activity():
    """Shows generated Activity."""
    type = request.args.get('activity')
    price = request.args.get('price')
    accessible = request.args.get('accessible')
    data = get_activity_by_type(type)
    result_activity = data["activity"]
    result_price = data["price"]
    result_type = data["type"]
    
    result_price_str = determine_price(result_price)
    
    videos = get_videos(result_activity, 5)
    activity_info = {'activity': result_activity, 'price': result_price_str, 'type': result_type}
    return render_template('activity.html', activity_info=activity_info, videos=videos)

# @app.route('/activity_videos', methods=["GET"])
# def show_videos():
#     """Shows videos based on recommended activity"""
#     # request = youtube.search().list(
#     #     part='snippet', 
#     #     maxResults=1,
#     #     q='Pickles'
#     # )

#     # response = request.execute()
#     # videoId = response['items'][0]['snippet']['id']['videoId']
#     response = get_videos('playing piano', 1)
#     videoId = response['items'][0]['id']['videoId']

#     return render_template('videos.html', videoId=videoId)