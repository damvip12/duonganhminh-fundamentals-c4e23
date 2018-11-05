from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

post = db["post"] 

new_post = {
    "title": "Xin chào mọi người",
    "author": "Dương Anh Minh",
    "content": "Mình chỉ muốn chào thui. Hellu ae"
}


post.insert_one(new_post)

client.close()