from app import app, render_template

def render_hello_world():
    return render_template('hello_world.html')

def show_user_profile(username):
    return 'Hello, %s' % username

def redirect_page(username):
    return render_template('redirect_to_user.html', username=username)
