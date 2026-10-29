import json


def loadFromJson():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data

def saveToJson(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
        
def register(data, username, password):
    if username in data ["users"]:
        return False
    data["users"][username] = {"password": password, "accounts": []}
    saveToJson(data)
    return True

def login(data, username, password):
    data = loadFromJson()
    user = data["users"].get(username)
    if user and user["password"] == password:
        return True
    return False

