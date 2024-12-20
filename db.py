from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Collections
users_col = db["users"]
premium_col = db["premium"]
messages_col = db["messages"]
analytics_col = db["analytics"]
