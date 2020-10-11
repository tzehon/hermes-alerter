from google.cloud import firestore

def update_bags(available_bags):
    db = firestore.Client()

    bags_ref = db.collection(u'bags').document(u'vYvPTrf6xjrcY0VfgrgC')
    bags_ref.set({
        u'bag': available_bags
    })

def get_bags():
    db = firestore.Client()

    bags_ref = db.collection(u'bags')
    docs = bags_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        bags = doc.to_dict()
        bags['bag'].sort()
        print(bags['bag'])
        return bags['bag']
