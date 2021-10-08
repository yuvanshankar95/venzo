from flask import Flask, render_template, request
from backend import Login
import webbrowser
import tweepy
from pyre import Add,Fetch,Remove



#twitter csunsumerkeys and tokens
auth = tweepy.OAuthHandler("L257qgdPIAy49BicnSfTTXdZ0", "KtiGNxeKgVNeOxsDbW9sU9QfwOKzc1k0sGp9x8QGNZ9c37QjDe")
# "AAAAAAAAAAAAAAAAAAAAANDPUQEAAAAAoJH%2BsG9G84S5Y6Pt9QD6n11ILk8%3DJZQbpByutD23GDNfmBWZlaOYn83NdXo1n4O2P99dnZKTaioLOO")


#
application = Flask(__name__)

@application.route('/')
def index():

    return render_template('index.html')


@application.route('/', methods=['POST'])
def login():
    global auth
    redirect_user = auth.get_authorization_url()
    webbrowser.open(redirect_user)
    return render_template('tweets.html')
@application.route("/pin",methods=['POST'])
def data():
    pin = request.form['pin']
    global auth
    auth.get_access_token(pin)
    api = tweepy.API(auth)
    timeline = ""
    tweets = api.user_timeline(tweet_mode="extended")
    # timeline += "<h3>"+api.me()+"</h3>"
    public_tweets = api.home_timeline()

    token = auth.access_token
    Remove(token).del_data()
    for tweet in public_tweets:
        id = tweet.id
        add = Add(token,tweet.user.name,tweet.text,str(tweet.created_at))
        add.add_to_db()
        # timeline += "<p class='tweet'>"+tweet.text +" created at "+ str(tweet.created_at) +" posted by <span>"+ tweet.user.name+"</span> </p>"
        # user = api.get_user(tweet)
        # print(tweet.user)
        # print(tweet.text,tweet.created_at,tweet.id)
    
        fetch_data = Fetch(token)
        data = fetch_data.get_data()
        data1=[]
        for key,val in data.items():
            data1.append(val)


    return render_template('timeline.html',data=data1)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port='5001')
