import json

reactions = {
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

# Calculates the number of messages participants send
def num_messages_per_user(data):
    mydict = {}
    participants = data["participants"]
    messages = data["messages"]
    for participant in participants:
        for message in messages:
            if "content" in message:
                user = message["sender_name"]
                if (user == participant["name"]):
                    if user in mydict:
                        mydict[user] += 1
                    else:
                        mydict[user] = 1
    return mydict

# Calculates the number of reacts participants send
def num_reacts_per_user(data):
    mydict = {}
    participants = data["participants"]
    user_dict = init_user_dict(data)
    for participant in participants:
        for user, reacts in user_dict.items():
            for content, meta in reacts.items():
                actor = meta["actor"]
                if actor == participant["name"]:
                    if actor in mydict:
                        mydict[actor] += 1
                    else:
                        mydict[actor] = 1
    return mydict

# Return message(s) with at least minct reacts
def messages_with_at_least_min_reacts(data, minct):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if "content" in message and "reactions" in message:
            if len(message["reactions"]) >= minct:
                mydict[message["content"]] = message["reactions"]
    return mydict

# Take in react and return how many of those reacts each user received
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

# Take in react and return how many of those reacts each user sent
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
    
# Take in a user and return the frequency of reacts they received
def reacts_for_user(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        if user == target:
            for content, meta in reacts.items():
                react = list(reactions.keys())[list(reactions.values()).index(meta["react"])]
                if react in mydict:
                    mydict[react] += 1
                else:
                    mydict[react] = 1
    return mydict

# Take in a user and return the frequency of reacts they sent
def reacts_by_user(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        for content, meta in reacts.items():
            if meta["actor"] == target:
                react = list(reactions.keys())[list(reactions.values()).index(meta["react"])]
                if react in mydict:
                    mydict[react] += 1
                else:
                    mydict[react] = 1
    return mydict

# Take in a user and return the a dictionary of the people who reacted to them and what they reacted
def num_reacts_by_actor_for_user(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        if user == target:
            for content, meta in reacts.items():
                actor = meta["actor"]
                react = list(reactions.keys())[list(reactions.values()).index(meta["react"])]
                if actor in mydict:
                    if react in mydict[actor]:
                        mydict[actor][react] += 1
                    else:
                        mydict[actor][react] = 1
                else:
                    mydict[actor] = {}
                    mydict[actor][react] = 1
    return mydict

# Take in a user and return the a dictionary of the people who they reacted to and what they reacted
def num_reacts_by_actor_by_user(data, target):
    mydict = {}
    user_dict = init_user_dict(data)
    for user, reacts in user_dict.items():
        for content, meta in reacts.items():
            if meta["actor"] == target:
                react = list(reactions.keys())[list(reactions.values()).index(meta["react"])]
                if user in mydict:
                    if react in mydict[user]:
                        mydict[user][react] += 1
                    else:
                        mydict[user][react] = 1
                else:
                    mydict[user] = {}
                    mydict[user][react] = 1
    return mydict

# Loop over reacts and call a method (that takes in a react)
def react_loop(data, method):
    mydict = {}
    for name, react in reactions.items():
        mydict[name] = method(data, react)
    return mydict

# Loop over users and call a method (that takes in a user)
def user_loop(data, method):
    mydict = {}
    participants = data["participants"]
    for participant in participants:
        mydict[participant["name"]] = method(data, participant["name"])
    return mydict

def main():
    with open('dont_commit.json') as f:
        data = json.load(f)

    # mydict = num_messages_per_user(data)
    # mydict = num_reacts_per_user(data)
    # mydict = messages_with_at_least_min_reacts(data, 3)
    # mydict = react_loop(data, receivers_of_react)
    # mydict = react_loop(data, senders_of_react)
    # mydict = user_loop(data, reacts_for_user)
    # mydict = user_loop(data, reacts_by_user)
    # mydict = user_loop(data, num_reacts_by_actor_for_user)
    # mydict = user_loop(data, num_reacts_by_actor_by_user)

    for k, v in mydict.items():
        print(k, v)
        # for k1, v1 in v.items():
            # print(k, k1, v1)

if __name__ == '__main__':
    main()
