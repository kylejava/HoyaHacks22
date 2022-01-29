import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
cred = credentials.Certificate('hoyahacks-339701-firebase-adminsdk-hlqfr-7de4c062b8.json')
firebase_admin.initialize_app(cred,
{
'databaseURL': 'https://hoyahacks-339701.firebaseio.com/'
})

db = firestore.client()
doc_ref = db.collection(u'users')
docs = doc_ref.stream()


data = {

    u'name':u'New Test',
    u'phone_number':456,
    u'sign':'New Test!!!'
}

doc_ref.document(u'two').set(data)

for doc in docs:
    pprint(f'{doc.id} => {doc.to_dict()}')
