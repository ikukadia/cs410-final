import json
import io


# REACTS
# "love" = "\xf0\x9f\x98\x8d"
# "haha" = "\xf0\x9f\x98\x86"
# "wow" = "\xf0\x9f\x98\xae" 
# "sad" = "\xf0\x9f\x98\xa2"
# "angry" = "\xf0\x9f\x98\xa0"
# "like" = "\xf0\x9f\x91\x8d"
# "dislike" = "\xf0\x9f\x91\x8e"

def init_react_dict(data, user):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if (message["sender_name"] == user and "content" in message and "reactions" in message):
            for react in message["reactions"]:
                mydict[message["content"]] = {"react": react["reaction"], "actor": react["actor"]}
    return mydict

def init_user_dict(data):
    mydict = {}
    participants = data["participants"]
    for participant in participants:
        user = participant["name"]
        mydict[user] = init_react_dict(data, user)
    return mydict

def users_with_reacts(data, react):
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
    
# def messages_with_most_reacts(data, react):

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

# def actor_who_gives_most_reacts(data, user):

def main():
    with open('dont_commit.json') as f:
        data = json.load(f)

    mydict = users_with_reacts(data, u'\xf0\x9f\x98\x86')
    print(mydict)

if __name__ == '__main__':
    main()