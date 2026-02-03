from . import collection

coll_exists = collection.find_one({"init": True})

def reset_collection():
    if coll_exists:
        collection.delete_many({})
    return