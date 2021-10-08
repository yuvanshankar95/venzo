import pyrebase

# firebase credentials

config = {
    "apiKey": "AIzaSyDmCPhy0WQphZD_gZoc40fYwcamU6QRCpk",
    "authDomain": "venzo-2d888.firebaseapp.com",
    "databaseURL": "https://venzo-2d888-default-rtdb.firebaseio.com",
    "projectId": "venzo-2d888",
    "storageBucket": "venzo-2d888.appspot.com",
    "messagingSenderId": "308946271573",
    "appId": "1:308946271573:web:c22e193442bacacf0783dc",
    "measurementId": "G-XFD5H6G3GC"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class Add:
    def __init__(self,token,name,tweet,created):
        self.token = token
        self.name = name
        self.tweet = tweet
        self.created = created

    def add_to_db(self):
        global db
        db.child(self.token).push({"name":self.name,"tweet":self.tweet,"created_at":self.created})

class Fetch:
    def __init__(self,token):
        self.token=token
    
    def get_data(self):
        global db
        data = db.child(self.token).get()
        return data.val()
class Remove:
    def __init__(self,token):
        self.token = token
    
    def del_data(self):
        global db
        db.child(self.token).remove()
        return
