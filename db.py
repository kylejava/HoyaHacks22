import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate('hoyahacks-339701-firebase-adminsdk-hlqfr-7de4c062b8.json')
firebase_admin.initialize_app(cred,
{
'databaseURL': 'https://hoyahacks.firebaseio.com/'
})

db = firestore.client()
doc_ref = db.collection(u'applications')
