from pymongo import MongoClient
mongodb = "mongodb+srv://Alex_Oldgarden:Qq646546545@nothing.djovyht.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb)
database = client.get_database("default")
users_collection = database.get_collection("users")
