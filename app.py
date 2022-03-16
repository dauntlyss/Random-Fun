from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db
from forms import GenerateActivityForm
# from werkzeug.exceptions import Unauthorized

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "girlslovebeyonce"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

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
    
    
    return render_template('activity.html')