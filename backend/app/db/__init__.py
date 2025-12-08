from os import environ

if not environ.get("DB_USERNAME"):
    environ["DB_USERNAME"] = "yahiaboukharrata092_db_user"
    
if not environ.get("DB_PASSWORD"):
    environ["DB_PASSWORD"] = "55Xq0fT5gCchfEzK"
    
if not environ.get("APP_NAME"):
    environ["APP_NAME"] = "rag"