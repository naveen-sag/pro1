
# firebase_config.py
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("don/firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smaids-66571-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

