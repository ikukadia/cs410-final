import io
import json
from utils import get_messages
from utils import get_participants

def write_all_messages(data, user):
    
    f = open("./../text/%s_words.txt" %user, "w+", encoding="utf-8")
    
    for message in get_messages(data, user):
        if "content" in message.keys() and  "joined the" not in message['content'] and "voted for" not in message['content'] and "set your nickname" not in message['content'] and "set the nickname" not in message['content'] and "created a poll" not in message['content']:
            f.write(message["content"])
    f.close()

def main():
    with open('./../../dont_commit.json') as f:
        data = json.load(f)
        for user in get_participants(data):  
            write_all_messages(data, user)

if __name__ == '__main__':
    main()