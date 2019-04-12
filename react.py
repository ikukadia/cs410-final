from __future__ import division
import json

reacts = {
    "love": u'\xf0\x9f\x98\x8d',
    "haha": u'\xf0\x9f\x98\x86',
    "wow": u'\xf0\x9f\x98\xae', 
    "sad": u'\xf0\x9f\x98\xa2',
    "angry": u'\xf0\x9f\x98\xa0',
    "like": u'\xf0\x9f\x91\x8d',
    "dislike": u'\xf0\x9f\x91\x8e',
}

# Maps messages to their reacts/the reacts' actors
def init_react_dict(data, user):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if (message["sender_name"] == user and "content" in message and "reactions" in message):
            for react in message["reactions"]:
                mydict[message["content"]] = {"react": react["reaction"], "actor": react["actor"]}
    return mydict

# Maps users to the previous dict
def init_user_dict(data):
    mydict = {}
    participants = data["participants"]
    for participant in participants:
        user = participant["name"]
        mydict[user] = init_react_dict(data, user)
    return mydict

# Take in react and return user who received most reacts of that type
def receivers_of_react(data, react):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        for content, meta in reacts.items():
            if (meta["react"] == react):
                if user in mydict:
                    mydict[user] += 1
                else:
                    mydict[user] = 1
    return mydict

# Take in react and return user who sent most reacts of that type
def senders_of_react(data, react):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        for content, meta in reacts.items():
            if (meta["react"] == react):
                user = meta["actor"]
                if user in mydict:
                    mydict[user] += 1
                else:
                    mydict[user] = 1
    return mydict

# Returns either receiver of react or sender of react
def users_vs_reacts(data, receive):
    mydict = {}
    for name, react in reacts.items():
        mydict[name] = receivers_of_react(data, react) if receive else senders_of_react(data, react)
    return mydict
    
# Return messages with most reacts
def messages_with_most_reacts(data):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if "content" in message and "reactions" in message:
            mydict[message["content"]] = len(message["reactions"])
    maxct = max(val for val in mydict.values())
    return [key for key, val in mydict.items() if val == maxct]
    
# Take in a user and return the frequency of reacts they received
def reacts_for_user(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        if user == target:
            for content, meta in reacts.items():
                react = meta["react"]
                if react in mydict:
                    mydict[react] += 1
                else:
                    mydict[react] = 1
    return mydict

# Take in a user and return the a dictionary of the people who reacted to them and what they reacted
def num_reacts_by_actor(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        if user == target:
            for content, meta in reacts.items():
                actor = meta["actor"]
                react = meta["react"]
                if actor in mydict:
                    if react in mydict[actor]:
                        mydict[actor][react] += 1
                    else:
                        mydict[actor][react] = 1
                else:
                    mydict[actor] = {}
                    mydict[actor][react] = 1
    return mydict

def main():
    with open('dont_commit.json') as f:
        data = json.load(f)
    
    mydict = num_reacts_per_user(data)
    for k, v in mydict.items():
        print(k, v)

if __name__ == '__main__':
    main()