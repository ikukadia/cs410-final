import io
import json
from utils import get_messages

def write_all_messages(data, user):
    
    f = open("./word_cloud/text/%s_words.txt" %user, "w+")
    
    for message in get_messages(data, user):
        if "content" in message.keys():
            f.write(message["content"])
    
    f.close()

def main():
    with open('dont_commit.json') as f:
        data = json.load(f)
    write_all_messages(data, "Suhirtha Raj")

if __name__ == '__main__':
    main()