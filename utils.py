from pymongo import MongoClient
from decouple import config


client = MongoClient(config('CONNECTION_STRING'))
db = client[config('DB_NAME')]

articles = db["article"]
