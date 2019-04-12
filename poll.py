import json
from utils import get_participants

def most_mentioned(data):
    mydict = {}
    messages = data["messages"]
    for message in messages:
        if ("content" in message.keys() and "created a poll" in message["content"]):
            for user in get_participants(data):
                if (user) in message["sender_name"]:
                    if(user in mydict.keys()):
                        mydict[user] += 1
                    else:
                        mydict[user] = 1
    return mydict


def main():
    with open('dont_commit.json') as f:
        data = json.load(f)
    print(most_mentioned(data))

if __name__ == '__main__':
    main()