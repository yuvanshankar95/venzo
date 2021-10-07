from flask import Flask, render_template, request
from backend import Login
import webbrowser
import tweepy

auth = tweepy.OAuthHandler("L257qgdPIAy49BicnSfTTXdZ0", "KtiGNxeKgVNeOxsDbW9sU9QfwOKzc1k0sGp9x8QGNZ9c37QjDe")
# "AAAAAAAAAAAAAAAAAAAAANDPUQEAAAAAoJH%2BsG9G84S5Y6Pt9QD6n11ILk8%3DJZQbpByutD23GDNfmBWZlaOYn83NdXo1n4O2P99dnZKTaioLOO")



app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/', methods=['POST'])
def login():
    global auth
    redirect_user = auth.get_authorization_url()
    webbrowser.open(redirect_user)
    return render_template('tweets.html')
@app.route("/pin",methods=['POST'])
def data():
    pin = request.form['pin']
    global auth
    auth.get_access_token(pin)
    api = tweepy.API(auth)
    timeline = ""
    for item in tweepy.Cursor(api.user_timeline).items():
        timeline += "<p>"+ item.full_text + "</p>"
        print(item.full_text)



    return timeline

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
