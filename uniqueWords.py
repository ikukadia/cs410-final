import json
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from collections import Counter 
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

en_stops = set(stopwords.words('english'))


def concatonate(participant, messages):
    a = ""

    for i in range(len(messages)):
        if messages[i]['sender_name'] == participant:
            try:
                if(messages[i]['content'] and 
                "joined the" not in messages[i]['content'] and "voted for" not in messages[i]['content']
                and "set your nickname" not in messages[i]['content'] 
                and "set the nickname" not in messages[i]['content'] and "created a poll" not in messages[i]['content']):
                    a += " " + messages[i]['content'].lower()
                
            except KeyError:
                pass
    words = a.split()
    real_words = []

    for i in range(len(words)):
        if words[i] not in en_stops:
            real_words.append(words[i])

       

    gg = Counter(real_words)
    most_occur = gg.most_common(20)
    print(most_occur)
    num_words = len(words)

    s = set(words)
    return len(s)/num_words


def main():
    start = time.time()
    with open('dont_commit.json', 'r') as f:
        messenger_dict = json.load(f)
    participant_list = messenger_dict['participants']
    messages = messenger_dict['messages']

    jobs = []
    threads = len(participant_list)

    for i in range(len(participant_list)):
        print(participant_list[i])
       
        print(concatonate(participant_list[i]['name'], messages))
        print("----------------------------------")
    end = time.time()
    print(end -start)

if __name__ == '__main__':
    main()