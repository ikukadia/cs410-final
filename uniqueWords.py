import json
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time


def concatonate(participant, messages):
    a = ""

    for i in range(len(messages)):
        if messages[i]['sender_name'] == participant:
            try:
                if(messages[i]['content']):
                    a += " " + messages[i]['content'].lower()
            except KeyError:
                pass
    words = a.split()
    num_words = len(words)

    s = set(words)
    return len(s)/num_words


if __name__ == "__main__":
    start = time.time()
    
   
    with open('message_1.json', 'r') as f:
        messenger_dict = json.load(f)
    participant_list = messenger_dict['participants']
    messages = messenger_dict['messages']

    jobs = []
    threads = len(participant_list)

    for i in range(len(participant_list)):
        print(participant_list[i])
        print(concatonate(participant_list[i]['name'], messages))
    end = time.time()
    print(end -start)
