from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "c2c6ea8b7bfce19c8b5423c11ea462229c093605"

oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id='Ov23lizhzKPFOPLTx11d',
    client_secret='c2c6ea8b7bfce19c8b5423c11ea462229c093605',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# Home Page
@app.route('/')
def home():
    return """
    <html>
        <body style="background:white; font-family:Arial;">
            <h1 style="color:blue;">Welcome to the GitHub OAuth Demo!</h1>

            <a href="/login" style="font-size:20px;">
                Login with GitHub
            </a>
        </body>
    </html>
    """

# Login Route
@app.route('/login')
def login():
    return github.authorize_redirect(url_for('callback', _external=True))

# GitHub Callback
@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    user = github.get('user').json()

    # Save user in session
    session['user'] = user

    return redirect('/profile')

# Profile Page
@app.route('/profile')
def profile():

    # Unauthorized Access
    if 'user' not in session:
        return """
        <h1>Unauthorized Access</h1>
        <p>You must login first.</p>
        <a href="/login">Login Here</a>
        """, 401

    user = session['user']

    # Successful Login
    return f"""
    <html>
        <body style="font-family:Arial;">
            <h1>Successful Login</h1>

            <h2>GitHub User Data</h2>

            <p><strong>Username:</strong> {user['login']}</p>
            <p><strong>ID:</strong> {user['id']}</p>
            <p><strong>Profile URL:</strong>
                <a href="{user['html_url']}">
                    {user['html_url']}
                </a>
            </p>

            <img src="{user['avatar_url']}" width="120">

            <br><br>

            <a href="/logout">Logout</a>
        </body>
    </html>
    """

# Logout Route
@app.route('/logout')
def logout():

    # Remove user session
    session.pop('user', None)

    return """
    <h1>Logged Out Successfully</h1>

    <p>Try accessing the profile page again:</p>

    <a href="/profile">Go to Profile</a>
    <br><br>
    <a href="/">Back to Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)