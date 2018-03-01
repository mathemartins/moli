from django.shortcuts import render
import pyrebase

config = {
	"apiKey": "AIzaSyBVjggWu4gAUqCtnirx-mT3z-mc4OvGsmI",
    "authDomain": "moli-ba53e.firebaseapp.com",
    "databaseURL": "https://moli-ba53e.firebaseio.com",
    "projectId": "moli-ba53e",
    "storageBucket": "moli-ba53e.appspot.com",
    "messagingSenderId": "467693396993"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()