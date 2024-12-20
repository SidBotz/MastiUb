import json
from db import users_col

def load_language(language_code):
    try:
        with open(f"Languages/{language_code}.json", "r") as lang_file:
            return json.load(lang_file)
    except FileNotFoundError:
        with open(f"Languages/eng.json", "r") as lang_file:  # Default to English
            return json.load(lang_file)

def get_user_language(user_id):
    user = users_col.find_one({"user_id": user_id})
    if user and "language" in user:
        return user["language"]
    return "eng"  # Default language

def is_premium(user_id):
    from db import premium_col
    return premium_col.find_one({"user_id": user_id}) is not None

def add_premium(user_id, days=30):
    from db import premium_col
    premium_col.update_one(
        {"user_id": user_id},
        {"$set": {"expires": time.time() + days * 86400}},
        upsert=True
    )

def remove_premium(user_id):
    from db import premium_col
    premium_col.delete_one({"user_id": user_id})
