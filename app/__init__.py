from flask import Flask, session
import pyrebase
from firebase_admin import firestore, credentials, initialize_app

from app import config, customer_authentication


application = Flask(__name__)


# set up firebase configs for firebase authentication 
# this uses the config.py file
firebase_config = config.firebaseConfig
pb = pyrebase.initialize_app(firebase_config)
auth = pb.auth()

# set up firestore credentials and database
# this uses the firestore_config.json file
cred = credentials.Certificate("app/firestore_config.json")
default_app = initialize_app(cred)
db = firestore.client()

# firebase databases (collections) intialization
users_collection = db.collection("users") #  users (customers) collection
shops_collection = db.collection("shops") # shops (pharmacies-admin) database

application.secret_key='lmaodead'


from app import (
    server,
    config,
    profile,
    database,
    customer_authentication,
    shop_authentication
    )