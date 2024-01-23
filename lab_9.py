import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Sport_Tracker"]
collection = db["tracker"]

def create_event(eventName, eventDuration, burnedCalories):
    event = {"EventName": eventName, "EventDuration": eventDuration, "BurnedCalories": burnedCalories}
    collection.insert_one(event)

def show_events():
    found_events = collection.find({}, {"_id": 0, "EventName": 1, "EventDuration": 1, "BurnedCalories": 1})
    for event in found_events:
        print(event)

def update_event(eventName, newName, newDuration, newBurnedCalories):
    query = {"EventName": eventName}
    new_data = {"$set": {"EventName": newName, "EventDuration": newDuration, "BurnedCalories": newBurnedCalories}}
    collection.update_one(query, new_data)

def delete_event(eventName):
    query = {"EventName": eventName}
    collection.delete_one(query)

create_event("Morning run", "30min", "200")
create_event("Riding my bike", "1hour", "300")
show_events()
print("-------------")
update_event("Morning run", "Morning run", "45min", "200")
show_events()
print("-------------")
delete_event("Morning run")
show_events()
print("-------------")

client.close()
