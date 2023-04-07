from pymongo import MongoClient

mongodb = "mongodb+srv://Alex_Oldgarden:Qq646546545@nothing.djovyht.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb)
database = client.get_database("default")
users_collection = database.get_collection("users")

#users_collection.delete_many({"_id": "0000"})

#users_collection.update_one({"_id": 231}, {"$set$":{"last_name": "Kry"}})

#users_collection.find_one(
#    {"_id: 478538"}, {"name: Pablo"}
#)

#new_user = {
#    "_id": 1000,
#    "name": "Ivan",
#    "last_name": "Martyn"
#}
#users_collection.insert_one (new_user)
all_users = users_collection.find({})
for user in all_users:
    print(user)