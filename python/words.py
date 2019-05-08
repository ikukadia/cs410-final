import nltk
from nltk.corpus import words
import json
import operator
import collections
import string
#only needs to be run once
def download_words():
    nltk.download()

def get_words():
    word_list = words.words()
    return word_list

def hasNumbersPunc(inputString):
    hasNumbers = any(char.isdigit() for char in inputString)
    invalidChars = set(string.punctuation)
    hasPunc = any(char in invalidChars for char in inputString)
    return hasPunc or hasNumbers


def get_misspells_dict(data):
    result = {}
    participants = data["participants"]
    for participant in participants:
        user = participant["name"]
        result[user] = 0
    participants = data["participants"] #participants[0]["name"]

    all_words = get_words()
    
    #names = []
    #for i in participants:
    #    names.append(i["name"])


    all_messages = data["messages"]
    misspelled_words = {}
    most_common = {}

    count = 0
    for message in all_messages:
        count += 1
        if count > 1000:
            break
        if ("content" in message):
            text = message["content"]
            user = message["sender_name"]
            for word in text.split():
                word = word.replace(".", "")
                word = word.lower()
                found = False
                if word in misspelled_words.keys():
                    result[user] += 1
                    misspelled_words[word] += 1
                    found = True
                elif '\'' not in word and len(word) > 1 and not hasNumbersPunc(word) and word not in all_words:
                    result[user] += 1
                    misspelled_words[word] = 1
                    found = True

                if found:
                    if user in most_common.keys():
                        curr_dict = most_common[user]
                        if word in curr_dict.keys():
                            most_common[user][word] += 1
                        else:
                            most_common[user][word] = 1
                    else:
                        most_common[user] = {}
                        most_common[user][word] = 1

    return result, most_common


def main():
    #run this once - opens a popup; go to corpus then words and hit download
    #download_words()
    data = {}

    with open('dont_commit.json') as f:
        data = json.load(f)

    misspellings_count, most_common = get_misspells_dict(data);
    print(misspellings_count)

    for user,users_words in most_common.items():
        sorted_words = collections.OrderedDict(sorted(users_words.items(), key=lambda kv: kv[1], reverse=True))
        #sorted_words = sorted(users_words.items(), key=operator.itemgetter(0),reverse=True)
        word = list(sorted_words.keys())[0]
        count = sorted_words[word]
        print("user = " + user + " word = " + word + " count = " + str(count))

if __name__ == '__main__':
    main()