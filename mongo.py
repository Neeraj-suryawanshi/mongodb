import pymongo
client = pymongo.MongoClient("mongodb+srv://Neerajineuron:Nrjmikki@cluster0.jxhn5os.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)