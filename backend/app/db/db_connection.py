from . import connect


collection, coll_exists = connect()

def reset_collection():
    if coll_exists:
        collection.delete_many({})
        print("Collection reset")
    return