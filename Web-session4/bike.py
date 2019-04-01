from pymongo import MongoClient
from faker import Faker
from random import randint, choice

faker = Faker()
mongo_uri = "mongodb+srv://admin:admin@c4e28-cluster-pigup.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
bike_database = client.db_bike
bike_collection = bike_database["bike"]
# for i in range(50):
#     bike = {
#         "model": choice(["Honda", "Lead", "Vision", "Wave", "PCX"]),
#         "daily_fee": randint(100000, 10000000),
#         "image": faker.url(),
#         "year": randint(1990, 2019)
#     }
#     bike_collection.insert_one(bike)
#     print(i+1)