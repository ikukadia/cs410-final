import io
import json

# returns all messages of given user
# returns a list of message objects
def get_messages(data, user):
    participants = list(map(lambda x: x["name"], data["participants"]))
    if user not in participants:
        return []
    messages = list(filter(lambda x: x["sender_name"] == user, data["messages"]))
    return messages

# returns a list of participants in given JSON
# returns a list of strings
def get_participants(data):
    return list(map(lambda x: x["name"], data["participants"]))

# Calculates the number of messages participants send
def num_messages_per_user(data):
    mydict = {}
    participants = data["participants"]
    messages = data["messages"]
    for participant in participants:
        for message in messages:
            user = message["sender_name"]
            if (user == participant["name"]):
                if user in mydict:
                    mydict[user] += 1
                else:
                    mydict[user] = 1
    return mydict





