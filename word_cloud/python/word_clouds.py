import io
import json
from utils import get_messages
from utils import get_participants

def write_all_messages(data, user):
    
    f = open("./../text/%s_words.txt" %user, "w+", encoding="utf-8")
    
    for message in get_messages(data, user):
        if "content" in message.keys() and  "joined the" not in message['content'] and " sent a live location" not in message['content'] and "set the emoji to" not in message['content'] and "changed the" not in message['content'] and "voted for" not in message['content'] and "set your nickname" not in message['content'] and "set the nickname" not in message['content'] and "created a poll" not in message['content']:
            f.write(message["content"])
    f.close()


def create_json_wordcloud(data, user):
    f = open("./../vega/%s_words.vg.json" %user, "w+", encoding="utf-8")
    f.write("{ \"$schema\": \"https://vega.github.io/schema/vega/v5.json\", \"width\": 800, \"height\": 400, \"padding\": 0, \"data\": [ { \"name\": \"table\", \"url\": \"./word_cloud/text/%s_words.txt\", \"transform\": [ { \"type\": \"countpattern\", \"field\": \"data\", \"case\": \"upper\", \"pattern\": \"[\\\\w']{3,}\", \"stopwords\": \"(i|me|my|myself|we|us|our|ours|ourselves|you|your|yours|yourself|yourselves|he|him|his|himself|she|her|hers|herself|it|its|itself|they|them|their|theirs|themselves|what|which|who|whom|whose|this|that|these|those|am|is|are|was|were|be|been|being|have|has|had|having|do|does|did|doing|will|would|should|can|could|ought|i'm|you're|he's|she's|it's|we're|they're|i've|you've|we've|they've|i'd|you'd|he'd|she'd|we'd|they'd|i'll|you'll|he'll|she'll|we'll|they'll|isn't|aren't|wasn't|weren't|hasn't|haven't|hadn't|doesn't|don't|didn't|won't|wouldn't|shan't|shouldn't|can't|cannot|couldn't|mustn't|let's|that's|who's|what's|here's|there's|when's|where's|why's|how's|a|an|the|and|but|if|or|because|as|until|while|of|at|by|for|with|about|against|between|into|through|during|before|after|above|below|to|from|up|upon|down|in|out|on|off|over|under|again|further|then|once|here|there|when|where|why|how|all|any|both|each|few|more|most|other|some|such|no|nor|not|only|own|same|so|than|too|very|say|says|said|shall)\" }, { \"type\": \"formula\", \"as\": \"angle\", \"expr\": \"[-45, 0, 45][~~(random() * 3)]\" }, { \"type\": \"formula\", \"as\": \"weight\", \"expr\": \"if(datum.text=='VEGA', 600, 300)\" } ] } ], \"scales\": [ { \"name\": \"color\", \"type\": \"ordinal\", \"domain\": {\"data\": \"table\", \"field\": \"text\"}, \"range\": [\"#d5a928\", \"#652c90\", \"#939597\"] } ], \"marks\": [ { \"type\": \"text\", \"from\": {\"data\": \"table\"}, \"encode\": { \"enter\": { \"text\": {\"field\": \"text\"}, \"align\": {\"value\": \"center\"}, \"baseline\": {\"value\": \"alphabetic\"}, \"fill\": {\"scale\": \"color\", \"field\": \"text\"} }, \"update\": { \"fillOpacity\": {\"value\": 1} }, \"hover\": { \"fillOpacity\": {\"value\": 0.5} } }, \"transform\": [ { \"type\": \"wordcloud\", \"size\": [800, 400], \"text\": {\"field\": \"text\"}, \"rotate\": {\"field\": \"datum.angle\"}, \"font\": \"Helvetica Neue, Arial\", \"fontSize\": {\"field\": \"datum.count\"}, \"fontWeight\": {\"field\": \"datum.weight\"}, \"fontSizeRange\": [12, 56], \"padding\": 2 } ] } ] } " %user)

    f.close()


def main():
    with open('./../../dont_commit.json') as f:
        data = json.load(f)
    for user in get_participants(data):  
        write_all_messages(data, user)
    for user in get_participants(data):  
        create_json_wordcloud(data, user)

if __name__ == '__main__':
    main()