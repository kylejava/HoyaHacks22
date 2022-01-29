import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
from User import *
cred = credentials.Certificate('hoyahacks-339701-firebase-adminsdk-hlqfr-7de4c062b8.json')
firebase_admin.initialize_app(cred,
{
'databaseURL': 'https://hoyahacks-339701.firebaseio.com/'
})

db = firestore.client()
doc_ref = db.collection(u'users')
docs = doc_ref.stream()


def addToDatabase(user):
    data = {
        u'name':user.name,
        u'phone_number':user.phone_number,
        u'sign':user.sign
    }
    doc_ref.document().set(data)

x = User("Kyle Edward Galido Java", 1234567890, "Aries")
addToDatabase(x)


for doc in docs:
    pprint(f'{doc.id} => {doc.to_dict()}')
