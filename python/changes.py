import json
from utils import get_participants, format_dict

# This function returns how many times a user's nickname has been changed 
# and how many times a user has changed a nickname 
def set_nickname(data):
    # warning: does not work for users json (your nickname)
    mydict = {}
    changed_names = {}
    name_got_changed = {}
    messages = data["messages"]
    for message in messages:
        if ("content" in message.keys() and "set the nickname for" in message["content"]):
            for changer in get_participants(data):
                key_phrase = "set the nickname for"
                if (changer) in message["sender_name"] and (key_phrase) in message["content"]:
                    for user in get_participants(data):
                        if(user in message["content"]):
                            nickname = message["content"].split("to",1)[1] 
                            if(changer in changed_names.keys()):
                                changed_names[changer] += 1
                            else:
                                changed_names[changer] = 1
                            if(user in name_got_changed.keys()):
                                name_got_changed[user] += 1
                            else:
                                name_got_changed[user] = 1
    return name_got_changed, changed_names

# This function counts how many times a user has changed the emoji
def set_emoji(data):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if ("content" in message.keys() and "set the emoji to" in message["content"]):
            for user in get_participants(data):
                if (user) in message["sender_name"]:
                    emoji = message["content"].split("to",1)[1] 
                    if(user in mydict.keys()):
                        mydict[user] += 1
                    else:
                        mydict[user] = 1
    print(mydict)
    return mydict


def main():
    with open('dont_commit.json') as f:
        data = json.load(f)
    #print(set_nickname(data))
    print(format_dict(set_emoji(data)))

    f = open("./../changes.txt", "w+")
    f.write(format_dict(set_emoji(data)))
    f.close()

if __name__ == '__main__':
    main()