from app import app
from app.lesson2 import *

@app.route('/')
@app.route('/index')
def index():
    return render_hello_world()

@app.route('/users/<username>')
def user(username):
    return show_user_profile(username)

@app.route('/users/<username>/url')
def redirect_user(username):
    return redirect_page(username)
