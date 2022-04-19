from flask import Flask, session
import pyrebase
from firebase_admin import firestore, credentials, initialize_app

from customer_side import config



application=Flask(__name__)
application.secret_key='jaapuchkeaa'


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
orders_collection = db.collection('orders') # orders collections
medicines_collection = db.collection("medicines") # shops (pharmacies-admin) database



from customer_side import (
    server,
    database,
    authentication,
    cart
)